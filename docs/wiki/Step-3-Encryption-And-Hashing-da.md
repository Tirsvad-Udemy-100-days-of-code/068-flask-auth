[English](Step-3-Encryption-And-Hashing) · **Dansk** · [Bahasa Malaysia](Step-3-Encryption-And-Hashing-ms)

# Trin 3: Kryptering, hashing og adgangskodeangreb

## Hvad lektionen bad om

To teoriforelæsninger: hvorfor adgangskoder i klartekst er usikre, hvordan kryptering og hashing adskiller sig, og hvordan hackere angriber gemte adgangskoder.

## Hvad vi byggede

Der bygges ikke noget i dette trin. Illustrationen er lavet til denne gennemgang: den samme adgangskode giver altid den samme hash, mens et salt gør hver gemt værdi forskellig.

## Sådan ser det ud

![Hashing kontra salting](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-03-hashing-vs-salting.png)

## Hvad vi fik ud af det

- Klartekst afslører alle brugere, hvis databasen lækkes.
- Kryptering kræver en nøgle og kan vendes; en hash er envejs.
- Hash-tabeller og ordbogsangreb knækker almindelige adgangskoder hurtigt, selv på moderne GPU'er.
- Lange, komplekse adgangskoder og et salt gør angrebene meget sværere.

Forrige trin: [Download en fil](Step-2-Download-A-File-da) · Næste trin: [Hash og salt adgangskoder med Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug-da) · [Tilbage til oversigten](Home-da)
