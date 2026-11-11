**English** · [Dansk](Step-4-Hash-And-Salt-With-Werkzeug-da) · [Bahasa Malaysia](Step-4-Hash-And-Salt-With-Werkzeug-ms)

# Step 4: Hash and salt passwords with Werkzeug

## What the lecture asked

Delete the old plain text entry, then hash the password with `generate_password_hash()` using `pbkdf2:sha256` and a `salt_length` of 8 before it is stored.

## What we built

The `register` route now stores the hash. The stored value holds the method, the iteration count, the salt and the hash.

```python
from werkzeug.security import generate_password_hash

hash_and_salted_password = generate_password_hash(
    request.form.get("password"),
    method="pbkdf2:sha256",
    salt_length=8,
)
```

## What it looks like

![The users table holds a hash, not the password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-04-hashed-password-in-db.png)

## What we gained

- Werkzeug hashes and salts in one call.
- The database never holds the real password.
- Two users with the same password get different stored values because the salt differs.

Previous step: [Encryption, hashing and password attacks](Step-3-Encryption-And-Hashing) · Next step: [Authenticate users with Flask-Login](Step-5-Authenticate-With-Flask-Login) · [Back to the overview](Home)
