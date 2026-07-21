"""
Baseline experiment run (ORIGINAL weights: genre +3.0, mood +2.0,
energy up to +2.0, acoustic up to +1.0).

Runs the recommender for three reference profiles -- EDM, Chill Lo-fi, and
Rock/Alternative -- and writes the captured terminal output to
experiments/baseline_profiles_results.md so it can be compared against a
later weight-tuning phase.

Run from the project root:  python experiments/run_baseline_profiles.py
"""

import io
import os
import sys
from contextlib import redirect_stdout

# Ensure the project root is importable no matter where this is launched from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import print_recommendations
from src.recommender import load_songs, recommend_songs

RESULTS_PATH = "experiments/baseline_profiles_results.md"

# (label, user_prefs)
PROFILES = [
    ("EDM (high energy)",
     {"genre": "edm", "mood": "energetic", "target_energy": 0.95, "likes_acoustic": False}),
    ("Chill Lo-fi",
     {"genre": "lofi", "mood": "chill", "target_energy": 0.35, "likes_acoustic": True}),
    ("Rock / Alternative",
     {"genre": "rock", "mood": "intense", "target_energy": 0.90, "likes_acoustic": False}),
]


def main() -> None:
    songs = load_songs("data/songs.csv")

    blocks = []
    for label, prefs in PROFILES:
        buf = io.StringIO()
        with redirect_stdout(buf):
            recs = recommend_songs(prefs, songs, k=5)
            print_recommendations(prefs, recs)
        output = buf.getvalue()
        # Echo to the real terminal too.
        print(f"\n===== {label} =====")
        print(output)
        blocks.append((label, prefs, output))

    lines = [
        "# Baseline Profile Results (original weights)",
        "",
        "**Scoring weights:** genre +3.0 | mood +2.0 | energy up to +2.0 "
        "(closeness) | acousticness up to +1.0",
        "",
        "Reference run captured before any weight-tuning experiment, so a later "
        "phase can be compared against it. Regenerate with "
        "`python experiments/run_baseline_profiles.py`.",
        "",
    ]
    for label, prefs, output in blocks:
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"**Profile:** `{prefs}`")
        lines.append("")
        lines.append("```")
        lines.append(output.rstrip("\n"))
        lines.append("```")
        lines.append("")

    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nSaved results to {RESULTS_PATH}")


if __name__ == "__main__":
    main()
