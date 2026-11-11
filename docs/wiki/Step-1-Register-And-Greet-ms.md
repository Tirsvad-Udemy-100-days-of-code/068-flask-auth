[English](Step-1-Register-And-Greet) · [Dansk](Step-1-Register-And-Greet-da) · **Bahasa Malaysia**

# Langkah 1: Daftar pengguna baharu dan sambut mereka

## Apa yang diminta dalam kuliah

Ambil nama, e-mel dan kata laluan daripada borang pendaftaran, cipta `User` baharu dan simpan dalam `users.db`. Kemudian hantar pengguna terus ke `secrets.html`, tempat `h1` menyapa dengan nama yang ditaip.

## Apa yang kami bina

Laluan `register` membaca `request.form`, membina `User`, menambahnya ke sesi dan melakukan commit. Selepas itu ia mengubah hala ke `secrets`, yang menghantar `current_user.name` ke templat.

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

## Rupanya

![Borang pendaftaran](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01a-register-form.png)

![Halaman rahsia menyambut pengguna](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-01b-secrets-greeting.png)

## Apa yang kami perolehi

- `POST` borang menjadi baris pangkalan data melalui objek model.
- `request.form.get()` membaca apa yang ditaip pengguna.
- Ubah hala selepas menyimpan membawa pengguna ke halaman seterusnya.
- Dalam versi pertama ini kata laluan disimpan sebagai teks biasa, yang dibaiki dalam langkah 4.

Langkah seterusnya: [Muat turun fail](Step-2-Download-A-File-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
