[English](Step-5-Authenticate-With-Flask-Login) · **Dansk** · [Bahasa Malaysia](Step-5-Authenticate-With-Flask-Login-ms)

# Trin 5: Godkend brugere med Flask-Login

## Hvad lektionen bad om

Kun loggede brugere må se `/secrets` og hente filen. Konfigurer Flask-Login, log brugeren ind ved registrering, beskyt `/secrets` og `/download`, og skriv ruterne `/login` og `/logout`.

## Hvad vi byggede

En `LoginManager` med et `user_loader`-callback, en `User` der bruger `UserMixin`, `login_user()` efter registrering og login, `@login_required` på de beskyttede ruter, `check_password_hash()` til at kontrollere adgangskoden og `logout_user()` til `/logout`.

```python
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)
```

I dette repository accepterer `/logout` kun POST. Menupunktet "Log Out" er en lille formular med CSRF-token, og `GET /logout` giver 405. Det afviger fra lektionen, hvor logout er et almindeligt link, fordi en GET, der ændrer tilstand, kan udløses fra et andet site.

## Sådan ser det ud

![/secrets uden login afvises](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05a-secrets-requires-login.png)

![Login-formularen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05b-login-form.png)

![Efter et vellykket login](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05c-login-success.png)

## Hvad vi fik ud af det

- Flask-Login husker, hvem der er logget ind mellem forespørgsler.
- En `user_loader` omsætter det gemte bruger-id til en `User`.
- `@login_required` beskytter en rute med én linje.
- `check_password_hash()` sammenligner en indtastet adgangskode med den gemte hash uden nogensinde at afkode den.

Forrige trin: [Hash og salt adgangskoder med Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-da) · Næste trin: [Flash-beskeder](Step-6-Flash-Messages-da) · [Tilbage til oversigten](Home-da)
