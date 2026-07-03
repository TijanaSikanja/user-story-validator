import json
import re
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from models import AgentState
from prompts import INVEST_ANALYSIS_PROMPT

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

# ── ČVOR 1: parse_input ──────────────────────────────────────────
def parse_input(state: AgentState) -> AgentState:
    raw = state["raw_input"]
    
    # Podeli na stories po praznoj liniji ili numerisanju
    parts = re.split(r'\n\s*\n|\n(?=\d+\.)', raw.strip())
    stories = [s.strip() for s in parts if s.strip()]
    
    return {**state, "stories": stories, "current_index": 0, "analyses": []}


# ── ČVOR 2: analyze_invest ───────────────────────────────────────
def analyze_invest(state: AgentState) -> AgentState:
    idx = state["current_index"]
    story = state["stories"][idx]
    
    # Proveri format user story
    format_pattern = r"[Kk]ao .+, [zž]elim .+, kako bih .+|[Aa]s an? .+, I want .+, so that .+"
    format_valid = bool(re.search(format_pattern, story))
    
    # Pozovi LLM
    prompt = INVEST_ANALYSIS_PROMPT.format(story=story)
    response = llm.invoke([HumanMessage(content=prompt)])
    
    try:
        content = response.content
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        result = json.loads(json_match.group() if json_match else content)
        
        scores = result.get("scores", {})
        explanations = result.get("explanations", {})
        recommendations = result.get("recommendations", [])
        total = round(sum(scores.values()) / len(scores), 1) if scores else 0.0
        
    except Exception:
        scores = {k: 0 for k in ["Independent", "Negotiable", "Valuable", "Estimable", "Small", "Testable"]}
        explanations = {k: "Greska pri analizi" for k in scores}
        recommendations = ["Proveriti format user story i pokusati ponovo"]
        total = 0.0
    
    analysis = {
        "story_id": f"US-{idx + 1:03d}",
        "original_text": story,
        "format_valid": format_valid,
        "invest_scores": scores,
        "invest_explanations": explanations,
        "total_score": total,
        "recommendations": recommendations
    }
    
    analyses = state.get("analyses", []) + [analysis]
    next_index = idx + 1
    
    return {**state, "analyses": analyses, "current_index": next_index}


# ── ROUTING ───────────────────────────────────────────────────────
def should_continue(state: AgentState) -> str:
    if state["current_index"] < len(state["stories"]):
        return "analyze_invest"
    return "generate_report"


# ── ČVOR 3: generate_report ──────────────────────────────────────
def generate_report(state: AgentState) -> AgentState:
    analyses = state["analyses"]
    
    # ─ Markdown izvestaj ─
    md_lines = ["# INVEST Izvestaj — User Story Validator\n"]
    
    for a in analyses:
        md_lines.append(f"## {a['story_id']}")
        md_lines.append(f"**Originalni tekst:** {a['original_text']}\n")
        md_lines.append(f"**Format ispravan:** {'Da' if a['format_valid'] else 'Ne'}\n")
        md_lines.append(f"**Ukupni skor: {a['total_score']}/10**\n")
        
        md_lines.append("| Kriterijum | Ocena | Obrazlozenje |")
        md_lines.append("|---|---|---|")
        
        for k in ["Independent", "Negotiable", "Valuable", "Estimable", "Small", "Testable"]:
            score = a["invest_scores"].get(k, 0)
            expl = a["invest_explanations"].get(k, "")
            emoji = "OK" if score >= 7 else "UPOZORENJE" if score >= 4 else "LOSE"
            md_lines.append(f"| {k} | {emoji} {score}/10 | {expl} |")
        
        if a["recommendations"]:
            md_lines.append("\n**Preporuke za poboljsanje:**")
            for r in a["recommendations"]:
                md_lines.append(f"- {r}")
        
        md_lines.append("\n---\n")
    
    # Summary
    all_scores = [a["total_score"] for a in analyses]
    avg = round(sum(all_scores) / len(all_scores), 1) if all_scores else 0
    ready = sum(1 for s in all_scores if s >= 7.0)
    
    md_lines.append("## Rezime")
    md_lines.append(f"- Ukupno analiziranih user stories: **{len(analyses)}**")
    md_lines.append(f"- Prosecni skor: **{avg}/10**")
    md_lines.append(f"- Spremne za sprint (skor >= 7): **{ready}**")
    md_lines.append(f"- Potrebna revizija: **{len(analyses) - ready}**")
    
    # ─ JSON izvestaj ─
    json_report = {
        "summary": {
            "total_stories": len(analyses),
            "average_score": avg,
            "ready_for_sprint": ready,
            "need_revision": len(analyses) - ready
        },
        "details": analyses
    }
    
    return {**state, "final_report_md": "\n".join(md_lines), "final_report_json": json_report}


# ── Gradnja grafa ─────────────────────────────────────────────────
def build_agent():
    graph = StateGraph(AgentState)
    
    graph.add_node("parse_input", parse_input)
    graph.add_node("analyze_invest", analyze_invest)
    graph.add_node("generate_report", generate_report)
    
    graph.set_entry_point("parse_input")
    graph.add_edge("parse_input", "analyze_invest")
    graph.add_conditional_edges("analyze_invest", should_continue)
    graph.add_edge("generate_report", END)
    
    return graph.compile()