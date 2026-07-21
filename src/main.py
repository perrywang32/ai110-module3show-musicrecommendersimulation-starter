"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

# Width of the divider lines. Kept as a constant so the layout is easy to tweak.
WIDTH = 60


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Print the ranked recommendations in a clean, readable layout."""
    print()
    print("=" * WIDTH)
    print("  TOP MUSIC RECOMMENDATIONS".ljust(WIDTH))
    print("=" * WIDTH)

    # Show which preferences produced these results.
    profile = "  |  ".join(f"{key}: {value}" for key, value in user_prefs.items())
    print(f"For profile -> {profile}")
    print("=" * WIDTH)

    if not recommendations:
        print("\n  No matching songs found.\n")
        print("=" * WIDTH)
        return

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print()
        print(f"  #{rank}  {song['title']}")
        print(f"      Artist : {song['artist']}")
        print(f"      Score  : {score:.2f}")
        print(f"      Reasons:")
        for reason in reasons:
            print(f"        - {reason}")
        print("-" * WIDTH)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(user_prefs, recommendations)


if __name__ == "__main__":
    main()
