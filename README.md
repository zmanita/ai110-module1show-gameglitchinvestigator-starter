# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

   The game's purpose is to Display winning messages when usen can guess the secret, calculate and display number of attempts left, end game when 0 attempts left, and show correct hints (higher/lower) based on user guess and secret.

   The bugs I found: 
   the "hint" only tells you to "go higher", even when the secret number is lower than the attempt
   the "new game" button does not work
   scoring seems to be incorrect
   game ends when 1 attempt is left

   Fixes applied:
   Fixed hints 
   New game button works
   Game ends after 0 attempts left
   Moved code from app.py to logic_utils.py

## 📸 Demo

- [ ] ![alt text](image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
