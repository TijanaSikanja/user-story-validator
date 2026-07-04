# User Story Validator AI Agent

AI agent za automatsku validaciju korisničkih priča (user stories) prema INVEST kriterijumima.

## Tehnologije
- Python 3.10+
- LangGraph
- LangChain
- Groq API (llama-3.1-8b-instant)
- JIRA (project management)

## Instalacija

1. Kloniraj repozitorijum:
git clone https://github.com/TijanaSikanja/user-story-validator.git
cd user-story-validator

2. Instaliraj zavisnosti:
pip install langgraph langchain langchain-groq python-dotenv

3. Kreiraj .env fajl:
GROQ_API_KEY=tvoj_api_kljuc

4. Pokreni agenta:
python main.py

## Primer korišćenja
Agent prima user stories kao tekstualni ulaz i generiše izveštaj sa INVEST ocenama i preporukama.

## Izlaz
- report.md - Markdown izveštaj
- report.json - JSON izveštaj

## Ograničenja
- Zavisi od Groq API dostupnosti
- Rezultati mogu varirati zbog probabilističke prirode LLM-a
- Ne čita direktno iz JIRA API-ja