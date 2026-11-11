[English](Step-1-Register-And-Greet) · **Dansk** · [Bahasa Malaysia](Step-1-Register-And-Greet-ms)

# Trin 1: Registrer nye brugere og hils på dem

## Hvad lektionen bad om

Tag navn, e-mail og adgangskode fra registreringsformularen, opret en ny `User` og gem den i `users.db`. Send derefter brugeren direkte til `secrets.html`, hvor `h1` hilser med det navn, de skrev.

## Hvad vi byggede

Ruten `register` læser `request.form`, bygger en `User`, tilføjer den til sessionen og committer. Derefter omdirigerer den til `secrets`, som sender `current_user.name` videre til skabelonen.

```python
new_user = User(
    email=request.form.get("email"),
    password=request.form.get("password"),
    name=request.form.get("name"),
)
db.session.add(new_user)
db.session.commit()
return redirect(url_for("secrets"))
```

## Sådan ser det ud

![Registreringsformularen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01a-register-form.png)

![Hemmelighedssiden hilser på brugeren](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01b-secrets-greeting.png)

## Hvad vi fik ud af det

- En formular-`POST` bliver til en databaserække via et modelobjekt.
- `request.form.get()` læser det, brugeren skrev.
- En omdirigering efter gem sender brugeren videre til næste side.
- I denne første version gemmes adgangskoden som klartekst, hvilket trin 4 retter.

Næste trin: [Download en fil](Step-2-Download-A-File-da) · [Tilbage til oversigten](Home-da)
