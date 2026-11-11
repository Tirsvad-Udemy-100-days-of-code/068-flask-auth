[English](Step-6-Flash-Messages) · [Dansk](Step-6-Flash-Messages-da) · **Bahasa Malaysia**

# Langkah 6: Mesej kilat (flash)

## Apa yang diminta dalam kuliah

Beri maklum balas kepada pengguna dengan mesej flash Flask: apabila e-mel tidak wujud, apabila kata laluan salah, dan apabila seseorang mendaftar dengan e-mel yang sudah wujud.

## Apa yang kami bina

Setiap kes memanggil `flash()` dan mengubah hala semula ke `/login`. Templat log masuk melelar `get_flashed_messages()` dan memaparkan setiap mesej dalam teg `<p>`.

```python
flash("That email does not exist, please try again.")
return redirect(url_for("login"))
```

## Rupanya

![E-mel tidak dikenali](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06a-flash-unknown-email.png)

![Kata laluan salah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06b-flash-wrong-password.png)

![Sudah berdaftar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-06c-flash-already-registered.png)

## Apa yang kami perolehi

- Mesej flash dipaparkan sekali dan hilang apabila dimuat semula.
- Maklum balas yang baik memberitahu pengguna apa yang salah tanpa mendedahkan lebih daripada perlu.
- Mengubah hala selepas mesej memastikan borang bersih.

Langkah sebelumnya: [Sahkan pengguna dengan Flask-Login](Step-5-Authenticate-With-Flask-Login-ms) · Langkah seterusnya: [Hantar status pengesahan ke templat](Step-7-Authentication-Status-In-Templates-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
