# Her Little Universe ✨

A complete, cinematic, fully animated personal website — a tiny corner of the internet made just for someone special.

## Quick Start

**No installation or build step required.** This is a pure HTML/CSS/JavaScript application.

1. Open **`index.html`** directly in any modern browser.
2. Or serve with any static file server for the best experience:
   - **VS Code**: Install the "Live Server" extension → right-click `index.html` → "Open with Live Server"
   - **Python**: `python -m http.server 8080` (then visit http://localhost:8080)
   - **Node.js** (if available): `npx serve .`

---

## Adding Your Photographs

### Where to Put Them
Place all photographs in the `public/images/` folder:

```
public/
  images/
    photo-hero.jpg      ← Hero background (large, landscape recommended)
    photo-01.jpg        ← Gallery photo 1
    photo-02.jpg        ← Gallery photo 2
    photo-03.jpg        ← Gallery photo 3
    photo-04.jpg        ← Scrapbook photo 1
    photo-05.jpg        ← Scrapbook photo 2
    photo-06.jpg        ← Mosaic photo 1
    photo-07.jpg        ← Mosaic photo 2
    photo-08.jpg        ← Secret section reveal photo
    photo-final.jpg     ← Closing scene photo (portrait recommended)
```

**Supported formats:** JPG, JPEG, PNG, WebP, AVIF

**Recommended sizes:**
- Hero image: at least 1920×1080px
- Gallery / scrapbook: at least 800×600px
- Final photo: at least 800×1000px (portrait works beautifully)

---

## Personalizing the Content

All editable text lives in **`src/data/siteContent.js`**.

Open that file and change:

### Photos
```js
photos: [
  {
    id: "photo-01",
    src: "images/photo-01.jpg",   // ← change filename to match yours
    alt: "Personal photograph",   // ← describe the photo for accessibility
    title: "A Little Moment",
    caption: "A little moment worth keeping.",  // ← your caption
    section: "gallery",   // "gallery" | "scrapbook" | "mosaic" | "secret" | "final"
  },
  // ... add or remove entries
]
```

### Personal Messages
```js
letter: {
  body: `Hey!

Your personal message goes here.
Write anything you'd like.`
},

closing: {
  heading: "And that's your little world.",
  body: "Made with care, a little creativity, and the hope of making you smile.",
  signature: "— from a friend ✨",   // ← change to your preferred sign-off
},

secret: {
  message: "Your editable surprise message goes here.",
},
```

### Introduction Text
```js
introduction: {
  firstLine: "A little corner of the internet...",
  secondLine: "...made just for you.",
  buttonText: "Enter Your Little World",
},
```

---

## Optional: Adding Ambient Music

1. Place an audio file named `ambient.mp3` in `public/audio/`
2. The music button will appear automatically (bottom-left)
3. Music only plays when the visitor explicitly clicks the ♪ button (no autoplay)

**If no audio file is present**, the button is hidden automatically.

---

## Website Sections

| Scene | Section | Description |
|-------|---------|-------------|
| 1 | Intro | Cinematic starfield with animated entry |
| 2 | Hero | Large photo reveal with heading |
| 3 | Universe | Interactive floating navigation nodes |
| 4 | Gallery | Editorial photo grid with lightbox |
| 5 | Scrapbook | Paper-style photo cards with captions |
| 6 | Mosaic | Dramatic tiled photo composition |
| 7 | Secret | Animated envelope with surprise message |
| 8 | Letter | Envelope that opens to reveal a personal note |
| 9 | Final | Closing cinematic scene with selected photo |

---

## Browser Support

Works in all modern browsers:
- Chrome / Chromium 80+
- Firefox 80+
- Safari 14+
- Edge 80+

---

## Troubleshooting

**Photos not showing?**
- Make sure filenames exactly match what's in `siteContent.js` (case-sensitive)
- Use forward slashes in paths: `"images/photo-01.jpg"` not `"images\photo-01.jpg"`
- Open the browser's developer console (F12) to see any loading errors

**Fonts not loading?**
- The site requires an internet connection to load Google Fonts
- Offline fallbacks (Georgia serif, Helvetica sans-serif) are applied automatically

**Animations too slow on your device?**
- Enable "Reduce Motion" in your operating system's accessibility settings to simplify all animations

---

## File Structure

```
her-little-universe/
├── index.html                    ← Open this in your browser
├── public/
│   ├── images/                   ← ✅ Place your photos here
│   └── audio/
│       └── ambient.mp3           ← Optional: ambient background music
├── src/
│   ├── data/
│   │   └── siteContent.js        ← ✅ Edit captions, messages, photo paths
│   ├── styles/
│   │   ├── globals.css           ← Design system (colors, typography)
│   │   ├── animations.css        ← Animation keyframes & utilities
│   │   └── responsive.css        ← Section layouts & responsive rules
│   └── components/
│       └── app.js                ← Application logic (StarField, Lightbox, etc.)
└── README.md                     ← This file
```

---

Made with care ✨
