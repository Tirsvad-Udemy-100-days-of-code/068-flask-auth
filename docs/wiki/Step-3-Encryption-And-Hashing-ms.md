[English](Step-3-Encryption-And-Hashing) · [Dansk](Step-3-Encryption-And-Hashing-da) · **Bahasa Malaysia**

# Langkah 3: Penyulitan, pencincangan dan serangan kata laluan

## Apa yang diminta dalam kuliah

Dua kuliah teori: mengapa kata laluan teks biasa tidak selamat, bagaimana penyulitan dan pencincangan berbeza, dan bagaimana penggodam menyerang kata laluan yang disimpan.

## Apa yang kami bina

Tiada apa-apa dibina dalam langkah ini. Ilustrasi ini dijana untuk panduan ini: kata laluan yang sama sentiasa memberi cincang yang sama, manakala garam menjadikan setiap nilai yang disimpan berbeza.

## Rupanya

![Pencincangan berbanding penggaraman](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-03-hashing-vs-salting.png)

## Apa yang kami perolehi

- Penyimpanan teks biasa mendedahkan setiap pengguna jika pangkalan data bocor.
- Penyulitan memerlukan kunci dan boleh diterbalikkan; cincang adalah sehala.
- Jadual cincang dan serangan kamus memecahkan kata laluan biasa dengan pantas, malah pada GPU moden.
- Kata laluan panjang dan kompleks serta garam menjadikan serangan itu jauh lebih sukar.

Langkah sebelumnya: [Muat turun fail](Step-2-Download-A-File-ms) · Langkah seterusnya: [Cincang dan garamkan kata laluan dengan Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
