[English](Step-4-Hash-And-Salt-With-Werkzeug) · **Dansk** · [Bahasa Malaysia](Step-4-Hash-And-Salt-With-Werkzeug-ms)

# Trin 4: Hash og salt adgangskoder med Werkzeug

## Hvad lektionen bad om

Slet den gamle klartekstpost, og hash derefter adgangskoden med `generate_password_hash()` med `pbkdf2:sha256` og `salt_length` på 8, før den gemmes.

## Hvad vi byggede

Ruten `register` gemmer nu hashen. Den gemte værdi indeholder metoden, antal iterationer, saltet og hashen.

```python
from werkzeug.security import generate_password_hash

hash_and_salted_password = generate_password_hash(
    request.form.get("password"),
    method="pbkdf2:sha256",
    salt_length=8,
)
```

## Sådan ser det ud

![Tabellen users indeholder en hash, ikke adgangskoden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-04-hashed-password-in-db.png)

## Hvad vi fik ud af det

- Werkzeug hasher og salter i ét kald.
- Databasen indeholder aldrig den rigtige adgangskode.
- To brugere med samme adgangskode får forskellige gemte værdier, fordi saltet er forskelligt.

Forrige trin: [Kryptering, hashing og adgangskodeangreb](Step-3-Encryption-And-Hashing-da) · Næste trin: [Godkend brugere med Flask-Login](Step-5-Authenticate-With-Flask-Login-da) · [Tilbage til oversigten](Home-da)
