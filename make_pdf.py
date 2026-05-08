from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "Vision_Playground_Exercises.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.85*inch,
    rightMargin=0.85*inch,
    topMargin=0.9*inch,
    bottomMargin=0.9*inch,
)

styles = getSampleStyleSheet()

# ── custom styles ──────────────────────────────────────────────────────────────
DARK   = colors.HexColor("#0d1117")
BLUE   = colors.HexColor("#58a6ff")
GREY   = colors.HexColor("#8b949e")
LIGHT  = colors.HexColor("#e6edf3")
GREEN  = colors.HexColor("#3fb950")
PURPLE = colors.HexColor("#8957e5")

title_style = ParagraphStyle("DocTitle",
    fontSize=26, leading=32, textColor=BLUE,
    fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4)

subtitle_style = ParagraphStyle("Subtitle",
    fontSize=11, textColor=GREY,
    fontName="Helvetica", alignment=TA_CENTER, spaceAfter=20)

section_style = ParagraphStyle("Section",
    fontSize=16, leading=20, textColor=PURPLE,
    fontName="Helvetica-Bold", spaceBefore=18, spaceAfter=6)

ex_title_style = ParagraphStyle("ExTitle",
    fontSize=13, leading=16, textColor=BLUE,
    fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=3)

body_style = ParagraphStyle("Body",
    fontSize=10, leading=15, textColor=colors.HexColor("#24292f"),
    fontName="Helvetica", spaceAfter=4)

label_style = ParagraphStyle("Label",
    fontSize=9, leading=13, textColor=GREY,
    fontName="Helvetica-Bold", spaceAfter=2)

detail_style = ParagraphStyle("Detail",
    fontSize=9, leading=13, textColor=colors.HexColor("#24292f"),
    fontName="Helvetica", spaceAfter=2, leftIndent=10)

tip_style = ParagraphStyle("Tip",
    fontSize=9, leading=13, textColor=colors.HexColor("#1a7f37"),
    fontName="Helvetica-Oblique", leftIndent=10, spaceAfter=6)

def hr():
    return HRFlowable(width="100%", thickness=0.5,
                      color=colors.HexColor("#d0d7de"), spaceAfter=6, spaceBefore=2)

def section(title):
    return [Paragraph(title, section_style), hr()]

def exercise(title, description, controls=None, goal=None, tip=None):
    items = [Paragraph(title, ex_title_style),
             Paragraph(description, body_style)]
    if controls:
        items.append(Paragraph("Controls:", label_style))
        for c in controls:
            items.append(Paragraph(f"• {c}", detail_style))
    if goal:
        items.append(Paragraph("Goal:", label_style))
        items.append(Paragraph(goal, detail_style))
    if tip:
        items.append(Paragraph(f"💡 {tip}", tip_style))
    items.append(Spacer(1, 4))
    return items

intro_style = ParagraphStyle("Intro",
    fontSize=10.5, leading=17, textColor=colors.HexColor("#24292f"),
    fontName="Helvetica", spaceAfter=10)

intro_italic = ParagraphStyle("IntroItalic",
    fontSize=10.5, leading=17, textColor=colors.HexColor("#24292f"),
    fontName="Helvetica-Oblique", spaceAfter=10)

# ── document content ───────────────────────────────────────────────────────────
story = []

story.append(Paragraph("Vision Playground", title_style))
story.append(Paragraph(
    "<highlight>A collection of interactive eye training exercises · "
    "<a href='https://priyanka-mondal.github.io/vision-playground' color='#58a6ff'>"
    "priyanka-mondal.github.io/vision-playground</a></highlight>",
    subtitle_style))
story.append(Paragraph("Author: Priyanka Mondal", ParagraphStyle("Author",
    fontSize=14, textColor=GREY, fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=16)))
story.append(hr())
story.append(Spacer(1, 10))

# ── Personal background ────────────────────────────────────────────────────────
story += section("About This Project")

story.append(Paragraph(
    "I have been dealing with <b>double vision (diplopia)</b> since childhood. It is something "
    "I have lived with for as long as I can remember — the world sometimes appears as two "
    "overlapping images, making everyday tasks like reading, driving, and screen time more "
    "tiring than they should be.",
    intro_style))

