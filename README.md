# ABYSS RUN — Into the Blue

A playable underwater survival/exploration game using HTML Canvas, CSS, JavaScript, Flask and SQLite.

## Features
- Animated deep-ocean scene, light rays, bubbles, fish and sea plants
- Diver movement with keyboard and touch controls
- Oxygen and suit integrity meters
- Collect oxygen canisters and treasure
- Avoid sharks and jellyfish
- Find the research beacon and rescue the lost diver
- Pause, restart, sound toggle and SQLite high-score leaderboard

## Run on Windows
Open PowerShell in the folder containing `app.py`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Open **http://127.0.0.1:5000/** in Chrome or Edge. Do not use Live Server for `index.html`; Flask must serve the page.

## Controls
- W / Up: swim up
- S / Down: swim down
- A / Left: swim left
- D / Right: swim right
- Space: boost
- Esc: pause / resume

Collect the beacon and rescue capsule to complete the mission. Oxygen tanks refill oxygen; treasure increases score. Sharks and jellyfish damage your suit.


## Deploy publicly (Render)

1. Upload this project folder to a GitHub repository (keep `app.py`, `requirements.txt`,
   `render.yaml`, `templates/`, and `static/` at the repository root).
2. Sign in to Render and choose **New + → Blueprint**.
3. Connect the GitHub repository containing this project.
4. Render detects `render.yaml`; choose **Apply** and wait for deployment.
5. Open the `https://...onrender.com` URL Render gives you and share it with your class group.

The game itself runs on Render. The SQLite leaderboard uses the service filesystem;
on a free instance, saved scores may be lost when the instance is replaced/redeployed.
