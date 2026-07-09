# INVEST Izvestaj — User Story Validator

## US-001
**Originalni tekst:** Kao registrovani korisnik, zelim da se prijavim na sistem koristeci email i lozinku, kako bih mogao da pristupim svom nalogu i sacuvanim podacima.

**Format ispravan:** Da

**Ukupni skor: 7.8/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | OK 8/10 | User story je relativno samostalan, jer korisnik može da se prijavi na sistem koristeci email i lozinku. |
| Negotiable | UPOZORENJE 6/10 | User story nije toliko pregovorno, jer korisnik mora da se prijavi koristeci email i lozinku. |
| Valuable | OK 9/10 | User story ima veliku vrednost, jer korisnik može da pristupi svom nalogu i sacuvanim podacima. |
| Estimable | OK 8/10 | User story je relativno ocjenjivljiv, jer se može proceniti vreme potrebno za implementaciju funkcionalnosti za prijavu korisnika. |
| Small | OK 7/10 | User story nije toliko mala, jer se radi o funkcionalnosti za prijavu korisnika, koja može da bude kompleksna. |
| Testable | OK 9/10 | User story je veoma testabilan, jer se može testirati funkcionalnost za prijavu korisnika koristeći jednostavne testove. |

**Preporuke za poboljsanje:**
- Pregovoriti o detaljima prijave, kao što je zahtev za potvrdnu poruku ili zahtev za reset lozinke.
- Implementirati funkcionalnost za prijavu korisnika koristeći postojeći kod.

---

## US-002
**Originalni tekst:** Sistem treba da radi brze i bude bolji.

**Format ispravan:** Ne

**Ukupni skor: 4.0/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | UPOZORENJE 4/10 | User story nije dovoljno detaljan da bi se mogao razumeo bez dodatnih informacija. |
| Negotiable | OK 8/10 | User story je dovoljno širok da bi se moglo pregovarati o detaljima. |
| Valuable | UPOZORENJE 6/10 | User story nije dovoljno detaljan da bi se mogao razumeo njegovu vrednost. |
| Estimable | LOSE 3/10 | User story nije dovoljno detaljan da bi se mogla proceniti njegova težina. |
| Small | LOSE 2/10 | User story je previše širok da bi se mogao smatrati malim. |
| Testable | LOSE 1/10 | User story nije dovoljno detaljan da bi se moglo razumeo kako će se testirati. |

**Preporuke za poboljsanje:**
- Detaljno opisati user story da bi se mogao razumeo njegov sadržaj.
- Šireći user story da bi se omogućilo više pregovora.
- Detaljno opisati kako će se testirati user story.
- Detaljno opisati njegovu vrednost i težinu.

---

## US-003
**Originalni tekst:** Kao administrator, zelim da vidim sve korisnike, kako bih mogao da upravljam nalozima, ali i da brisem, edituje, suspenduje, resetuje lozinke i generisem izvestaje za sve korisnike u sistemu.

**Format ispravan:** Da

**Ukupni skor: 6.5/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | UPOZORENJE 6/10 | User story nije potpuno nezavisan, jer zahteva da se vidi sve korisnike u sistemu, što može biti problem ako sistem ima velik broj korisnika. |
| Negotiable | OK 8/10 | User story je delimično pregovarljiv, jer administrator može pregovarati o detaljima upravljanja nalozima, ali ne i o osnovnim funkcionalnostima. |
| Valuable | OK 9/10 | User story je vrlo vredan, jer omogućava administratoru da upravlja nalozima, brise, edituje, suspenduje, resetuje lozinke i generiše izveštaje za sve korisnike u sistemu. |
| Estimable | OK 7/10 | User story nije potpuno estimabilan, jer zahteva različite radnje koje su teške za procenu vremena. |
| Small | UPOZORENJE 4/10 | User story nije potpuno mali, jer zahteva kompleksne radnje kao što su upravljanje nalozima, brisanje, editovanje, suspendovanje, resetovanje lozinke i generisanje izveštaja. |
| Testable | UPOZORENJE 5/10 | User story nije potpuno testabilan, jer zahteva kompleksne radnje koje su teške za testiranje. |

**Preporuke za poboljsanje:**
- Podelite user story na manje, jednostavnije taskove koji su lakše za implementiranje i testiranje.
- Dodajte više detalja o funkcionalnostima koje se očekuju od administratora, kako bi se smanjila neizvesnost i lakše bilo moguće proceniti vreme za implementaciju.

---

## Rezime
- Ukupno analiziranih user stories: **3**
- Prosecni skor: **6.1/10**
- Spremne za sprint (skor >= 7): **1**
- Potrebna revizija: **2**