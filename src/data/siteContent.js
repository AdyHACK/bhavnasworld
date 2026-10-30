/**
 * ═══════════════════════════════════════════════════════════════════
 *  HER LITTLE UNIVERSE — Central Content Configuration
 * ═══════════════════════════════════════════════════════════════════
 *
 *  This file controls all personalizable content on the website.
 *  Edit this file to change photographs, captions, messages, and text.
 *
 *  PHOTOS: Place your images in the /public/images/ folder.
 *  Then update the `src` paths below to match the actual filenames.
 *
 *  EXAMPLE: If you have a file at public/images/portrait.jpg
 *  Set src to: "images/portrait.jpg"
 * ═══════════════════════════════════════════════════════════════════
 */

const siteContent = {

  // ── Site Meta ──────────────────────────────────────────────────
  siteTitle: "Bhavna's Little Universe",
  siteDescription: "A tiny corner of the internet, made just for Bhavna.",

  // ── Introduction Screen ────────────────────────────────────────
  introduction: {
    firstLine: "A little corner of the internet...",
    secondLine: "...made just for you.",
    buttonText: "Enter Your Little World",
  },

  // ── Hero Section ───────────────────────────────────────────────
  hero: {
    eyebrow: "ONE LITTLE WORLD",
    heading: "Made of little moments.",
    subheading: "A collection of photographs, tiny details, and a few unexpected things along the way.",
    buttonText: "Explore the World ↓",
    // Photo used as hero background — replace with your chosen image
    photo: {
      src: "public/images/photo-hero.png",
      alt: "A personal photograph",
    },
  },

  // ── Photo Collection ───────────────────────────────────────────
  // Add or remove photo objects below.
  // Sections: "gallery" | "scrapbook" | "mosaic" | "secret" | "final"
  photos: [
    {
      id: "photo-01",
      src: "public/images/photo-01.png",
      alt: "Personal photograph",
      title: "A Little Moment",
      caption: "A little moment worth keeping.",
      section: "gallery",
      featured: true,
    },
    {
      id: "photo-02",
      src: "public/images/photo-02.png",
      alt: "Personal photograph",
      title: "Soft Light",
      caption: "Filed under: lovely things.",
      section: "gallery",
      featured: false,
    },
    {
      id: "photo-03",
      src: "public/images/photo-03.png",
      alt: "Personal photograph",
      title: "A Small Frame",
      caption: "Some pictures deserve their own page.",
      section: "gallery",
      featured: false,
    },
    {
      id: "photo-04",
      src: "public/images/photo-04.png",
      alt: "Personal photograph",
      title: "Kept Quietly",
      caption: "A small frame for a small moment.",
      section: "scrapbook",
      featured: true,
    },
    {
      id: "photo-05",
      src: "public/images/photo-05.png",
      alt: "Personal photograph",
      title: "Little Things",
      caption: "Little things, beautifully kept.",
      section: "scrapbook",
      featured: false,
    },
    {
      id: "photo-06",
      src: "public/images/photo-06.png",
      alt: "Personal photograph",
      title: "On a Quiet Day",
      caption: "On a quiet day, remembered.",
      section: "scrapbook",
      featured: false,
    },
    {
      id: "photo-07",
      src: "public/images/photo-07.png",
      alt: "Personal photograph",
      title: "Warm Corners",
      caption: "Warm corners, worth revisiting.",
      section: "mosaic",
      featured: true,
    },
    {
      id: "photo-final",
      src: "public/images/photo-final.png",
      alt: "Personal photograph — closing scene",
      title: "That's Your World",
      caption: "And that's your little world.",
      section: "final",
      featured: true,
    },
  ],

  // ── Gallery Section ────────────────────────────────────────────
  gallery: {
    eyebrow: "A COLLECTION OF LITTLE MOMENTS",
    heading: "Some things are too nice to leave in a folder.",
  },

  // ── Scrapbook Section ──────────────────────────────────────────
  scrapbook: {
    eyebrow: "LITTLE THINGS, BEAUTIFULLY KEPT",
    heading: "A few pictures, a little imagination,\nand some space for the unexpected.",
  },

  // ── Mosaic Section ─────────────────────────────────────────────
  mosaic: {
    heading: "Every little frame has its place.",
  },

  // ── Secret Section ─────────────────────────────────────────────
  secret: {
    teaser: "Hmm... there's something here.",
    buttonText: "Take a Look",
    message: "You found the little secret. ✨\nSome things are made to be discovered.",
  },

  // ── Letter Section ─────────────────────────────────────────────
  letter: {
    teaser: "ONE LAST THING...",
    subTeaser: "There's a little note for you.",
    buttonText: "Open the Note",
    heading: "A Little Note",
    // ↓ Edit the letter body freely. Use \n for line breaks.
    body: `Hey!

I wanted to make something a little different instead of sending another ordinary link.

So, I put together this tiny corner of the internet — with a few photographs, little details, and some unexpected things.

I hope exploring it brings a smile to your face.

That's the whole idea behind it. Some things are simply nice to make.`,
  },

  // ── Final Scene ────────────────────────────────────────────────
  closing: {
    heading: "And that's your little world bittu.",
    body: "Made with care, a little creativity, and the hope of making you smile.",
    // ↓ Change this to your preferred sign-off
    signature: "— Aadi ✦",
    buttonText: "Explore Again",
  },

};

// Make available as both a module export and a global (for vanilla JS)
if (typeof module !== "undefined") {
  module.exports = siteContent;
} else {
  // Primary: HLU_CONTENT (used by app.js)
  window.HLU_CONTENT = siteContent;
  // Legacy alias kept for compatibility
  window.siteContent = siteContent;
}
