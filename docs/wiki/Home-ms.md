[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Flask Auth: Hari 68, pengesahan

Wiki ini menerangkan apa yang diajar oleh setiap langkah kuliah Hari 68 kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp". Kuliah ini membina tapak Flask tempat orang mendaftar, log masuk, melihat halaman rahsia dan memuat turun fail. Tangkapan skrin datang daripada projek akhir kuliah, dijalankan dalam bekas Docker dengan data ujian.

## Jalankannya

Repositori ini hanya mengandungi dokumentasi. Untuk mengikuti, cipta `.venv` setempat, naik taraf pip dan pasang pakej kuliah (arahan penuh ada dalam [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install Flask==3.0.0 Werkzeug==3.0.0 Flask_Login==0.6.3 flask_sqlalchemy==3.1.1 "SQLAlchemy>=2.0.36"
```

## Tujuh langkah

1. [Langkah 1: Daftar pengguna baharu dan sambut mereka](Step-1-Register-And-Greet-ms)
2. [Langkah 2: Muat turun fail](Step-2-Download-A-File-ms)
3. [Langkah 3: Penyulitan, pencincangan dan serangan kata laluan](Step-3-Encryption-And-Hashing-ms)
4. [Langkah 4: Cincang dan garamkan kata laluan dengan Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-ms)
5. [Langkah 5: Sahkan pengguna dengan Flask-Login](Step-5-Authenticate-With-Flask-Login-ms)
6. [Langkah 6: Mesej kilat (flash)](Step-6-Flash-Messages-ms)
7. [Langkah 7: Hantar status pengesahan ke templat](Step-7-Authentication-Status-In-Templates-ms)

## Apa yang kami perolehi secara keseluruhan

- Mendaftar pengguna dan menyambut mereka dengan nama.
- Menyajikan fail dengan `send_from_directory()`.
- Mengapa kata laluan dicincang dan digaram, dan bagaimana Werkzeug melakukannya.
- Flask-Login untuk sesi, laluan dilindungi dan log keluar.
- Mesej flash untuk maklum balas dan pemboleh ubah templat untuk status log masuk.
