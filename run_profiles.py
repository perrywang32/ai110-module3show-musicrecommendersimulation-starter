"""
Test driver: runs the recommender against several diverse user profiles
so we can inspect ranking behavior and edge cases.

Run from the project root:  python run_profiles.py
"""

from src.main import print_recommendations
from src.recommender import load_songs, recommend_songs

# Each entry: (label, why-it-matters, user_prefs)
PROFILES = [
    (
        "High-energy EDM",
        "Happy-path check that genre + mood + high target_energy all align "
        "and push genuine EDM tracks to the top.",
        {"genre": "edm", "mood": "energetic", "target_energy": 0.95, "likes_acoustic": False},
    ),
    (
        "Chill lo-fi",
        "Low-energy, acoustic-leaning taste. Verifies the energy-closeness "
        "and acousticness terms reward calm songs instead of loud ones.",
        {"genre": "lofi", "mood": "chill", "target_energy": 0.35, "likes_acoustic": True},
    ),
    (
        "Rock / intense",
        "A guitar-driven, high-energy but NON-electronic taste. Checks that "
        "the scorer separates rock from EDM even though both are high-energy.",
        {"genre": "rock", "mood": "intense", "target_energy": 0.90, "likes_acoustic": False},
    ),
    (
        "Adversarial / conflicting",
        "Every signal fights every other: favorite genre is metal (loud, "
        "non-acoustic, fast) yet the user asks for a chill mood, near-zero "
        "energy, and acoustic songs. Exposes how a single +3.0 genre match "
        "can dominate a profile whose other four signals all disagree.",
        {"genre": "metal", "mood": "chill", "target_energy": 0.10, "likes_acoustic": True},
    ),
]


def main() -> None:
    songs = load_songs("data/songs.csv")
    for label, _why, prefs in PROFILES:
        print()
        print("#" * 60)
        print(f"#  PROFILE: {label}")
        print("#" * 60)
        recs = recommend_songs(prefs, songs, k=5)
        print_recommendations(prefs, recs)


if __name__ == "__main__":
    main()
