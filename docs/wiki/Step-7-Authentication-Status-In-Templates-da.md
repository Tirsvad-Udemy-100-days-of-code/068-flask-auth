[English](Step-7-Authentication-Status-In-Templates) · **Dansk** · [Bahasa Malaysia](Step-7-Authentication-Status-In-Templates-ms)

# Trin 7: Send godkendelsesstatus til skabeloner

## Hvad lektionen bad om

Skjul knapperne og navigationslinkene Login og Register for loggede brugere, og vis "(you are already logged in)" på forsiden.

## Hvad vi byggede

Hver rute sender `logged_in=current_user.is_authenticated`. `base.html` og `index.html` omslutter knapper og links i `{% if not logged_in: %}` og viser beskeden i `else`-grenen.

```python
return render_template("index.html", logged_in=current_user.is_authenticated)
```

## Sådan ser det ud

![Forsiden, logget ud](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07a-home-logged-out.png)

![Forsiden, logget ind](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07b-home-logged-in.png)

## Hvad vi fik ud af det

- Skabeloner kan reagere på, hvem der er logget ind.
- Layoutskabelonen `base.html` ændrer navigationen på alle sider på én gang.
- At skjule et link er et brugervenlighedsvalg; selve ruten skal stadig beskyttes.

Forrige trin: [Flash-beskeder](Step-6-Flash-Messages-da) · [Tilbage til oversigten](Home-da)
