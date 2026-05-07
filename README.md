# Vision Playground

An interactive browser-based eye training app built with vanilla HTML, CSS, and JavaScript — no dependencies, no install.

**Live site:** https://priyanka-mondal.github.io/vision-playground/

---

## Exercises

### General Eye Training

| Exercise | Description |
|---|---|
| **Smooth Pursuit** | Follow a smoothly moving dot with your eyes without moving your head. Trains smooth pursuit eye movements. |
| **Saccades** | Jump your gaze as quickly as possible between highlighted targets. Trains fast, accurate eye movements. |
| **Figure 8** | Trace a figure-eight path with your eyes while keeping your head still. |
| **Focus Shift** | Alternate between a near dot and a far target, holding each for 2 seconds. Trains accommodation (focus flexibility). |
| **20-20-20 Timer** | Guided timer for the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds. Reduces digital eye strain. |
| **Palming Relaxation** | Cover your eyes with your palms and breathe deeply. Relieves tension after screen time. |

---

### RDS Stereogram (Red-Green Glasses Required)

These exercises use **red-green anaglyph glasses** (red lens on left eye, green lens on right eye). They train binocular vision, vergence, and stereoscopic depth perception.

#### Position Game
A random-dot stereogram with a 3D circle hidden in one of four positions (up / down / left / right). Press **↑ ↓ ← →** to identify where the circle appears to float in depth. You have 30 seconds — score as many correct answers as possible.

#### Convergence Test
Two large random-dot circles (red for the left eye, green for the right eye) drift apart by **0.5 prism diopters (Δ)** every few seconds. Fuse the two circles into one through your glasses. Press **SPACE** the moment you lose fusion. The app records your maximum convergence amplitude in diopters.

#### Combined Test
The circles separate progressively (0.5Δ every 10 seconds) while a hidden 3D circle appears somewhere inside the fused area. During each 10-second window:
- Press **↑ ↓ ← →** to identify the hidden circle's position
- A correct answer immediately advances to the next diopter level
- Press **SPACE** when you lose fusion to end the session

Tracks your history of correct responses across diopter levels.

---

### Convergence Rings
Wear red-green glasses and converge or diverge your eyes until the two outline rings fuse into one. A hidden number appears inside when fused correctly. Useful for basic vergence check.

---

## How to Use

1. Open https://priyanka-mondal.github.io/vision-playground/ in any modern browser
2. Click a tab in the top navigation to switch exercises
3. For RDS exercises, wear **red-green anaglyph glasses** (red lens on left)

No account, no installation, no data collection.

---

## Running Locally

Just open `index.html` in a browser — it is a single self-contained file.

```bash
git clone https://github.com/Priyanka-Mondal/vision-playground.git
cd vision-playground
open index.html   # macOS
# or double-click index.html on Windows/Linux
```

---

## Technical Notes

- Single HTML file — all CSS and JavaScript inline, zero dependencies
- Canvas-based rendering with `createImageData` for pixel-level dot manipulation
- Dynamically sized canvases via `ResizeObserver` — works on any screen size
- RDS dots rendered per-frame with random seed for fresh patterns on every draw
- Diopter-to-pixel conversion is configurable via an in-app slider (px per 0.5Δ)