story.append(Paragraph(
    "Over the years I have gone through <b>vision therapy</b> and tried many different eye "
    "exercises — some recommended by my vision doctor, others I discovered on my own through "
    "research. Some of them genuinely helped. They improved my ability to fuse images, increased "
    "my convergence range, and reduced the fatigue I felt after long hours of work.",
    intro_style))

story.append(Paragraph(
    "To make things easier for myself — and for others who might be in a similar situation — "
    "I built <b>Vision Playground</b>. It brings all the science-backed exercises I found "
    "useful into one place: free, browser-based, and always available. No appointments, "
    "no expensive equipment, no subscriptions.",
    intro_style))

story.append(Paragraph(
    "The only prop you will ever need is a pair of <b>red-green anaglyph glasses</b> — the "
    "kind that cost a few dollars on Amazon.com. These unlock the more advanced "
    "RDS (Random Dot Stereogram) exercises, which are specifically designed to train "
    "binocular fusion and stereoscopic depth perception. If you are just starting out, "
    "begin with the no-glasses exercises (the website is at "
    "<a href='https://priyanka-mondal.github.io/vision-playground' color='#58a6ff'>"
    "Vision Playground</a>) and build up from there. "
    "Get the glasses only when "
    "you feel ready to move to the advanced levels.",
    intro_style))

story.append(Paragraph(
    "I hope this helps you as much as it has helped me.",
    intro_italic))

story.append(Spacer(1, 10))
story.append(hr())
story.append(Spacer(1, 6))

# ── RDS Stereogram ─────────────────────────────────────────────────────────────
story += section("🔴🟢  RDS Stereogram Exercises  (Red-Green Glasses Required)")

story.append(Paragraph(
    "These exercises use <b>red-green anaglyph glasses</b> (red lens on the left eye, green lens on "
    "the right eye). They train binocular vision, vergence, and stereoscopic depth perception. The "
    "random-dot patterns are generated fresh every 4 seconds so you cannot memorise the image.",
    body_style))
story.append(Spacer(1, 6))

story += exercise(
    "🎮  Position Game",
    "A random-dot stereogram fills a large circle. Hidden inside is a smaller circle that appears "
    "to float at a different depth. The hidden circle is placed in one of four positions — "
    "top, bottom, left, or right — relative to the centre of the fused image. "
    "You have 30 seconds to score as many correct identifications as possible.",
    controls=[
        "↑ ↓ ← →  — identify where the 3D circle appears to float",
        "Start Game button — begin a new 30-second round",
    ],
    goal="Score as many correct answers as possible within 30 seconds. "
         "Each correct answer adds 1 point and a green flash confirms it.",
    tip="Keep both eyes open and relaxed. The hidden circle pops out in depth once your "
        "visual system finds the binocular match — this can take a few seconds."
)

story += exercise(
    "📏  Convergence Test",
    "Two large random-dot circles — one rendered in red (left eye) and one in green (right eye) — "
    "start overlapping and slowly drift apart by 0.5 prism diopters (Δ) every few seconds. "
    "While wearing your anaglyph glasses, fuse the two circles into one by adjusting your eye "
    "vergence. Press SPACE the moment you can no longer hold fusion. "
    "The app records your maximum convergence amplitude.",
    controls=[
        "SPACE — signal that fusion is lost; records the current diopter level",
        "Start button — begin a new convergence measurement session",
    ],
    goal="Push your binocular fusion as far as possible. Your maximum fused diopter is saved "
         "so you can track improvement over multiple sessions.",
    tip="Relax your eyes rather than straining — forced vergence fatigues faster. "
        "Try again after a short rest to see if your range improves."
)

story += exercise(
    "🔬  Combined Test",
    "The most demanding exercise. The two circles drift apart by 0.5Δ every 10 seconds "
    "(increasing vergence demand), while a hidden 3D circle is simultaneously present inside "
    "each circle at the same relative position. You must maintain fusion of the two big circles "
    "AND identify the position of the hidden element within each 10-second window. "
    "A correct answer immediately advances to the next diopter level. "
    "The dot pattern refreshes every 4 seconds to keep the task challenging.",
    controls=[
        "↑ ↓ ← →  — identify the hidden circle's position (top / bottom / left / right)",
        "SPACE — signal fusion lost; ends the session and shows your results",
        "Start button — begin at 0Δ and advance automatically",
    ],
    goal="Reach the highest diopter level while maintaining fusion. "
         "Your score (correct answers) and max fused diopter are displayed after each session.",
    tip="The hidden circle is at the same quadrant position within each big circle. "
        "When fused correctly, it appears clearly offset from centre in one direction. "
        "Use the faint arrow hints on screen as a spatial reference."
)

