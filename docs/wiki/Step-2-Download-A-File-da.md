[English](Step-2-Download-A-File) · **Dansk** · [Bahasa Malaysia](Step-2-Download-A-File-ms)

# Trin 2: Download en fil

## Hvad lektionen bad om

Få linket på `secrets.html` til at kalde `GET /download`, og brug Flasks `send_from_directory()` i ruten `download` til at returnere `static/files/cheat_sheet.pdf`.

## Hvad vi byggede

Linket bruger `url_for('download')`. Ruten angiver mappen `static` og filens sti i den.

```python
@app.route("/download")
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")
```

## Sådan ser det ud

![Download-linket](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02a-download-link.png)

![Svaret fra /download: status 200 og en PDF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02b-download-response.png)

## Hvad vi fik ud af det

- `send_from_directory()` leverer en fil sikkert fra en navngiven mappe.
- Filer til download hører hjemme i en kendt mappe som `static/files`.
- På dette tidspunkt kan alle, der kender URL'en, hente filen; trin 5 beskytter den.

Forrige trin: [Registrer nye brugere og hils på dem](Step-1-Register-And-Greet-da) · Næste trin: [Kryptering, hashing og adgangskodeangreb](Step-3-Encryption-And-Hashing-da) · [Tilbage til oversigten](Home-da)
