<div align="center">

# 🐾 Petnunu

**Un animaletto virtuale che vive sulla tua scrivania — macOS · Windows · Linux.**

Il tuo pet cammina, salta, si arrampica sui bordi dello schermo e fa un pisolino dentro una
finestra trasparente che fluttua sopra ogni app — si comanda dalla barra dei menu, con
Pomodoro e modalità focus per rendere il lavoro un po' più leggero.

[![Download](https://img.shields.io/github/v/release/hihi-team/pet-nunu-info?label=Download&style=for-the-badge&color=ff8fab)](https://github.com/hihi-team/pet-nunu-info/releases/latest)
&nbsp;
![macOS](https://img.shields.io/badge/macOS-14%2B-black?style=for-the-badge&logo=apple)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=for-the-badge&logo=windows)
![Linux](https://img.shields.io/badge/Linux-X11-FCC624?style=for-the-badge&logo=linux&logoColor=black)
&nbsp;
![Languages](https://img.shields.io/badge/Web-22%20lingue-8f7fdb?style=for-the-badge&logo=googletranslate&logoColor=white)

[English](README.md) ·
[Tiếng Việt](README.vi.md) ·
[简体中文](README.zh-Hans.md) ·
[繁體中文](README.zh-Hant.md) ·
[日本語](README.ja.md) ·
[한국어](README.ko.md) ·
[Español](README.es.md) ·
[Português (BR)](README.pt-BR.md) ·
[Français](README.fr.md) ·
[Deutsch](README.de.md) ·
**Italiano** ·
[Русский](README.ru.md) ·
[Українська](README.uk.md) ·
[Polski](README.pl.md) ·
[Nederlands](README.nl.md) ·
[Svenska](README.sv.md) ·
[Türkçe](README.tr.md) ·
[العربية](README.ar.md) ·
[हिन्दी](README.hi.md) ·
[ไทย](README.th.md) ·
[Bahasa Indonesia](README.id.md) ·
[Bahasa Melayu](README.ms.md)

</div>

---

## ⬇️ Download

Scarica l'ultima versione dalle **[Releases](https://github.com/hihi-team/pet-nunu-info/releases/latest)**, poi scegli il file adatto al tuo sistema:

| Sistema | File | Installazione |
|---|---|---|
| 🍎 **macOS** 14+ | `Petnunu-macOS-*.dmg` (oppure `.zip`) | Apri il `.dmg` → trascina **Petnunu.app** in **Applications** |
| 🪟 **Windows** 10/11 | `Petnunu_*-setup.exe` (oppure `.msi`) | Avvia l'installer → avanti → fatto |
| 🐧 **Linux** (X11) | `Petnunu_*.AppImage` · `.deb` | AppImage: `chmod +x` e poi esegui · `.deb`: `sudo dpkg -i` |

### Primo avvio
- **macOS** — l'app è **firmata con un Developer ID e notarizzata**, quindi si apre come qualsiasi app normale (doppio clic), senza avvisi di Gatekeeper.
- **Windows** — SmartScreen potrebbe mostrare *«Windows protected your PC»* → **More info → Run anyway** (non abbiamo ancora acquistato un certificato di code signing).
- **Linux** — il supporto migliore è su **X11**. Su **GNOME Wayland**, accedi a una sessione **«Xorg/X11»** così il pet può posizionarsi e restare sempre in primo piano.

**Requisiti:** macOS 14 (Sonoma)+ · Windows 10/11 · un desktop Linux con X11/XWayland.

---

## ✨ Funzionalità

- 🐣 **Pet in overlay sul desktop** — cammina, salta, dorme, si arrampica e si aggrappa ai bordi dello schermo, segue il cursore, e lo trascini dove vuoi.
- 💖 **Cure ed emozioni** — dagli da mangiare, accarezzalo, gioca con lui, mettilo a nanna; statistiche happiness / energy / hunger / affection.
- 🪙 **Monete, missioni e obiettivi** — missioni giornaliere, obiettivi, portafoglio di monete.
- 🍅 **Pomodoro e modalità focus** — promemoria per pause, acqua e riposo degli occhi, statistiche di focus (giornaliere, settimanali, serie).
- 🛒 **Pet Store** — sblocca altri pet con le monete.
- 🌱 **Fai crescere di livello i tuoi pet** + classifica della community.
- 🎨 **Petnunu Studio** — crea il tuo pet.
- 📦 **Importa i tuoi pacchetti di pet**.
- 🖥️ **Multi-monitor**, tray / barra dei menu, guida iniziale, suoni.

> Account, portafoglio di monete, negozio e pacchetti di pet sono **condivisi fra tutte e tre le piattaforme**.

---

## 🌍 Lingue

**[Petnunu World](https://www.petnunu.com)** — la parte web (catalogo pet, portafoglio di monete,
Studio, forum, classifica) — parla **22 lingue**, scelte automaticamente in base al browser e
cambiabili in qualsiasi momento in fondo alla pagina:

| | | | |
|---|---|---|---|
| English | Tiếng Việt | 简体中文 | 繁體中文 |
| 日本語 | 한국어 | Español | Português (BR) |
| Français | Deutsch | Italiano | Русский |
| Українська | Polski | Nederlands | Svenska |
| Türkçe | العربية | हिन्दी | ไทย |
| Bahasa Indonesia | Bahasa Melayu | | |

L'arabo ha un layout completo da destra a sinistra.
Le pagine di **Termini, Informativa sulla privacy e DMCA** esistono solo in inglese e
vietnamita — tutte le altre lingue leggono la versione inglese, che è quella vincolante.

Nell'app: **Windows/Linux** includono inglese + vietnamita; **macOS** per ora è solo in inglese.

---

## 🌐 Link

- 🏠 **[Petnunu World](https://www.petnunu.com)** — catalogo pet, forum, classifica, portafoglio di monete *(web, 22 lingue)*
- 🛒 **[Pet Store](https://www.petnunu.com/store)** — sfoglia e adotta i pet
- 📝 **[Changelog / What's new](https://github.com/hihi-team/pet-nunu-info/releases)**

---

## ❓ FAQ

**L'app è open source?**
Le build vengono pubblicate qui pubblicamente; il codice sorgente resta privato. Questo repository serve a distribuire l'app.

**Le build Windows/Linux hanno tutto quello che c'è su macOS?**
Condividono lo stesso server, account, portafoglio e formato dei pacchetti di pet. La build macOS (Swift) è arrivata per prima; quella Windows/Linux (Tauri) sta procedendo verso la parità completa.

**La mia lingua è supportata?**
Il web parla 22 lingue. L'app Windows/Linux include inglese + vietnamita; l'app macOS per ora è solo in inglese.

**Ha un costo?**
Scaricarla e usarla è gratis. Alcuni oggetti nell'app si possono comprare con le monete.

**Hai trovato un bug / hai un'idea?**
Apri una **[Issue](https://github.com/hihi-team/pet-nunu-info/issues)** in questo repository.

---

<div align="center">
<sub>© hihiteam · Made with 🐾 for macOS · Windows · Linux</sub>
</div>
