# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- the "hint" only tells you to "go higher", even when the secret numer is lower than the attempt
the "new game" button does not work
scoring seems to be incorrect
game ends when 1 attempt is left

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 I used Copilot. One example of an AI suggestion that was correct was that the agent was able to correcty move the function names I gave it to the logic_utils.py file from app.py file. I was able to verify via checking both the files.
 The AI had not called correct imports during the switch. As a result, the UI of the game was showing an error via streamlit. I was able to fix it by giving the AI the error I was facing, with a more detailed prompt.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided the attempts left bug was fixed after playing the game in the local host following AI's fix. 
For other fixes, such as, for fixing the hints, I instructed the AI to create separate pytests for testing higher/lower hints. The failed tests confirmed logic errors that were later fixed. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I learnt how to use Copilot's Generate Commit Message feature in the Source Control tab.  
- What is one thing you would do differently next time you work with AI on a coding task?
I would give the AI examples of the changes I want it to make in the prompt.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is not always correct. This project made me more informed on effective prompts. 