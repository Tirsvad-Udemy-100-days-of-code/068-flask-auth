[English](Step-4-Hash-And-Salt-With-Werkzeug) · [Dansk](Step-4-Hash-And-Salt-With-Werkzeug-da) · **Bahasa Malaysia**

# Langkah 4: Cincang dan garamkan kata laluan dengan Werkzeug

## Apa yang diminta dalam kuliah

Padam entri teks biasa yang lama, kemudian cincang kata laluan dengan `generate_password_hash()` menggunakan `pbkdf2:sha256` dan `salt_length` 8 sebelum disimpan.

## Apa yang kami bina

Laluan `register` kini menyimpan cincang. Nilai yang disimpan mengandungi kaedah, bilangan lelaran, garam dan cincang.

```python
from werkzeug.security import generate_password_hash

hash_and_salted_password = generate_password_hash(
    request.form.get("password"),
    method="pbkdf2:sha256",
    salt_length=8,
)
```

## Rupanya

![Jadual users menyimpan cincang, bukan kata laluan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-04-hashed-password-in-db.png)

## Apa yang kami perolehi

- Werkzeug mencincang dan menggaram dalam satu panggilan.
- Pangkalan data tidak pernah menyimpan kata laluan sebenar.
- Dua pengguna dengan kata laluan sama mendapat nilai simpanan berbeza kerana garam berbeza.

Langkah sebelumnya: [Penyulitan, pencincangan dan serangan kata laluan](Step-3-Encryption-And-Hashing-ms) · Langkah seterusnya: [Sahkan pengguna dengan Flask-Login](Step-5-Authenticate-With-Flask-Login-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
