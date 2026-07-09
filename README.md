<div align="center">

# 🎯 User Story Validator AI Agent

**AI agent koji automatizuje validaciju korisničkih priča prema INVEST kriterijumima**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-workflow-1C3C3C)
![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C)
![Groq](https://img.shields.io/badge/LLM-Groq%20llama--3.1--8b-orange)
![License](https://img.shields.io/badge/status-student%20project-lightgrey)

</div>

---

Backlog stavke koje ulaze u sprint su često nejasno formulisane, previše obimne ili im nedostaju kriterijumi prihvatanja — a ručna provera od strane Project Managera ili Product Owner-a je spora i subjektivna.

**User Story Validator** rešava taj problem: prima user stories, analizira ih prema šest **INVEST kriterijuma** uz pomoć LLM-a, i vraća strukturiran izveštaj sa ocenama, obrazloženjima i konkretnim preporukama — pre nego što priča uopšte uđe u sprint.

---

## 📑 Sadržaj

- [✨ Funkcionalnosti](#-funkcionalnosti)
- [🧠 Arhitektura i workflow](#-arhitektura-i-workflow)
- [🛠️ Tehnologije](#️-tehnologije)
- [⚙️ Instalacija](#️-instalacija)
- [▶️ Pokretanje](#️-pokretanje)
- [📄 Primer izlaza](#-primer-izlaza)
- [📁 Struktura projekta](#-struktura-projekta)
- [🔗 JIRA i GitHub](#-jira-i-github)
- [⚠️ Ograničenja](#️-ograničenja)
- [🚀 Mogućnosti za unapređenje](#-mogućnosti-za-unapređenje)
- [👥 Autori](#-autori)

---

## ✨ Funkcionalnosti

- 📥 Prihvata jednu ili više user stories — ručnim unosom u terminalu ili kroz unapred definisane test primere
- ✂️ Automatski parsira ulaz i razdvaja pojedinačne user stories
- ✅ Proverava da li svaka priča prati standardni format *„Kao ..., želim ..., kako bih ..."*
- 🧩 Analizira svaku priču prema **6 INVEST kriterijuma**: Independent, Negotiable, Valuable, Estimable, Small, Testable
- 🔢 Dodeljuje ocenu (0–10) i tekstualno obrazloženje za svaki kriterijum
- 💡 Generiše konkretne, primenljive preporuke za poboljšanje
- 📊 Računa ukupan skor i sumarnu statistiku (koliko je priča spremno za sprint)
- 📤 Izvozi izveštaj u **Markdown** i **JSON** formatu
- 🛡️ Gracefully obrađuje greške u LLM odgovoru bez rušenja programa

## 🧠 Arhitektura i workflow

Agent je implementiran kao **LangGraph graf stanja** sa tri čvora i uslovnom granom koja realizuje petlju po svim unetim user stories:

```
                    ┌─────────────────────────┐
                    │   Ulaz: tekst sa user    │
                    │        stories           │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      parse_input         │
                    │  deli tekst na pojedi-   │
                    │     načne user stories    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
              ┌────►│     analyze_invest        │
              │     │  poziva Groq LLM, ocenju- │
              │     │  je 6 INVEST kriterijuma   │
              │     └────────────┬─────────────┘
              │                  │
              │           ima još priča?
              └──────── da ──────┴────── ne
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     generate_report       │
                    │  formatira Markdown +     │
                    │        JSON izveštaj       │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Izlaz: report.md +       │
                    │       report.json          │
                    └─────────────────────────┘
```

## 🛠️ Tehnologije

| Komponenta | Tehnologija |
|---|---|
| 🐍 Jezik | Python 3.10+ |
| 🔀 Orkestracija workflow-a | LangGraph |
| 🔌 LLM konekcija | LangChain (`langchain-groq`) |
| 🤖 LLM model | Groq — `llama-3.1-8b-instant` |
| 🔐 Konfiguracija | `python-dotenv` (.env fajl) |
| 📋 Upravljanje projektom | JIRA (Scrum board) |
| 🌿 Verzionisanje | Git / GitHub, povezano sa JIRA-om |

## ⚙️ Instalacija

**1. Klonirajte repozitorijum:**
```bash
git clone https://github.com/TijanaSikanja/user-story-validator.git
cd user-story-validator
```

**2. Instalirajte zavisnosti:**
```bash
pip install -r requirements.txt
```

**3. Kreirajte `.env` fajl** u korenu projekta:
```env
GROQ_API_KEY=tvoj_api_kljuc
```
> 💡 Besplatan API ključ dobijate registracijom na [console.groq.com](https://console.groq.com)

## ▶️ Pokretanje

```bash
python main.py
```

Agent nudi dve opcije unosa:

| Opcija | Opis |
|:---:|---|
| **1** | ✍️ **Unesi user stories u terminalu** — ručni unos, priče odvojene praznim redom, unos se završava sa `KRAJ` |
| **2** | 🧪 **Koristi test primere** — agent koristi tri unapred definisane test user stories |

Nezavisno od izabrane opcije, agent ispisuje kompletan INVEST izveštaj u konzoli i čuva ga kao `report.md` i `report.json`.

## 📄 Primer izlaza

```
## US-001
Originalni tekst: Kao registrovani korisnik, zelim da se prijavim na sistem
koristeci email i lozinku, kako bih mogao da pristupim svom nalogu.

Format ispravan: Da
Ukupni skor: 7.8/10

┌─────────────┬───────┬───────────────────────────────────────────┐
│ Kriterijum  │ Ocena │ Obrazloženje                               │
├─────────────┼───────┼───────────────────────────────────────────┤
│ Independent │  8/10 │ User story je relativno samostalan...       │
│ Negotiable  │  6/10 │ User story nije toliko pregovorno...         │
│ Valuable    │  9/10 │ User story ima veliku vrednost...             │
│ Estimable   │  8/10 │ User story je relativno ocenjiv...             │
│ Small       │  7/10 │ User story nije toliko mala...                  │
│ Testable    │  9/10 │ User story je veoma testabilan...                │
└─────────────┴───────┴───────────────────────────────────────────┘

Preporuke:
 • Pregovoriti o detaljima prijave...
 • Implementirati funkcionalnost koristeći postojeći kod...
```

Rezime nakon obrade svih priča *(stvarni rezultat, test pokretanje sa 3 primera)*:

```
📊 Ukupno analiziranih user stories: 3
📈 Prosečan skor: 6.1/10
✅ Spremne za sprint (skor >= 7): 1
🔁 Potrebna revizija: 2
```

## 📁 Struktura projekta

```
user-story-validator/
├── 🚀 main.py            Ulazna tačka — meni, pokretanje agenta, čuvanje izveštaja
├── 🧠 agent.py            LangGraph workflow: parsiranje, INVEST analiza, izveštaj
├── 📦 models.py           AgentState — stanje koje se prosleđuje kroz graf
├── ✏️  prompts.py          Strukturiran prompt za INVEST analizu
├── 📋 requirements.txt    Python zavisnosti
├── 🔐 .env                GROQ_API_KEY (nije u repozitorijumu)
├── 📝 report.md           Poslednji generisani Markdown izveštaj
└── 🗂️  report.json         Poslednji generisani JSON izveštaj
```

## 🔗 JIRA i GitHub

Projekat je organizovan u JIRA-i kroz epike, story-je, taskove i subtaskove (Scrum board, projekat `SCRUM`), sa dodeljenim zaduženjima i prioritetima.

GitHub repozitorijum je povezan sa JIRA projektom preko zvanične **GitHub for Jira** integracije — commit poruke referenciraju odgovarajući issue key:

```
[SCRUM-13] Promena LLM na Groq API - llama-3.1-8b-instant
[SCRUM-16] Dodati izvestaji testiranja - report.md i report.json
[SCRUM-15] Azuriran README sa uputstvom za pokretanje
```

Ovi commit-ovi se automatski prikazuju u razvojnoj istoriji odgovarajućeg JIRA taska.

## ⚠️ Ograničenja

- 🚫 Agent trenutno ne učitava user stories direktno iz JIRA API-ja niti iz fajla — podržan je ručni unos u terminalu ili unapred definisani test primeri
- 🎲 Ocene mogu blago varirati između pokretanja zbog probabilističke prirode LLM-a (ublaženo niskom temperaturom modela, 0.1)
- 🧠 Agent ne čuva istoriju prethodnih analiza — svako pokretanje je nezavisno
- 🌐 Zavisi od dostupnosti Groq API servisa
- 🧪 Nema automatizovanih (unit/integration) testova — testiranje je trenutno manuelno

## 🚀 Mogućnosti za unapređenje

- [ ] Učitavanje user stories direktno iz fajla ili preko CLI argumenata
- [ ] Integracija sa JIRA API-jem za automatsko preuzimanje backlog stavki
- [ ] Podrška za dodatne LLM provajdere (Claude, GPT-4) uz mogućnost odabira
- [ ] Web ili grafički interfejs
- [ ] Praćenje istorije analiza kroz vreme
- [ ] Dodavanje automatizovanih testova

## 👥 Autori

<div align="center">

**Nađa Mladenović** · **Tijana Šikanja**



</div>
