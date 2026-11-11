[English](Step-2-Download-A-File) · [Dansk](Step-2-Download-A-File-da) · **Bahasa Malaysia**

# Langkah 2: Muat turun fail

## Apa yang diminta dalam kuliah

Jadikan pautan pada `secrets.html` memanggil `GET /download`, dan gunakan `send_from_directory()` Flask dalam laluan `download` untuk memulangkan `static/files/cheat_sheet.pdf`.

## Apa yang kami bina

Pautan menggunakan `url_for('download')`. Laluan menamakan folder `static` dan laluan fail di dalamnya.

```python
@app.route("/download")
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")
```

## Rupanya

![Pautan muat turun](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02a-download-link.png)

![Respons /download: status 200 dan PDF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02b-download-response.png)

## Apa yang kami perolehi

- `send_from_directory()` menyajikan fail dengan selamat dari folder yang dinamakan.
- Fail untuk dimuat turun diletakkan dalam folder yang diketahui seperti `static/files`.
- Pada ketika ini sesiapa yang tahu URL boleh memuat turun fail; langkah 5 melindunginya.

Langkah sebelumnya: [Daftar pengguna baharu dan sambut mereka](Step-1-Register-And-Greet-ms) · Langkah seterusnya: [Penyulitan, pencincangan dan serangan kata laluan](Step-3-Encryption-And-Hashing-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
