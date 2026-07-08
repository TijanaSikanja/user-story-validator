import json
from dotenv import load_dotenv
from agent import build_agent

load_dotenv()

# Test stories (hardkodovani)
TEST_INPUT = """Kao registrovani korisnik, zelim da se prijavim na sistem koristeci email i lozinku, kako bih mogao da pristupim svom nalogu i sacuvanim podacima.

Sistem treba da radi brze i bude bolji.

Kao administrator, zelim da vidim sve korisnike, kako bih mogao da upravljam nalozima, ali i da brisem, edituje, suspenduje, resetuje lozinke i generisem izvestaje za sve korisnike u sistemu."""


def main():
    print("=" * 50)
    print("  USER STORY VALIDATOR AI AGENT")
    print("=" * 50)
    print("Izaberite nacin unosa:")
    print("1 - Unesi user stories u terminalu")
    print("2 - Koristi test primere")
    print("=" * 50)
    
    izbor = input("Vas izbor (1 ili 2): ").strip()
    
    if izbor == "1":
        print("\nUnesite user stories (prazna linija izmedju svake).")
        print("Kada zavrsite, unesite 'KRAJ' i pritisnite Enter.")
        print("-" * 50)
        lines = []
        while True:
            line = input()
            if line.strip() == "KRAJ":
                break
            lines.append(line)
        user_input = "\n".join(lines)
        
        if not user_input.strip():
            print("Niste uneli nijednu user story!")
            return
    else:
        print("\nKoriste se test primeri iz SRS dokumenta...")
        user_input = TEST_INPUT
    
    print("\nPokretanje analize...")
    
    agent = build_agent()
    
    result = agent.invoke({
        "raw_input": user_input,
        "stories": [],
        "current_index": 0,
        "analyses": [],
        "final_report_md": None,
        "final_report_json": None
    })
    
    print(result["final_report_md"])
    
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(result["final_report_md"])
    
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(result["final_report_json"], f, indent=2, ensure_ascii=False)
    
    print("\nIzvestaji sacuvani: report.md i report.json")


if __name__ == "__main__":
    main()