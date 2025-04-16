
#  Word of the Day - Desktop Notifier

This Python project sends you a daily desktop notification with a word and its meaning, based on the current date. It’s a fun and easy way to build your vocabulary, right from your computer!

##  Features
-  Sends a desktop notification once a day using `winotify`
-  Maps each calendar day to a specific starting letter (e.g., 1st → A, 2nd → B, etc.)
-  Randomly picks a word starting with that letter from a local dictionary
-  Includes a custom icon for the notification

##  How It Works
- The script maps the current day to a letter (1 → A, 2 → B, ..., 26 → Z, 27 → A again, etc.)
- It filters words from `dict.json` that start with that letter
- A random word is selected and shown as a desktop notification

##  Requirements
- Python 3.x
- `winotify` library  
  Install it using:
  ```bash
  pip install winotify
