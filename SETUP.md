# Setup: get the site running on your laptop

This takes about 30–45 minutes the first time. Do the steps in order.

## 1. Install the tools

| Tool | What it's for | Get it |
|---|---|---|
| **Git** | Downloads the project and saves your changes | git-scm.com (Mac: run `git --version` in Terminal and it offers to install) |
| **Node.js 20 or newer** (the LTS version) | Runs the website on your laptop | nodejs.org |
| **Blender 5.2 LTS** | 3D work | blender.org. **Use 5.2 or newer**, because older versions can't open `placeholder.blend` |
| **VS Code** (optional) | Editing code | code.visualstudio.com |

Check that it worked. Open **Terminal** (Mac) or **PowerShell** (Windows) and run:

```bash
git --version
node --version     # should print v20 or higher
```

## 2. Download the project

```bash
git clone https://github.com/talha397/Portofolio.git
cd Portofolio
git checkout plan/checklist      # the branch with our work so far
```

## 3. Run the website

```bash
cd web
npm install        # first time only: downloads libraries into web/node_modules (takes a minute)
npm run dev
```

Open **http://localhost:5173** in your browser. You should see the placeholder head with a graduation cap. Move your mouse and the eyes follow it. Scroll and the camera flies to each sticker.

To stop the site, press `Ctrl + C` in the terminal. To start it again later, run `npm run dev` from inside `web/`.

## 4. Make your first change (2 minutes)

1. With `npm run dev` still running, open `web/src/App.tsx`.
2. Find `COPY` near the top and replace the `[One or two sentences…]` text with anything.
3. Save. The browser updates by itself. That's the whole edit loop.

## 5. Open the 3D scene

1. Open Blender, then **File → Open → `blender/placeholder.blend`**.
2. In the **Outliner** (the list at top right), find:
   - `Camera`: press **Space** to play its animation. Frames 0, 50, 100, 150, 200 and 250 are the stops.
   - `focus-0` … `focus-5`, `focus-works`: the points the camera looks at
   - `eye_L`, `eye_R`: the googly eyes. The website finds them because their names contain "eye".
   - `head`: the part that gets replaced by your scan later
3. Don't save over `placeholder.blend`. Use **File → Save As → `blender/talha.blend`** and do your own work there.

## Where things live

| I want to change… | Edit |
|---|---|
| About text | `COPY` in `web/src/App.tsx` |
| Name and corner labels on the first screen | `hero-meta` lines in `web/src/App.tsx` |
| Résumé entries and links | `RESUME` and `SOCIAL_LINKS` in `web/src/ui/Resume.tsx` |
| Projects list | `web/src/data/works.ts` |
| A project's detail page | `web/src/content/works/<slug>.md` (copy `example.md`) |
| Colours, blur, lights | Constants at the top of each part of `web/src/scene/Scene.tsx` |
| The 3D model | Export from Blender to `web/public/models/me.glb` |

**Blender export settings** (File → Export → glTF 2.0): Format **glTF Binary (.glb)**. Include: **Cameras** ✅. Transform: **+Y Up** ✅. Animation ✅. Save over `web/public/models/me.glb`, then refresh the browser.

## Stuck?

- `npm: command not found` → Node isn't installed, or the terminal was open before you installed it. Close and reopen the terminal.
- Blank page → check the terminal running `npm run dev` for red errors, and paste them to Claude.
- Model doesn't update after export → hard-refresh the browser (`Cmd+Shift+R` / `Ctrl+Shift+R`).
