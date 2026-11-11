[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Flask Auth: Dag 68, autentificering

Denne wiki forklarer, hvad hvert lektionstrin på dag 68 af Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp" lærte os. Lektionen bygger et Flask-site, hvor folk registrerer sig, logger ind, ser en hemmelig side og henter en fil. Skærmbillederne stammer fra lektionens slutprojekt, kørt i en Docker-container med testdata.

## Kør det

Dette repository indeholder en fungerende Flask-applikation, der implementerer lektionens trin, med pytest-tests. For at køre den skal du oprette en lokal `.venv`, opgradere pip og installere projektet (hele vejledningen står i [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
# SECRET_KEY skal sættes først (se README)
python -m flask_auth     # serverer http://127.0.0.1:5000
python -m pytest         # kører testene
```

Skærmbillederne i trinene stammer fra lektionens eget slutprojekt; koden i dette repository følger de samme trin.

## De syv trin

1. [Trin 1: Registrer nye brugere og hils på dem](Step-1-Register-And-Greet-da)
2. [Trin 2: Download en fil](Step-2-Download-A-File-da)
3. [Trin 3: Kryptering, hashing og adgangskodeangreb](Step-3-Encryption-And-Hashing-da)
4. [Trin 4: Hash og salt adgangskoder med Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-da)
5. [Trin 5: Godkend brugere med Flask-Login](Step-5-Authenticate-With-Flask-Login-da)
6. [Trin 6: Flash-beskeder](Step-6-Flash-Messages-da)
7. [Trin 7: Send godkendelsesstatus til skabeloner](Step-7-Authentication-Status-In-Templates-da)

## Hvor koden er

| Trin | Kode i `src/flask_auth/` |
| --- | --- |
| 1 Registrer og hils | `presentation/routes.py` (`register`, `secrets`), `application/register_user.py`, `domain/user.py` |
| 2 Hent en fil | `presentation/routes.py` (`download`) |
| 3, 4 Hashing og salt | `infrastructure/password_hasher.py`, `constants.py` |
| 5 Flask-Login | `presentation/login_adapter.py`, `application/authenticate_user.py`, `presentation/routes.py` (`login`, `logout`) |
| 6 Flash-beskeder | `presentation/routes.py`, `presentation/templates/base.html`, `constants.py` |
| 7 Loginstatus | `presentation/templates/base.html`, `presentation/templates/index.html` |

Testene ligger i `tests/unit`, `tests/integration` og `tests/e2e`.

## Hvad vi fik ud af det samlet set

- At registrere brugere og hilse på dem ved navn.
- At levere en fil med `send_from_directory()`.
- Hvorfor adgangskoder hashes og saltes, og hvordan Werkzeug gør det.
- Flask-Login til sessioner, beskyttede ruter og logout.
- Flash-beskeder til feedback og skabelonvariabler til login-status.
