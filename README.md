# 💀 Hangman Game — CodeAlpha Internship Task 1

A classic **Hangman word-guessing game** with a dark-themed graphical interface built using **Python** and **Tkinter**. Developed as Task 1 of the CodeAlpha Internship Program.

---

## 📸 Preview

> A dark-themed 900×680 window with a live-drawn gallows, on-screen QWERTY keyboard, and score tracker.

---

## 📁 Project Structure

```
CodeAlpha_HangmanGame/
├── hangman_gui.py      # Main game file (all logic + UI)
└── README.md           # Project documentation
```

---

## ✨ Features

- 🎨 **Dark-themed GUI** — sleek 900×680 window built with Tkinter
- 🖼️ **Live canvas gallows** — hangman figure draws step by step with each wrong guess
- ⌨️ **On-screen QWERTY keyboard** with color-coded feedback:
  - 🟢 **Green** — correct guess
  - 🔴 **Red** — wrong guess
- 💡 **Word hints** displayed for every round
- ⚫ **Wrong guess pip indicators** (● ● ● ● ● ●) that light up red as mistakes accumulate
- 🏆 **Win/Loss score tracker** persisted across rounds within a session
- 🔄 **NEW GAME** button to restart anytime
- ❌ **QUIT** button to exit
- 📢 Game Over reveals the full word in **red**; win message shown in **green**

---

## 🧩 Word Bank

| Word | Hint |
|---|---|
| python | 🐍 A popular programming language |
| hangman | 🎮 The name of this game |
| keyboard | ⌨️ You type with this |
| monitor | 🖥️ You look at this screen |
| algorithm | 🔢 A step-by-step problem-solving method |
| variable | 📦 Stores data in programming |
| function | ⚙️ A reusable block of code |
| database | 🗄️ Stores large amounts of data |
| network | 🌐 Connects computers together |
| compiler | 🔧 Translates code to machine language |

---

## ⚙️ Requirements

- Python **3.6+**
- **Tkinter** — included with most standard Python installations

### Verify Tkinter is available:
```bash
python -m tkinter
```
If a small window opens, you're good to go. If not, install it:

```bash
# Ubuntu / Debian
sudo apt-get install python3-tk

# macOS (via Homebrew)
brew install python-tk
```

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/padamatibhargavi09-dot/CodeAlpha_HangmanGame.git
```

**2. Navigate to the project folder:**
```bash
cd CodeAlpha_HangmanGame
```

**3. Run the game:**
```bash
python hangman_gui.py
```

---

## 🕹️ How to Play

1. A **secret word** is chosen at random and a **hint** is displayed
2. Click a letter on the **on-screen keyboard** to guess
3. A **correct guess** reveals the letter's position(s) in the word
4. A **wrong guess** adds a body part to the gallows
5. You have **6 wrong guesses** before the game is over
6. Guess all letters correctly before the hangman is complete to **WIN!** 🎉

---

## 🗂️ Code Overview

| Component | Description |
|---|---|
| `HangmanApp` | Main Tkinter app window, extends `tk.Tk` |
| `_build_ui()` | Constructs all UI widgets (header, canvas, keyboard, buttons) |
| `new_game()` | Resets all state and starts a fresh round |
| `guess()` | Handles a letter guess, updates button color and game state |
| `_draw_gallows()` | Draws the hangman figure based on wrong guess count |
| `_win()` / `_lose()` | End-of-game handlers that update score and show messages |
| `_update_word_display()` | Refreshes the word label with currently guessed letters |
| `_update_pips()` | Updates the wrong-guess pip indicators |

---

## 🔧 Customization

To add more words, edit the `WORDS` list in `hangman_gui.py`:

```python
WORDS = [
    ("yourword", "💡 Your hint here"),
    ("anotherword", "🔥 Another hint"),
    ...
]
```

---

## 👤 Author

| | |
|---|---|
| **Name** | Padamatibhargavi9 |
| **GitHub** | [@padamatibhargavi09-dot](https://github.com/padamatibhargavi09-dot) |
| **Internship** | CodeAlpha |
| **Task** | Task 1 — Hangman Game |

---

## 📄 License

This project was created as part of the **CodeAlpha Internship Program**.
Free to use and modify for educational purposes.

---

⭐ *If you found this project helpful, consider giving it a star!*
