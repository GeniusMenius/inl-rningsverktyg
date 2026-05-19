# Inlärningsverktyg

Ett fristående inlärningsverktyg för yrkesutbildning inom automation och styrteknik. Körs helt offline direkt i webbläsaren – ingen installation, ingen inloggning, ingen server.

🌐 **Live:** [teach.tmhp.xyz](https://teach.tmhp.xyz)

---

## Funktioner

- **Flashkort** – bläddra igenom begrepp och definitioner per kategori, blanda med en knapp, navigera med tangentbord (← → mellanslag)
- **Quiz** – välj antal frågor och läge, få direkt feedback med förklaring efter varje svar
- **SM-2 Spaced Repetition** – algoritmen spårar varje fråga individuellt. Svarar du fel klassas frågan som *Fel* och dyker upp oftare
- **Svaga områden** – fokuserat läge som bara visar frågor du svarat fel på
- **Jämförelsefliken** – snabbreferens för tabeller och formler kopplade till modulen
- **Progressbar** – översiktssidan visar hur stor andel av frågorna du har rätt på per kategori
- **Konfetti** – vid 100% rätt på ett quiz 🎉
- **Mörkt läge** – växla i headern
- **Spara till USB** – exportera din modul inkl. SM-2-framsteg som JSON, ladda in den igen på valfri dator
- **Adminpanel** – lägg till, redigera och ta bort frågor och flashkort (🔧-ikonen)

---

## Moduler

Modulerna är separata JSON-filer som laddas in i verktyget. Ladda ned en modul från mappen [`moduler/`](./moduler/) och klicka **📂 Ladda modul** i verktygets header.

| Modul | Kategorier | Quiz | Flashkort | Version |
|---|---|---|---|---|
| 🏭 Distribuerade Styrsystem | SCADA, RTU, DCS, PROFIBUS, BAS | 110 | 118 | v1.1 |
| ⚙️ Industriautomation | Cylindrar, Ventiler, Gripdon, Sensorer, Styrsystem, Beräkningar | 73 | 54 | v1.0 |

### Skapa en egen modul

En modul är en JSON-fil med följande struktur:

```json
{
  "name": "Mitt ämne",
  "icon": "📚",
  "version": "1.0",
  "categories": [
    { "name": "Kategori A", "color": "#4f46e5", "icon": "⚡" }
  ],
  "quiz": [
    {
      "c": "Kategori A",
      "q": "Vad är frågan?",
      "o": ["Alternativ 1", "Alternativ 2", "Alternativ 3", "Alternativ 4"],
      "a": 0,
      "e": "Förklaring som visas efter svar."
    }
  ],
  "flashcards": [
    { "c": "Kategori A", "t": "Term", "d": "Definition" }
  ],
  "comparison": "",
  "srData": {}
}
```

- `a` är index för rätt svar (0–3)
- `srData` lämnas tom `{}` – fylls på automatiskt av verktyget
- `comparison` kan innehålla HTML som visas i Jämför-fliken

---

## USB-flödet (lånedator)

1. Lägg `index.html` + modulens JSON-fil på ett USB-minne
2. Öppna `index.html` i webbläsaren direkt från USB
3. Klicka **📂 Ladda modul** och välj JSON-filen
4. Plugga – SM-2-data sparas automatiskt i webbläsarens localStorage som backup
5. Klicka **💾 Spara till USB** när du är klar – laddar ned en uppdaterad JSON med dina framsteg
6. Kopiera filen tillbaka till USB – ta med dig till nästa session

---

## Tangentbordsgenvägar

| Tangent | Funktion |
|---|---|
| `←` `→` | Föregående / nästa flashkort |
| `Mellanslag` eller `Enter` | Vänd flashkortet |
| `1` `2` `3` `4` | Välj svarsalternativ i quiz |
| `Enter` eller `→` | Nästa fråga (efter svar) |

---

## Bidra

Hittar du fel i en fråga eller vill lägga till innehåll?

1. Öppna verktyget → **🔧 Adminpanel** → redigera frågan
2. Exportera modulen som JSON (**Im/Export → Spara till USB**)
3. Öppna en Pull Request med den uppdaterade JSON-filen i `moduler/`

Eller öppna en [Issue](https://github.com/GeniusMenius/inl-rningsverktyg/issues) om du hittar en bugg.

---

## Teknik

Ren HTML/CSS/JavaScript – inga beroenden, inga ramverk, ingen byggprocess. Hostad som statisk sida via [Netlify](https://netlify.com) med automatisk deploy från `main`-branchen.
