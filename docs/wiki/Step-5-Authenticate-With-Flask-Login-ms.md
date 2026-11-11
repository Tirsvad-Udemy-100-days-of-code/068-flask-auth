[English](Step-5-Authenticate-With-Flask-Login) · [Dansk](Step-5-Authenticate-With-Flask-Login-da) · **Bahasa Malaysia**

# Langkah 5: Sahkan pengguna dengan Flask-Login

## Apa yang diminta dalam kuliah

Hanya pengguna yang log masuk boleh melihat `/secrets` dan memuat turun fail. Konfigurasikan Flask-Login, log masuk pengguna apabila mendaftar, lindungi `/secrets` dan `/download`, dan tulis laluan `/login` dan `/logout`.

## Apa yang kami bina

`LoginManager` dengan panggilan balik `user_loader`, `User` yang menggunakan `UserMixin`, `login_user()` selepas daftar dan log masuk, `@login_required` pada laluan yang dilindungi, `check_password_hash()` untuk mengesahkan kata laluan dan `logout_user()` untuk `/logout`.

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

## Rupanya

![/secrets tanpa log masuk ditolak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05a-secrets-requires-login.png)

![Borang log masuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05b-login-form.png)

![Selepas log masuk berjaya](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05c-login-success.png)

## Apa yang kami perolehi

- Flask-Login mengesan siapa yang log masuk antara permintaan.
- `user_loader` menukar id pengguna yang disimpan kepada `User`.
- `@login_required` melindungi laluan dengan satu baris.
- `check_password_hash()` membandingkan kata laluan yang ditaip dengan cincang yang disimpan tanpa menyahkodnya.

Langkah sebelumnya: [Cincang dan garamkan kata laluan dengan Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-ms) · Langkah seterusnya: [Mesej kilat (flash)](Step-6-Flash-Messages-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
