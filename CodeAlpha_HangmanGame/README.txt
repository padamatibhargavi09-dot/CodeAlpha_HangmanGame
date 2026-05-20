# 💀 Hangman Game — CodeAlpha Internship Task 1

A classic Hangman word-guessing game with a graphical interface built using Python and Tkinter.

---

## 📁 Project Structure

```
CodeAlpha_HangmanGame/
├── hangman_gui.py      # Main game file
└── README.md
```

---

## 🎮 Features

- Dark-themed graphical interface (900×680 window)
- Live canvas-drawn gallows that updates with each wrong guess
- On-screen QWERTY keyboard with color-coded buttons:
  - 🟢 Green — correct guess
  - 🔴 Red — wrong guess
- Word hint displayed for each round
- Wrong guess pip indicators (● ● ● ● ● ●) that light up red as mistakes accumulate
- Win/Loss score tracker persisted across rounds within a session
- "NEW GAME" and "QUIT" buttons
- Game Over reveals the full word in red; win message shown in green

---

## 🧩 Word Bank

| Word        | Hint                                     |
|-------------|------------------------------------------|
| python      | 🐍 A popular programming language        |
| hangman     | 🎮 The name of this game                 |
| keyboard    | ⌨️  You type with this                   |
| monitor     | 🖥️  You look at this screen              |
| algorithm   | 🔢 A step-by-step problem-solving method |
| variable    | 📦 Stores data in programming            |
| function    | ⚙️  A reusable block of code             |
| database    | 🗄️  Stores large amounts of data         |
| network     | 🌐 Connects computers together           |
| compiler    | 🔧 Translates code to machine language   |

---

## ⚙️ Requirements

- Python **3.6+**
- **Tkinter** (included with most standard Python installations)

To verify Tkinter is available:

```bash
python -m tkinter
```

If a small test window opens, you're good to go. If not, install it:

```bash
# Ubuntu / Debian
sudo apt-get install python3-tk

# macOS (via Homebrew)
brew install python-tk
```

---

## 🚀 How to Run

```bash
python hangman_gui.py
```

---

## 🕹️ How to Play

1. A secret word is chosen at random and a hint is displayed.
2. Click a letter on the on-screen keyboard to guess.
3. A correct guess reveals the letter's position(s) in the word.
4. A wrong guess adds a body part to the gallows.
5. You have **6 wrong guesses** before the game is over.
6. Guess all letters correctly before the hangman is complete to **win**!

---

## 🗂️ Code Overview

| Component | Description |
|---|---|
| `HangmanApp` (class) | Main Tkinter app window, extends `tk.Tk` |
| `_build_ui()` | Constructs all UI widgets (header, canvas, keyboard, buttons) |
| `new_game()` | Resets all state and starts a fresh round |
| `guess()` | Handles a letter guess, updates button color and game state |
| `_draw_gallows()` | Draws the hangman figure on the canvas based on wrong count |
| `_win()` / `_lose()` | End-of-game handlers that update score and display messages |
| `_update_word_display()` | Refreshes the word label with currently guessed letters |
| `_update_pips()` | Updates the wrong-guess pip indicators |

---

## 🔧 Customization

To add more words, edit the `WORDS` list in `hangman_gui.py`:

```python
WORDS = [
    ("yourword", "💡 Your hint here"),
    ...
]
```

---

## 👤 Author

- Name:padamatibhargavi
- Internship:** CodeAlpha
- Task: Task 1 — Hangman Game

---

## 📄 License

This project was created as part of the CodeAlpha internship program. Free to use and modify for educational purposes.