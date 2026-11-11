**English** · [Dansk](Step-1-Register-And-Greet-da) · [Bahasa Malaysia](Step-1-Register-And-Greet-ms)

# Step 1: Register new users and greet them

## What the lecture asked

Take the name, email and password from the register form, create a new `User` and save it in `users.db`. Then send the user straight to `secrets.html`, where the `h1` says hello with the name they typed.

## What we built

The `register` route reads `request.form`, builds a `User`, adds it to the session and commits. After that it redirects to `secrets`, which passes `current_user.name` to the template.

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

## What it looks like

![The register form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01a-register-form.png)

![The secrets page greets the user](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01b-secrets-greeting.png)

## What we gained

- A form `POST` becomes a database row through a model object.
- `request.form.get()` reads what the user typed.
- A redirect after saving sends the user on to the next page.
- In this first version the password is stored as plain text, which step 4 fixes.

Next step: [Download a file](Step-2-Download-A-File) · [Back to the overview](Home)
