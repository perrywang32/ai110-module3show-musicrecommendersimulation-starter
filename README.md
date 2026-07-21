# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project implements a simple music recommendation system that suggests songs based on a user's preferences. Each song is scored using features such as genre, mood, energy, and acousticness, then ranked from highest to lowest score. The project demonstrates how recommendation systems use weighted features to personalize suggestions while also highlighting the limitations and potential biases of rule-based recommenders.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My music recommendation system compares a user's preferences with the attributes of every song in the dataset. Each Song contains features such as genre, mood, energy, and acousticness. The UserProfile stores the user's favorite genre, favorite mood, target energy level, and acousticness preference. The recommender reads every song from songs.csv and calculates a score based on how closely each song matches the user's preferences. Genre is weighted the most because it represents the overall style of music, followed by mood. Energy is scored using a closeness formula, so songs with energy levels nearest the user's target receive more points. Acousticness is used as a smaller preference to help break ties. After every song is scored, the system sorts the songs from highest to lowest score and recommends the top results. This is a simplified version of how streaming services personalize recommendations for users.

Algorithm Recipe
* Read the user's preferences.
* Load every song from songs.csv.
* Compare the song's genre with the user's favorite genre.
* Compare the song's mood with the user's favorite mood.
* Award points based on how close the song's energy is to     the user's target energy.
* Award points based on whether the song matches the user's acousticness preference.
* Add the points together to calculate the song's total score.
* Repeat for every song.
* Sort all songs by score.
* Recommend the Top K highest-scoring songs.

Potential Biases

This recommender may over-prioritize genre, causing songs from other genres that closely match the user's mood or energy to receive lower scores. It also depends on manually chosen weights, which may not reflect every user's listening habits. Real recommendation systems reduce these biases by learning from large amounts of user behavior and continuously adjusting their models.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Running `python -m src.main` with the profile `genre=pop, mood=happy, energy=0.8`
against the 24-song catalog produces:

```
Loaded 24 songs from data/songs.csv

============================================================
  TOP MUSIC RECOMMENDATIONS
============================================================
For profile -> genre: pop  |  mood: happy  |  energy: 0.8
============================================================

  #1  Sunrise City
      Artist : Neon Echo
      Score  : 6.96
      Reasons:
        - Genre 'pop' matches your favorite (+3.0)
        - Mood 'happy' matches your favorite (+2.0)
        - Energy 0.82 vs target 0.80 (+1.96)
------------------------------------------------------------

  #2  Gym Hero
      Artist : Max Pulse
      Score  : 4.74
      Reasons:
        - Genre 'pop' matches your favorite (+3.0)
        - Mood 'intense' is not your favorite 'happy' (+0.0)
        - Energy 0.93 vs target 0.80 (+1.74)
------------------------------------------------------------

  #3  Rooftop Lights
      Artist : Indigo Parade
      Score  : 3.92
      Reasons:
        - Genre 'indie pop' is not your favorite 'pop' (+0.0)
        - Mood 'happy' matches your favorite (+2.0)
        - Energy 0.76 vs target 0.80 (+1.92)
------------------------------------------------------------

  #4  Basement Groove
      Artist : Funk Factory
      Score  : 2.00
      Reasons:
        - Genre 'funk' is not your favorite 'pop' (+0.0)
        - Mood 'playful' is not your favorite 'happy' (+0.0)
        - Energy 0.80 vs target 0.80 (+2.00)
------------------------------------------------------------

  #5  Afterglow Skies
      Artist : Illenium
      Score  : 1.96
      Reasons:
        - Genre 'edm' is not your favorite 'pop' (+0.0)
        - Mood 'uplifting' is not your favorite 'happy' (+0.0)
        - Energy 0.78 vs target 0.80 (+1.96)
------------------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Below are the experiments I ran while building and tuning the recommender.

- **Closeness vs. magnitude for energy.** I confirmed the scorer rewards being *close* to the target energy, not simply having high energy. With a target of 0.80, "Basement Groove" (energy 0.80) earned the full +2.00 even though it isn't a pop song, while "Gym Hero" (energy 0.93) only earned +1.74 despite being *more* energetic. This is the intended behavior.
- **Case sensitivity in matching.** An early profile used capitalized values like `"EDM"` and `"Intense"`, but the CSV stores genres/moods in lowercase. A plain `==` check matched *nothing*, silently zeroing out genre and mood points. I fixed this by lowercasing both sides (`.lower()`) inside `score_song()`.
- **Mood-label mismatch.** With only one EDM song (labeled `energetic`), an "intense EDM" listener earned genre points but *no* mood points on their favorite genre — and "intense rock" nearly tied the EDM pick. Adding intense EDM tracks ("Detonate", "Wreckage") gave the profile real matches and fixed the ranking.
- **Growing the catalog (10 → 24 songs).** I added new genres (hip-hop, edm, r&b, metal, country, classical, reggae, funk, drum & bass, folk) and moods, plus a cluster of 5 EDM songs spanning intense → melodic. This let me test *intra-genre* ranking (does it order EDM songs correctly?) rather than only across-genre ranking.
- **Different user profiles.** Swapping the profile from `genre=pop, mood=happy` to `genre=edm, mood=intense` produced clearly different top-5 lists, confirming the recommendations are actually driven by the profile.

---

## Limitations and Risks

Limitations I identified in the current recommender:

- **Tiny catalog.** Only 24 songs, so results are not representative of a real music library.
- **Hand-authored feature values.** The energy, tempo, and acousticness numbers were written by hand (including songs styled after real artists), not measured from actual audio — so they're subjective and could be wrong.
- **Exact-match categorical scoring is brittle.** Genre and mood only score on an *exact* match. "indie pop" earns 0 against "pop", and "energetic" earns 0 against "intense", even though they're closely related. There's no partial credit for similar categories.
- **Unused data.** The catalog stores `tempo_bpm`, `valence`, and `danceability`, but the implemented scorer only uses genre, mood, energy, and acousticness. Artist similarity and popularity aren't scored at all yet.
- **No understanding of lyrics, language, or culture.** The system only sees numbers and short text labels.
- **Filter-bubble risk.** Because it rewards similarity to what the user already likes, it tends to recommend "more of the same" and rarely surprises the listener with genuine discovery.
- **Cold-start problem.** A brand-new user with no stated preferences, or a new song with missing/incorrect metadata, is hard to handle well.
- **Weights encode value judgments.** The point weights (genre +3, mood +2, energy +2, acoustic +1) are choices I made. Weighting genre highest, for example, assumes genre matters most — which may not be true for every listener.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



