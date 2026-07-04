# INVEST Izvestaj — User Story Validator

## US-001
**Originalni tekst:** Kao registrovani korisnik, zelim da se prijavim na sistem koristeci email i lozinku, kako bih mogao da pristupim svom nalogu i sacuvanim podacima.

**Format ispravan:** Da

**Ukupni skor: 7.8/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | OK 8/10 | User story je relativno samostalan, jer korisnik može da se prijavi na sistem koristeci email i lozinku. |
| Negotiable | UPOZORENJE 6/10 | User story nije previše pregovarljiv, jer korisnik mora da se prijavi koristeci email i lozinku. |
| Valuable | OK 9/10 | User story ima visoku vrednost, jer korisnik može da pristupi svom nalogu i sacuvanim podacima. |
| Estimable | OK 8/10 | User story je relativno ocjenjiv, jer se vjerovatno koristi postojeći sistem za prijavu. |
| Small | OK 7/10 | User story nije previše mala, jer se vjerovatno koriste postojeće funkcionalnosti. |
| Testable | OK 9/10 | User story je relativno testabilan, jer se vjerovatno koriste postojeće funkcionalnosti za prijavu. |

**Preporuke za poboljsanje:**
- Pregovarati o detaljima prijave, kao što je zahtev za potvrdnu poruku.
- Izvršiti testove za prijavu da bi se obezbedila njena testabilnost.

---

## US-002
**Originalni tekst:** Sistem treba da radi brze i bude bolji.

**Format ispravan:** Ne

**Ukupni skor: 4.0/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | UPOZORENJE 6/10 | User story nije dovoljno detaljan da bi se mogao razumeo kao samostalan zadatak. |
| Negotiable | OK 8/10 | User story je dovoljno širok da bi se moglo pregovarati o detaljima. |
| Valuable | UPOZORENJE 4/10 | User story nije dovoljno detaljan da bi se mogao razumeo njegovu vrednost. |
| Estimable | LOSE 3/10 | User story nije dovoljno detaljan da bi se mogao ocjeniti njegov vremenski zahtjev. |
| Small | LOSE 2/10 | User story nije dovoljno detaljan da bi se mogao razumeo njegovu veličinu. |
| Testable | LOSE 1/10 | User story nije dovoljno detaljan da bi se mogao razumeo njegovu testabilnost. |

**Preporuke za poboljsanje:**
- Dodajte detaljnije informacije o sistem koji treba da radi brze i bude bolji.
- Definisite specifične kriterijume za ocjenjivanje vrednosti sistema.
- Definisite specifične kriterijume za ocjenjivanje vremenskog zahtjeva sistema.
- Definisite specifične kriterijume za ocjenjivanje testabilnosti sistema.

---

## US-003
**Originalni tekst:** Kao administrator, zelim da vidim sve korisnike, kako bih mogao da upravljam nalozima, ali i da brisem, edituje, suspenduje, resetuje lozinke i generisem izvestaje za sve korisnike u sistemu.

**Format ispravan:** Da

**Ukupni skor: 6.5/10**

| Kriterijum | Ocena | Obrazlozenje |
|---|---|---|
| Independent | UPOZORENJE 6/10 | User story nije potpuno nezavisan, jer zahteva da se vidi sve korisnike u sistemu, što može da bude problem ako sistem ima velik broj korisnika. |
| Negotiable | OK 8/10 | User story je delimično pregovarljiv, jer administrator može da pregovara o detaljima upravljanja nalozima, ali ne i o osnovnim funkcionalnostima. |
| Valuable | OK 9/10 | User story je vrlo vredan, jer omogućava administratoru da upravlja nalozima, brise, edituje, suspenduje, resetuje lozinke i generiše izveštaje za sve korisnike u sistemu. |
| Estimable | OK 7/10 | User story nije potpuno estimabilan, jer zahteva različite radnje (upravljanje nalozima, brisanje, editovanje, suspendovanje, resetovanje lozinke, generisanje izveštaja) koje su teške za procenu. |
| Small | UPOZORENJE 4/10 | User story nije potpuno mali, jer zahteva kompleksne radnje koje mogu da zauzmu dugo vreme za implementaciju. |
| Testable | UPOZORENJE 5/10 | User story nije potpuno testabilan, jer zahteva različite radnje koje su teške za testiranje, posebno generisanje izveštaja koji može da sadrži kompleksne podatke. |

**Preporuke za poboljsanje:**
- Podelite user story na manje, jednostavnije taskove koji će biti lakše za implementaciju i testiranje.
- Dodajte više detalja o funkcionalnostima koje administrator treba da ima, kako bi se smanjila nepoznanica i lakše bilo da se implementacija i testiranje provedu.

---

## Rezime
- Ukupno analiziranih user stories: **3**
- Prosecni skor: **6.1/10**
- Spremne za sprint (skor >= 7): **1**
- Potrebna revizija: **2**