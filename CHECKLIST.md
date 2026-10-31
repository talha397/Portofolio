# Build Checklist: Nov 1 → Nov 15

Shared to-do list. **Owner:** 🧑 Talha · 🤖 Claude. Tick boxes as we go (edit on GitHub or ask Claude).

## The key change: the head scan is late, so nothing waits for it

We build the **whole Blender scene around a placeholder head** (Blender's built-in "Suzanne" monkey, or a simple sphere head). Eyes, stickers, empties, camera path and export all get learned and tested on the placeholder. When the scan arrives, we swap the mesh and re-fit the stickers, which takes about a day.

**Scan deadline: Sun Nov 9.** If there's no scan by then, we sculpt a stylized head instead (Nov 10–11) and still launch on time.

---

## Week 1: Foundations (Nov 1–7)

### Setup
- [ ] 🧑 Install **Blender 4.x** (blender.org)
- [ ] 🧑 Install **Node.js 20+** and **Git**, and clone this repo to your laptop
- [ ] 🤖 Bring Sen's code into this repo (MIT-licensed code only) and strip out Sen's personal assets
- [ ] 🤖 Add a **placeholder `me.glb`** so the site runs end-to-end before any Blender work
- [ ] 🤖 Add a step-by-step `SETUP.md`: run the site locally and see changes live
- [ ] 🧑 Run the site locally (`npm install` → `npm run dev`) and confirm it works

### Blender learning (no head needed)
- [ ] 🧑 Donut tutorial ep. 1–2: navigation, objects, modes
- [ ] 🧑 Open Sen's `sen.blend` (for study only) and find the camera, the `focus-*` empties, the eye mesh and the `CameraAction`
- [ ] 🤖 Write `BLENDER-GUIDE.md`: exactly what to build, naming rules and export settings
- [ ] 🧑 New file `talha.blend` with the placeholder head
- [ ] 🧑 Eyes: two spheres named `eye_L` and `eye_R` with a googly-eye material
- [ ] 🧑 First export to `me.glb`, then check in the browser that the **eyes follow the cursor** ✅ *(milestone)*

### Content (writing, no head needed)
- [ ] 🧑 Graduation month and the roles you're targeting
- [ ] 🧑 Hero line: "Hi, I'm Talha…" (1–2 sentences, rough is fine)
- [ ] 🧑 5 résumé entries: title, place, dates, one line each (rough notes are fine)
- [ ] 🧑 Pick 3–5 projects: title, one-line summary, link
- [ ] 🧑 Links: LinkedIn, GitHub, email. Résumé PDF
- [ ] 🤖 Polish the copy into a short, punchy voice and put it in the code
- [ ] 🤖 Rename the timeline and sections for your story (Undergrad → Grad → Research → Experience → Graduating)

### Look & feel
- [ ] 🧑 Pick a vibe: send 2–3 reference images or colours you like
- [ ] 🤖 Propose 2 colour and font options, you choose one, and I apply it (replacing Sen's look)

---

## Week 2: Scene, swap, ship (Nov 8–15)

### Stickers
- [ ] 🧑 Final sticker list: 8–12 stickers, each with a one-line fact (see `CONCEPT.md` §3)
- [ ] 🧑 / 🤖 Make the sticker art: you draw them, or I help generate them, as transparent PNGs with a white border
- [ ] 🧑 Place the stickers on the placeholder head (image planes + Shrinkwrap)

### Camera path
- [ ] 🧑 Empties `focus-0` to `focus-5` and `focus-works`, each pointing at its sticker
- [ ] 🧑 Camera keyframes at frames 0, 50, 100, 150, 200, 250 and the end. Name the action `CameraAction`
- [ ] 🧑 Export, then scroll through the site and check the camera stops line up with the résumé ✅ *(milestone)*
- [ ] 🤖 Tune focus, blur, glow and lighting in code to match

### Head swap
- [ ] 🧑 **Head scan by Sun Nov 9** (otherwise fallback: stylized sculpt Nov 10–11)
- [ ] 🧑 Clean up the scan: decimate to ~50k triangles, texture ≤ 2K, delete the scanned eyes
- [ ] 🧑 Swap it into `talha.blend`, then re-fit the eyes and stickers
- [ ] 🧑 Final export
- [ ] 🤖 Compress the `.glb` so it loads fast on phones

### Projects & polish
- [ ] 🧑 Screenshots and images for each project
- [ ] 🤖 Project gallery and detail pages built from your write-ups
- [ ] 🤖 Grad touches: cap sticker moment, "Graduating · Open to roles" stamp
- [ ] 🤖 Mobile layout, loading screen, social-share preview image, page title
- [ ] 🤖 Update `LICENSE` / `NOTICE`: keep Sen's MIT notice for the code and mark the content as yours

### Ship
- [ ] 🤖 Set up auto-deploy to GitHub Pages
- [ ] 🧑 Turn on Pages in the repo settings (I'll give exact clicks)
- [ ] 🧑 Test on your phone and laptop, and get 2–3 friends to try it
- [ ] 🤖 Fix the feedback
- [ ] 🧑 🎓 **Launch: Sat Nov 15**
- [ ] 🧑 Optional: buy a domain, then 🤖 connect it

---

## Day-by-day

| Date | 🧑 Talha | 🤖 Claude |
|---|---|---|
| Sat Nov 1 | Install Blender, Node and Git. Donut ep. 1 | Code setup, placeholder `.glb`, `SETUP.md` |
| Sun Nov 2 | Donut ep. 2. Run the site locally | `BLENDER-GUIDE.md` |
| Mon Nov 3 | Study `sen.blend`. Send grad date, roles and links | Rename sections for your story |
| Tue Nov 4 | Placeholder head + eyes in Blender | Colour and font options |
| Wed Nov 5 | Export, **eyes working** ✅. Draft résumé entries | Apply chosen look |
| Thu Nov 6 | Sticker list + projects | Polish copy into the site |
| Fri Nov 7 | Sticker art | Projects gallery scaffolding |
| Sat Nov 8 | Stickers on the head, then empties | Help with stickers if needed |
| Sun Nov 9 | Camera path, **scroll working** ✅. **Scan deadline** | Tune focus, blur and lighting |
| Mon Nov 10 | Scan cleanup (or start stylized sculpt) | Grad touches, mobile layout |
| Tue Nov 11 | Head swap, re-fit eyes and stickers | Deploy pipeline |
| Wed Nov 12 | Final export, project screenshots | Compress model, add project pages |
| Thu Nov 13 | Turn on Pages, test on devices | Fixes |
| Fri Nov 14 | Friend feedback | Fixes, licence notice |
| **Sat Nov 15** | 🎓 **Launch** | Domain (optional) |
