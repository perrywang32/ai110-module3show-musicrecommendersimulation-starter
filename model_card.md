# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The clearest weakness I found is that genre and mood are scored on an *exact* string match, with no partial credit for closely related categories. During testing this meant a song labeled "indie pop" scored zero against a "pop" preference, and an "energetic" song scored zero against an "intense" preference, even though a listener would consider those nearly the same. This creates an unfair coverage gap: because 14 of the 17 genres in my dataset appear only once, a user whose favorite genre is a singleton (like folk or metal) can receive at most one true genre match, and the rest of their top-5 is filled by unrelated songs that merely happened to match on energy. In effect, users with mainstream-in-this-dataset tastes (EDM, high energy) get coherent recommendations, while users with underrepresented tastes get filler. The root cause is a scoring "cliff" — a near-miss category is treated identically to a completely unrelated one.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**Weight-shift experiment.** To see how sensitive the rankings were to my chosen weights, I ran a controlled experiment: I halved the genre weight (from +3.0 to +1.5) and doubled the energy weight (from a maximum of +2.0 to +4.0), while leaving mood (+2.0) and acousticness (up to +1.0) unchanged. I then reran the default profile (`genre=pop, mood=happy, energy=0.8`) and compared the top-5 against the original weights. The #1 pick, "Sunrise City," held its place and its score actually rose (6.96 → 7.42) because its near-perfect energy match now counted double. The most revealing change was a ranking flip at #2/#3: "Rooftop Lights" (indie pop, happy, energy 0.76) rose above "Gym Hero" (pop, intense, energy 0.93) — meaning a song that matched the *mood* and energy but missed the genre now outranked a song that matched the *genre* but missed the mood. This confirmed that my results are highly sensitive to weight choices, and that the weights encode a value judgment about whether genre loyalty or mood/energy "vibe" matters more. The trade-off was clear: emphasizing energy improved vibe-matching but weakened genre coherence, letting off-genre songs (like a funk track at exactly the target energy) climb into a "pop" list.

**Cross-profile comparison (EDM, pop, rock/alternative).** Using the original weights, I tested three profiles — an EDM listener (`edm, energetic, 0.95`), a pop listener (`pop, happy, 0.8`), and a rock/alternative listener (`rock, intense, 0.90`) — and looked at both the #1 pick and the overall coherence of the top-5. The saved outputs are in `experiments/baseline_profiles_results.md` and the README.

*What changed between the profiles:* the quality of the #1 recommendation was consistently strong (Neon Warehouse at 7.98 for EDM, Sunrise City at 6.96 for pop, Storm Runner at 7.88 for rock), but the coherence of the *rest* of the list varied dramatically with how many matching songs the catalog held. The EDM profile returned an all-EDM top-5 because the dataset has five EDM songs; the pop profile (only two pop songs) filled positions #4–#5 with a funk track and an EDM track; and the rock profile (only one rock song) filled positions #2–#5 entirely with non-rock songs (pop, EDM, drum & bass).

*Whether the recommendations matched expectations:* the top pick matched my intuition every time — each profile's #1 was exactly the song I would have chosen by hand, and the EDM list in particular was coherent from top to bottom, which is what I expected given the strong EDM representation.

*What surprised me:* I was surprised that a "rock" query returned mostly EDM and pop songs after the single rock track, and that in the EDM list the intense EDM songs dropped almost two full points below the energetic ones purely because "intense" is not an exact match for "energetic." The lists degraded into unrelated filler much faster than I expected once the catalog ran out of matching songs.

*Weaknesses and biases I discovered:* this comparison exposed a clear representation bias — the EDM listener gets a coherent, satisfying list while the rock listener effectively gets one real match plus filler, purely because of how many songs each genre has in the dataset. It also reinforced the exact-match "cliff" weakness described in the Limitations section: closely related moods and genres earn zero credit, so the fallback songs are chosen by energy alone rather than by any real musical similarity.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
