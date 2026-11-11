**English** · [Dansk](Step-2-Download-A-File-da) · [Bahasa Malaysia](Step-2-Download-A-File-ms)

# Step 2: Download a file

## What the lecture asked

Make the link on `secrets.html` call `GET /download`, and use Flask's `send_from_directory()` in the `download` route to return `static/files/cheat_sheet.pdf`.

## What we built

The anchor uses `url_for('download')`. The route names the `static` folder and the path of the file inside it.

```python
@app.route("/download")
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")
```

## What it looks like

![The download link](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02a-download-link.png)

![The response of /download: status 200 and a PDF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-02b-download-response.png)

## What we gained

- `send_from_directory()` serves a file safely from a named folder.
- Files for download belong in a known folder such as `static/files`.
- At this point anyone who knows the URL can download the file; step 5 protects it.

Previous step: [Register new users and greet them](Step-1-Register-And-Greet) · Next step: [Encryption, hashing and password attacks](Step-3-Encryption-And-Hashing) · [Back to the overview](Home)
