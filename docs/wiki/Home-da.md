[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Flask Auth: Dag 68, autentificering

Denne wiki forklarer, hvad hvert lektionstrin på dag 68 af Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp" lærte os. Lektionen bygger et Flask-site, hvor folk registrerer sig, logger ind, ser en hemmelig side og henter en fil. Skærmbillederne stammer fra lektionens slutprojekt, kørt i en Docker-container med testdata.

## Kør det

Dette repository indeholder kun dokumentation. For at følge med skal du oprette en lokal `.venv`, opgradere pip og installere lektionens pakker (hele vejledningen står i [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install Flask==3.0.0 Werkzeug==3.0.0 Flask_Login==0.6.3 flask_sqlalchemy==3.1.1 "SQLAlchemy>=2.0.36"
```

## De syv trin

1. [Trin 1: Registrer nye brugere og hils på dem](Step-1-Register-And-Greet-da)
2. [Trin 2: Download en fil](Step-2-Download-A-File-da)
3. [Trin 3: Kryptering, hashing og adgangskodeangreb](Step-3-Encryption-And-Hashing-da)
4. [Trin 4: Hash og salt adgangskoder med Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-da)
5. [Trin 5: Godkend brugere med Flask-Login](Step-5-Authenticate-With-Flask-Login-da)
6. [Trin 6: Flash-beskeder](Step-6-Flash-Messages-da)
7. [Trin 7: Send godkendelsesstatus til skabeloner](Step-7-Authentication-Status-In-Templates-da)

## Hvad vi fik ud af det samlet set

- At registrere brugere og hilse på dem ved navn.
- At levere en fil med `send_from_directory()`.
- Hvorfor adgangskoder hashes og saltes, og hvordan Werkzeug gør det.
- Flask-Login til sessioner, beskyttede ruter og logout.
- Flash-beskeder til feedback og skabelonvariabler til login-status.