story.append(Spacer(1, 4))

# ── General Eye Training ───────────────────────────────────────────────────────
story += section("👁  General Eye Training Exercises")

story.append(Paragraph(
    "These exercises require no special glasses and can be done anytime to reduce eye strain, "
    "improve eye muscle control, and build visual stamina.",
    body_style))
story.append(Spacer(1, 4))

story += exercise(
    "Smooth Pursuit",
    "A dot moves smoothly around the screen in a circular or figure-eight path. "
    "Track it with your eyes while keeping your head completely still.",
    controls=["Start / Stop button — begin or pause the exercise"],
    goal="Maintain smooth, continuous eye movement that exactly follows the dot. "
         "Avoid jerky catch-up movements.",
    tip="If you find yourself moving your head, place your chin on your fist as a reminder."
)

story += exercise(
    "Saccade Training",
    "Multiple targets appear on screen and one is highlighted at a time. "
    "Shift your gaze as quickly and accurately as possible to each newly highlighted target.",
    controls=["Start / Stop button — begin a session"],
    goal="Minimise reaction time between target changes. "
         "Saccades are the fast eye movements used in reading and scene scanning.",
    tip="Look directly at the centre of each target rather than the surrounding area."
)

story += exercise(
    "Figure 8",
    "Trace an imaginary figure-eight (∞) path with your eyes, following the on-screen guide. "
    "Keep your head still throughout.",
    controls=["Start / Stop button"],
    goal="Complete smooth, symmetrical loops in both directions, training all six extra-ocular muscles.",
    tip="Go slowly at first. Speed is less important than keeping the path smooth and continuous."
)

story += exercise(
    "Focus Shift",
    "Alternate between focusing on a near dot (close to your face) and a far text target "
    "on the screen. Hold each focus for 2 seconds before switching.",
    controls=["Start button — begin the timed alternation cycle"],
    goal="Train the ciliary muscles that control lens accommodation (focus adjustment). "
         "Particularly useful for people who spend long hours looking at screens.",
    tip="Hold a finger close to your nose as the near target if the on-screen dot is too far."
)

story += exercise(
    "20-20-20 Timer",
    "A guided countdown reminder for the 20-20-20 rule: every 20 minutes of screen time, "
    "look at something at least 20 feet away for 20 seconds.",
    controls=["Start button — begin the 20-minute work countdown"],
    goal="Reduce digital eye strain by giving your accommodation system regular breaks.",
    tip="Set this running whenever you start a work session and follow every rest prompt."
)

story += exercise(
    "Palming Relaxation",
    "Cup your palms gently over your closed eyes without pressing on them, blocking all light. "
    "Breathe slowly and deeply, and let your eyes rest in complete darkness.",
    controls=["Start button — begins a timed relaxation session"],
    goal="Release tension in the eye muscles and the visual cortex. "
         "Best done after any of the more demanding exercises.",
    tip="Visualise a peaceful dark space rather than trying to see anything. "
        "Even 2 minutes of palming can noticeably reduce eye fatigue."
)

story.append(Spacer(1, 6))

# ── Convergence Rings ──────────────────────────────────────────────────────────
story += section("⭕  Convergence Rings  (Red-Green Glasses Required)")

story += exercise(
    "Convergence Rings",
    "Two outline rings are displayed — one red, one green — at a fixed separation. "
    "Wear your red-green anaglyph glasses and adjust your eye vergence until the two rings "
    "fuse into a single ring. A hidden number appears inside when you achieve correct fusion.",
    controls=["Visual only — adjust vergence by relaxing or converging your eyes"],
    goal="Successfully fuse the two rings and read the hidden number. "
         "Use as a quick binocular check before the more demanding RDS sessions.",
    tip="Start by looking slightly beyond the screen (diverge) rather than crossing your eyes. "
        "The number will snap into focus once fusion is achieved."
)

story.append(Spacer(1, 10))
story.append(hr())
story.append(Paragraph(
    "Vision Playground · https://priyanka-mondal.github.io/vision-playground · Open source",
    ParagraphStyle("Footer", fontSize=8, textColor=GREY, alignment=TA_CENTER)))

doc.build(story)
print(f"PDF written to {OUTPUT}")
