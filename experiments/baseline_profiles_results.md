# Baseline Profile Results (original weights)

**Scoring weights:** genre +3.0 | mood +2.0 | energy up to +2.0 (closeness) | acousticness up to +1.0

Reference run captured before any weight-tuning experiment, so a later phase can be compared against it. Regenerate with `python experiments/run_baseline_profiles.py`.

## EDM (high energy)

**Profile:** `{'genre': 'edm', 'mood': 'energetic', 'target_energy': 0.95, 'likes_acoustic': False}`

```

============================================================
  TOP MUSIC RECOMMENDATIONS                                 
============================================================
For profile -> genre: edm  |  mood: energetic  |  target_energy: 0.95  |  likes_acoustic: False
============================================================

  #1  Neon Warehouse
      Artist : Pulse Divide
      Score  : 7.98
      Reasons:
        - Genre 'edm' matches your favorite (+3.0)
        - Mood 'energetic' matches your favorite (+2.0)
        - Energy 0.95 vs target 0.95 (+2.00)
        - Acousticness 0.02 (you prefer non-acoustic) (+0.98)
------------------------------------------------------------

  #2  Skyline Anthem
      Artist : Martin Garrix
      Score  : 7.90
      Reasons:
        - Genre 'edm' matches your favorite (+3.0)
        - Mood 'energetic' matches your favorite (+2.0)
        - Energy 0.92 vs target 0.95 (+1.94)
        - Acousticness 0.04 (you prefer non-acoustic) (+0.96)
------------------------------------------------------------

  #3  Detonate
      Artist : ISOKNOCK
      Score  : 5.96
      Reasons:
        - Genre 'edm' matches your favorite (+3.0)
        - Mood 'intense' is not your favorite 'energetic' (+0.0)
        - Energy 0.96 vs target 0.95 (+1.98)
        - Acousticness 0.02 (you prefer non-acoustic) (+0.98)
------------------------------------------------------------

  #4  Wreckage
      Artist : Crankdat
      Score  : 5.95
      Reasons:
        - Genre 'edm' matches your favorite (+3.0)
        - Mood 'intense' is not your favorite 'energetic' (+0.0)
        - Energy 0.97 vs target 0.95 (+1.96)
        - Acousticness 0.01 (you prefer non-acoustic) (+0.99)
------------------------------------------------------------

  #5  Afterglow Skies
      Artist : Illenium
      Score  : 5.38
      Reasons:
        - Genre 'edm' matches your favorite (+3.0)
        - Mood 'uplifting' is not your favorite 'energetic' (+0.0)
        - Energy 0.78 vs target 0.95 (+1.66)
        - Acousticness 0.28 (you prefer non-acoustic) (+0.72)
------------------------------------------------------------
```

## Chill Lo-fi

**Profile:** `{'genre': 'lofi', 'mood': 'chill', 'target_energy': 0.35, 'likes_acoustic': True}`

```

============================================================
  TOP MUSIC RECOMMENDATIONS                                 
============================================================
For profile -> genre: lofi  |  mood: chill  |  target_energy: 0.35  |  likes_acoustic: True
============================================================

  #1  Library Rain
      Artist : Paper Lanterns
      Score  : 7.86
      Reasons:
        - Genre 'lofi' matches your favorite (+3.0)
        - Mood 'chill' matches your favorite (+2.0)
        - Energy 0.35 vs target 0.35 (+2.00)
        - Acousticness 0.86 (you like acoustic) (+0.86)
------------------------------------------------------------

  #2  Midnight Coding
      Artist : LoRoom
      Score  : 7.57
      Reasons:
        - Genre 'lofi' matches your favorite (+3.0)
        - Mood 'chill' matches your favorite (+2.0)
        - Energy 0.42 vs target 0.35 (+1.86)
        - Acousticness 0.71 (you like acoustic) (+0.71)
------------------------------------------------------------

  #3  Focus Flow
      Artist : LoRoom
      Score  : 5.68
      Reasons:
        - Genre 'lofi' matches your favorite (+3.0)
        - Mood 'focused' is not your favorite 'chill' (+0.0)
        - Energy 0.40 vs target 0.35 (+1.90)
        - Acousticness 0.78 (you like acoustic) (+0.78)
------------------------------------------------------------

  #4  Spacewalk Thoughts
      Artist : Orbit Bloom
      Score  : 4.78
      Reasons:
        - Genre 'ambient' is not your favorite 'lofi' (+0.0)
        - Mood 'chill' matches your favorite (+2.0)
        - Energy 0.28 vs target 0.35 (+1.86)
        - Acousticness 0.92 (you like acoustic) (+0.92)
------------------------------------------------------------

  #5  Paper Boats
      Artist : Hazel Grove
      Score  : 2.87
      Reasons:
        - Genre 'folk' is not your favorite 'lofi' (+0.0)
        - Mood 'dreamy' is not your favorite 'chill' (+0.0)
        - Energy 0.33 vs target 0.35 (+1.96)
        - Acousticness 0.91 (you like acoustic) (+0.91)
------------------------------------------------------------
```

## Rock / Alternative

**Profile:** `{'genre': 'rock', 'mood': 'intense', 'target_energy': 0.9, 'likes_acoustic': False}`

```

============================================================
  TOP MUSIC RECOMMENDATIONS                                 
============================================================
For profile -> genre: rock  |  mood: intense  |  target_energy: 0.9  |  likes_acoustic: False
============================================================

  #1  Storm Runner
      Artist : Voltline
      Score  : 7.88
      Reasons:
        - Genre 'rock' matches your favorite (+3.0)
        - Mood 'intense' matches your favorite (+2.0)
        - Energy 0.91 vs target 0.90 (+1.98)
        - Acousticness 0.10 (you prefer non-acoustic) (+0.90)
------------------------------------------------------------

  #2  Gym Hero
      Artist : Max Pulse
      Score  : 4.89
      Reasons:
        - Genre 'pop' is not your favorite 'rock' (+0.0)
        - Mood 'intense' matches your favorite (+2.0)
        - Energy 0.93 vs target 0.90 (+1.94)
        - Acousticness 0.05 (you prefer non-acoustic) (+0.95)
------------------------------------------------------------

  #3  Detonate
      Artist : ISOKNOCK
      Score  : 4.86
      Reasons:
        - Genre 'edm' is not your favorite 'rock' (+0.0)
        - Mood 'intense' matches your favorite (+2.0)
        - Energy 0.96 vs target 0.90 (+1.88)
        - Acousticness 0.02 (you prefer non-acoustic) (+0.98)
------------------------------------------------------------

  #4  Wreckage
      Artist : Crankdat
      Score  : 4.85
      Reasons:
        - Genre 'edm' is not your favorite 'rock' (+0.0)
        - Mood 'intense' matches your favorite (+2.0)
        - Energy 0.97 vs target 0.90 (+1.86)
        - Acousticness 0.01 (you prefer non-acoustic) (+0.99)
------------------------------------------------------------

  #5  Circuit Breaker
      Artist : Tempo Fault
      Score  : 2.97
      Reasons:
        - Genre 'drum and bass' is not your favorite 'rock' (+0.0)
        - Mood 'tense' is not your favorite 'intense' (+0.0)
        - Energy 0.90 vs target 0.90 (+2.00)
        - Acousticness 0.03 (you prefer non-acoustic) (+0.97)
------------------------------------------------------------
```
