**English** · [Dansk](Step-6-Flash-Messages-da) · [Bahasa Malaysia](Step-6-Flash-Messages-ms)

# Step 6: Flash messages

## What the lecture asked

Give the user feedback with Flask flash messages: when the email does not exist, when the password is wrong, and when someone registers with an email that already exists.

## What we built

Each case calls `flash()` and redirects back to `/login`. The login template loops over `get_flashed_messages()` and shows each one in a `<p>` tag.

```python
flash("That email does not exist, please try again.")
return redirect(url_for("login"))
```

## What it looks like

![Unknown email](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06a-flash-unknown-email.png)

![Wrong password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06b-flash-wrong-password.png)

![Already registered](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06c-flash-already-registered.png)

## What we gained

- A flash message is shown once and disappears on reload.
- Good feedback tells users what went wrong without leaking more than needed.
- Redirecting after the message keeps the form clean.

Previous step: [Authenticate users with Flask-Login](Step-5-Authenticate-With-Flask-Login) · Next step: [Pass the authentication status to templates](Step-7-Authentication-Status-In-Templates) · [Back to the overview](Home)
