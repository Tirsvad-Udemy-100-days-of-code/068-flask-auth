**English** · [Dansk](Step-3-Encryption-And-Hashing-da) · [Bahasa Malaysia](Step-3-Encryption-And-Hashing-ms)

# Step 3: Encryption, hashing and password attacks

## What the lecture asked

Two theory lectures: why plain text passwords are unsafe, how encryption and hashing differ, and how hackers attack stored passwords.

## What we built

Nothing is built in this step. The illustration is generated for this walkthrough: the same password always gives the same hash, while a salt makes each stored value different.

## What it looks like

![Hashing versus salting](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-03-hashing-vs-salting.png)

## What we gained

- Plain text storage exposes every user if the database leaks.
- Encryption needs a key and can be reversed; a hash is one way.
- Hash tables and dictionary attacks crack common passwords fast, even on modern GPUs.
- Long, complex passwords and a salt make those attacks much harder.

Previous step: [Download a file](Step-2-Download-A-File) · Next step: [Hash and salt passwords with Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug) · [Back to the overview](Home)
