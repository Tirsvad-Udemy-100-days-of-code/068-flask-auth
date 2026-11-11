[English](Step-6-Flash-Messages) · **Dansk** · [Bahasa Malaysia](Step-6-Flash-Messages-ms)

# Trin 6: Flash-beskeder

## Hvad lektionen bad om

Giv brugeren feedback med Flasks flash-beskeder: når e-mailen ikke findes, når adgangskoden er forkert, og når nogen registrerer sig med en e-mail, der allerede findes.

## Hvad vi byggede

Hvert tilfælde kalder `flash()` og omdirigerer tilbage til `/login`. Login-skabelonen gennemløber `get_flashed_messages()` og viser hver besked i et `<p>`-tag.

```python
flash("That email does not exist, please try again.")
return redirect(url_for("login"))
```

## Sådan ser det ud

![Ukendt e-mail](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06a-flash-unknown-email.png)

![Forkert adgangskode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06b-flash-wrong-password.png)

![Allerede registreret](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06c-flash-already-registered.png)

## Hvad vi fik ud af det

- En flash-besked vises én gang og forsvinder ved genindlæsning.
- God feedback fortæller brugeren, hvad der gik galt, uden at afsløre mere end nødvendigt.
- Omdirigering efter beskeden holder formularen ren.

Forrige trin: [Godkend brugere med Flask-Login](Step-5-Authenticate-With-Flask-Login-da) · Næste trin: [Send godkendelsesstatus til skabeloner](Step-7-Authentication-Status-In-Templates-da) · [Tilbage til oversigten](Home-da)
