[English](Step-7-Authentication-Status-In-Templates) · [Dansk](Step-7-Authentication-Status-In-Templates-da) · **Bahasa Malaysia**

# Langkah 7: Hantar status pengesahan ke templat

## Apa yang diminta dalam kuliah

Sembunyikan butang dan pautan navigasi Login dan Register untuk pengguna yang log masuk, dan tunjukkan "(you are already logged in)" pada halaman utama.

## Apa yang kami bina

Setiap laluan menghantar `logged_in=current_user.is_authenticated`. `base.html` dan `index.html` membalut butang dan pautan dalam `{% if not logged_in: %}` dan menunjukkan mesej dalam cabang `else`.

```python
return render_template("index.html", logged_in=current_user.is_authenticated)
```

## Rupanya

![Halaman utama, log keluar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07a-home-logged-out.png)

![Halaman utama, log masuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-07b-home-logged-in.png)

## Apa yang kami perolehi

- Templat boleh bertindak balas terhadap siapa yang log masuk.
- Templat susun atur `base.html` menukar navigasi untuk semua halaman serentak.
- Menyembunyikan pautan ialah pilihan kebolehgunaan; laluan itu sendiri masih mesti dilindungi.

Langkah sebelumnya: [Mesej kilat (flash)](Step-6-Flash-Messages-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
