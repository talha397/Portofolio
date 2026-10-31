# Portfolio Concept: "Sticker-Bombed Grad" (3D)

**Owner:** Talha Jameel
**Deadline:** Saturday, November 15, 2026
**Path:** A. Fork the MIT-licensed code from [dayinji/sen-3d-resume](https://github.com/dayinji/sen-3d-resume) and build every 3D asset myself in Blender.

---

## 1. The idea

A 3D model of my head, covered in stickers that tell my grad-school story. **Scrolling moves the camera** around the head, and each résumé entry has its own camera stop. The **eyes follow the cursor**. The small, tidy résumé text scrolls over the 3D scene so the facts stay readable.

**Contrast rule:** the 3D scene can be playful and messy. The text has to stay small, clean and easy to scan, because recruiters will skim it.

## 2. The story (camera stops)

Every stop is one résumé entry, and the camera points at a matching sticker on the face.

| Frame | Anchor (Blender empty) | Section | Camera looks at… |
|---|---|---|---|
| 0 | `focus-0` | **Hero:** "Hi, I'm Talha", one-line pitch | Full face, eye contact |
| 50 | `focus-1` | Undergrad: degree, school, years | University sticker |
| 100 | `focus-2` | Grad program: degree, school | Grad-school sticker |
| 150 | `focus-3` | Research / thesis | Research-topic sticker |
| 200 | `focus-4` | Internship / RA / TA experience | Work or tool sticker |
| 250 | `focus-5` | **Graduating [month 2026/27]: open to roles** | Graduation-cap sticker |
| end | `focus-works` | Projects gallery | Wide shot, the whole sticker-bombed head |

Stops can be added or removed later. `FOCUS_POINTS` in the code and the résumé entries just need to match.

## 3. Sticker list (to fill in)

Aim for 8–12. Each sticker gets a one-line fact.

| # | Sticker | Meaning / fact |
|---|---|---|
| 1 | University logo / mascot | |
| 2 | Graduation cap | Graduating ___ |
| 3 | Research topic icon | |
| 4 | Main tool or language | |
| 5 | Second tool | |
| 6 | Hometown / flag | |
| 7 | Hobby | |
| 8 | Coffee / late-night-lab joke | |
| 9 | Internship or lab | |
| 10 | Wildcard | |

Make them in Figma, Illustrator or Procreate, or generate them with AI. Export each one as a **transparent PNG with a white die-cut border**.

## 4. Original touches (so it's not a copy of Sen's)

- **Grad theme throughout:** a cap sticker, a "Graduating ___ · Open to roles" stamp, and maybe a cap toss at the end of the scroll.
- My own colour palette, fonts and background. Sen's are not reused.
- My own copy and voice.

## 5. Blender pipeline (what I'll learn)

| Step | What | Blender skills learned |
|---|---|---|
| 1. Basics | Navigation, objects, Edit vs Object mode, modifiers | Interface fundamentals |
| 2. Head | **Phone scan** (Polycam / KIRI Engine / RealityScan), then import and clean up | Mesh cleanup, Decimate modifier, fixing the origin and scale |
| 3. Eyes | Delete the scanned eyes and add two spheres named `eye_L` and `eye_R` | Modelling primitives, materials, naming for code |
| 4. Stickers | Image planes conformed to the face (Shrinkwrap) with alpha materials | Image textures, alpha, Shrinkwrap |
| 5. Lighting test | Make sure it looks good in the browser | Principled BSDF and how materials survive glTF export |
| 6. Camera path | Empties `focus-0…5` and `focus-works`, with camera keyframes at 0, 50, 100… The action must be named `CameraAction` | Keyframes, Graph Editor easing, Action naming |
| 7. Export | `me.glb` (glTF 2.0) | glTF export settings, keeping file size small |

**Fallback:** if scanning fails, sculpt a **stylized head** instead, which is simpler and arguably more fun. The camera, eyes and stickers steps stay the same.

**Learning resources:** Blender Guru's "Donut" series (episodes 1–3 for basics), Blender's official glTF export docs, and Sen's `blender/sen.blend` to study how the empties and camera are set up. That file is for learning only and won't be shipped.

## 6. Web side

- **Stack (inherited):** React 18 · TypeScript · three.js via React Three Fiber · Vite. Deployed free to GitHub Pages.
- **Content files to edit:**
  - About copy: `COPY` in `web/src/App.tsx`
  - Résumé timeline: `web/src/ui/Resume.tsx`
  - Camera-stop list: `web/src/data/focusPoints.ts`
  - Projects list: `web/src/data/works.ts`
  - Project write-ups: `web/src/content/works/<slug>.md`
  - Look (colours, blur, glow, lights): the constants at the top of `web/src/scene/Scene.tsx`
- **Must remove before launch** (Sen's personal content, not covered by MIT): `me.glb`, `sen.blend`, `public/images/*`, the ZOOOP logo, Sen's résumé, works and social links.
- **Must keep:** Sen's MIT `LICENSE` copyright notice for the code (the license requires it), with my own notice added for my content.

## 7. Schedule (Nov 1 → Nov 15)

| Date | Blender track | Web / content track |
|---|---|---|
| **Sat Nov 1** | Install Blender 4.x. Donut tutorial ep. 1–2 | Install Node 20. Bring the code into this repo and run it locally |
| **Sun Nov 2** | Open `sen.blend` and study the empties, camera and eyes | Write the bio and the 5 résumé entries |
| **Mon Nov 3** | **Scan the head** (needs a friend and good, even light) | Choose project list (3–5) |
| **Tue Nov 4** | Import the scan, clean up, decimate to ~50k triangles, texture ≤ 2K | Sticker list and facts finalized |
| **Wed Nov 5** | Eyes: `eye_L` and `eye_R` spheres plus googly material | Design or generate the stickers |
| **Thu Nov 6** | Place the stickers on the face | Project write-ups and screenshots |
| **Fri Nov 7** | First test export, then load in the site (**checkpoint: head + eyes working**) | Replace Sen's content with mine |
| **Sat Nov 8** | Empties `focus-0…5` and `focus-works` | Colours and fonts (my own look) |
| **Sun Nov 9** | `CameraAction` keyframes and easing. Export | Hook up the camera stops to the résumé entries |
| **Mon Nov 10** | Tune the camera path in the browser | Projects gallery and detail pages |
| **Tue Nov 11** | Lighting and look pass | Grad touches (cap, "open to roles" stamp) |
| **Wed Nov 12** | Optimize the `.glb` file size | Mobile check, loading screen, résumé PDF link |
| **Thu Nov 13** | — | **Deploy to GitHub Pages**. Test on phone and laptop |
| **Fri Nov 14** | Buffer | Get feedback from 2–3 friends and fix issues |
| **Sat Nov 15** | **Launch** | Optional: custom domain |

**Risk:** 15 days is tight for a Blender beginner. Nov 7 is the go/no-go checkpoint. If the scanned head isn't in the browser by then, switch to the stylized-head fallback so the deadline holds.

## 8. Assets checklist (from Talha)

- [ ] Head scan (or photos for reference if sculpting)
- [ ] 1–2 regular photos (About section / social preview image)
- [ ] Sticker art or ideas (section 3)
- [ ] 5 résumé entries: title, place, dates, one line each
- [ ] 3–5 projects: title, summary, images, links
- [ ] Résumé PDF
- [ ] Links: LinkedIn, GitHub, email
- [ ] Graduation month and the roles I'm targeting
