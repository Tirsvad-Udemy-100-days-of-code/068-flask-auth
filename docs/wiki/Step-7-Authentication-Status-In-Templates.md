**English** · [Dansk](Step-7-Authentication-Status-In-Templates-da) · [Bahasa Malaysia](Step-7-Authentication-Status-In-Templates-ms)

# Step 7: Pass the authentication status to templates

## What the lecture asked

Hide the Login and Register buttons and navigation links for logged-in users, and show "(you are already logged in)" on the home page.

## What we built

Every route passes `logged_in=current_user.is_authenticated`. `base.html` and `index.html` wrap the buttons and links in `{% if not logged_in: %}` and show the message in the `else` branch.

```python
return render_template("index.html", logged_in=current_user.is_authenticated)
```

## What it looks like

![Home page, logged out](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07a-home-logged-out.png)

![Home page, logged in](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07b-home-logged-in.png)

## What we gained

- Templates can react to who is logged in.
- The layout template `base.html` changes the navigation for every page at once.
- Hiding a link is a usability choice; the route itself must still be protected.

Previous step: [Flash messages](Step-6-Flash-Messages) · [Back to the overview](Home)
