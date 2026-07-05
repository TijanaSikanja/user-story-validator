import json
from dotenv import load_dotenv
from agent import build_agent

load_dotenv()

# ── Test stories iz SRS sekcije 8.2 ──────────────────────────────
TEST_INPUT = """Kao registrovani korisnik, zelim da se prijavim na sistem koristeci email i lozinku, kako bih mogao da pristupim svom nalogu i sacuvanim podacima.

Sistem treba da radi brze i bude bolji.

Kao administrator, zelim da vidim sve korisnike, kako bih mogao da upravljam nalozima, ali i da brisem, edituje, suspenduje, resetuje lozinke i generisem izvestaje za sve korisnike u sistemu."""


def main():
    print("Pokretanje User Story Validator AI Agenta...")
    print("=" * 50)
    
    agent = build_agent()
    
    result = agent.invoke({
        "raw_input": TEST_INPUT,
        "stories": [],
        "current_index": 0,
        "analyses": [],
        "final_report_md": None,
        "final_report_json": None
    })
    
    # Prikazi Markdown izvestaj
    print(result["final_report_md"])
    
    # Sacuvaj izlaze
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(result["final_report_md"])
    
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(result["final_report_json"], f, indent=2, ensure_ascii=False)
    
    print("\nIzvestaji sacuvani: report.md i report.json")


if __name__ == "__main__":
    main()