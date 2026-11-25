# Build Checklist: Nov 25 → Dec 5 (launch)

Shared to-do list. **Owner:** 🧑 Talha · 🤖 Claude. Tick boxes as we go (edit on GitHub or ask Claude).

> **Replanned Nov 25.** The original Nov 15 date slipped, so this is the compressed 11-day plan.
> The scene is built on a **placeholder head** (`blender/placeholder.blend`). Your scan gets swapped in later.
> **Scan deadline: Sun Nov 30.** If there's no scan by then, sculpt a stylized head on Dec 1 and still launch on time.

---

## Setup
- [x] 🤖 Bring Sen's code into this repo (MIT-licensed code only) with all of Sen's personal content removed
- [x] 🤖 Placeholder 3D scene (`blender/placeholder.blend` → `web/public/models/me.glb`): head, googly eyes, grad cap, 4 stickers, camera path. Tested: it renders, the camera visits every stop, and there are no errors.
- [x] 🤖 `SETUP.md`: step-by-step guide to running the site and opening the scene
- [x] 🤖 `LICENSE` / `NOTICE`: Sen's MIT notice kept for the code, and your content marked as yours
- [ ] 🧑 Install **Git**, **Node 20+** and **Blender 5.2 LTS**
- [ ] 🧑 Follow `SETUP.md`: run the site locally and open `placeholder.blend`

## Blender (learn on the placeholder)
- [ ] 🧑 Donut tutorial ep. 1–2: navigation, objects, modes
- [ ] 🤖 `BLENDER-GUIDE.md`: exact steps for eyes, stickers, empties, camera keys and export
- [ ] 🧑 Save As `talha.blend`. Move an eye, re-export, and see it change in the browser
- [ ] 🧑 Rebuild the eyes yourself (sphere, 2 materials, origin at centre, named `eye_…`) ✅ *(milestone: eyes follow cursor)*
- [ ] 🧑 Real stickers on the head (image planes + Shrinkwrap)
- [ ] 🧑 Move the `focus-*` empties onto your stickers and re-key the camera at 0/50/100/150/200/250/350 ✅ *(milestone: scroll path is yours)*

## Content
- [ ] 🧑 Graduation month and the roles you're targeting
- [ ] 🧑 About text: 1–2 sentences (`COPY` in `web/src/App.tsx`)
- [ ] 🧑 5 résumé entries: title, place, dates, one line each (rough notes are fine)
- [ ] 🧑 3–5 projects: title, one-line summary, link, 1–2 images each
- [ ] 🧑 Links: LinkedIn, email. Résumé PDF
- [ ] 🤖 Polish your notes into the site's voice and fill in every `[bracket]`
- [ ] 🤖 Project detail pages from your write-ups

## Stickers
- [ ] 🧑 Sticker list: 8–12 stickers, each with a one-line fact (`CONCEPT.md` §3)
- [ ] 🧑 / 🤖 Sticker art: transparent PNGs with a white die-cut border

## Look & feel
- [ ] 🧑 Send 2–3 reference images or colours you like
- [ ] 🤖 Two colour and font options → you pick → I apply them (replacing Sen's green and fonts)
- [ ] 🤖 Grad touches: "Graduating · Open to roles" stamp, cap moment

## Head swap
- [ ] 🧑 **Head scan by Sun Nov 30** (Polycam / KIRI Engine / RealityScan, with a friend and even light)
- [ ] 🧑 Clean up the scan: decimate to ~50k triangles, texture ≤ 2K, remove the scanned eyes
- [ ] 🧑 Swap it in for `head` in `talha.blend`, then re-fit the eyes and stickers. Export
- [ ] 🤖 Compress the `.glb` so it loads fast on phones

## Ship
- [ ] 🤖 Auto-deploy workflow for GitHub Pages
- [ ] 🧑 Turn on Pages in the repo settings (I'll give exact clicks)
- [ ] 🧑 Test on your phone and laptop, and have 2–3 friends try it
- [ ] 🤖 Fixes, mobile polish, page title and share image
- [ ] 🧑 🎓 **Launch: Fri Dec 5**
- [ ] 🧑 Optional: buy a domain, then 🤖 connect it

---

## Day-by-day

| Date | 🧑 Talha | 🤖 Claude |
|---|---|---|
| **Tue Nov 25** | Install tools. Run `SETUP.md`. Donut ep. 1 | ✅ Code, placeholder scene, `SETUP.md` |
| **Wed Nov 26** | Donut ep. 2. Explore `placeholder.blend`. Send grad date, roles, links and rough résumé notes | `BLENDER-GUIDE.md`. Fill in your content |
| **Thu Nov 27** | Save As `talha.blend`, rebuild the eyes ✅. Sticker list | Colour and font options |
| **Fri Nov 28** | Sticker art. Pick projects and gather images | Apply chosen look, grad touches |
| **Sat Nov 29** | Stickers on the head, move the empties | Projects gallery and detail pages |
| **Sun Nov 30** | Re-key the camera ✅. **Scan deadline** | Tune focus, blur and lighting to your scene |
| **Mon Dec 1** | Scan cleanup (or stylized sculpt) | Deploy pipeline |
| **Tue Dec 2** | Head swap, re-fit the eyes and stickers, export | Compress model, mobile layout |
| **Wed Dec 3** | Turn on Pages, test on devices | Fixes |
| **Thu Dec 4** | Friend feedback | Fixes, share image |
| **Fri Dec 5** | 🎓 **Launch** | Domain (optional) |
