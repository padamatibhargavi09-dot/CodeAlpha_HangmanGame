# ============================================================
#  CodeAlpha Internship — Task 1: Hangman Game (GUI Version)
#  Author  :P.Bhargavi
#  GitHub  : CodeAlpha_HangmanGame
#  Run     : 
# ============================================================

import tkinter as tk
from tkinter import font as tkfont
import random

# ── Word Bank with Hints ─────────────────────────────────────
WORDS = [
    ("python",    "🐍 A popular programming language"),
    ("hangman",   "🎮 The name of this game"),
    ("keyboard",  "⌨️  You type with this"),
    ("monitor",   "🖥️  You look at this screen"),
    ("algorithm", "🔢 A step-by-step problem-solving method"),
    ("variable",  "📦 Stores data in programming"),
    ("function",  "⚙️  A reusable block of code"),
    ("database",  "🗄️  Stores large amounts of data"),
    ("network",   "🌐 Connects computers together"),
    ("compiler",  "🔧 Translates code to machine language"),
]

MAX_WRONG = 6

# ── Color Palette (Dark Theme) ───────────────────────────────
BG          = "#0f0f1a"
SURFACE     = "#1a1a2e"
SURFACE2    = "#16213e"
ACCENT      = "#e94560"
ACCENT2     = "#0f3460"
TEXT        = "#eaeaea"
TEXT_DIM    = "#7a7a9a"
GREEN       = "#00d4a0"
YELLOW      = "#ffd460"
RED         = "#e94560"
WHITE       = "#ffffff"
BTN_DEF     = "#1e1e3a"
BTN_HOVER   = "#2a2a4a"
BTN_USED    = "#0d0d1a"
BTN_RIGHT   = "#003a28"
BTN_WRONG   = "#3a0d15"


class HangmanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman — CodeAlpha")
        self.geometry("900x680")
        self.resizable(False, False)
        self.configure(bg=BG)

        # Fonts
        self.f_title  = tkfont.Font(family="Courier New", size=26, weight="bold")
        self.f_sub    = tkfont.Font(family="Courier New", size=12)
        self.f_word   = tkfont.Font(family="Courier New", size=30, weight="bold")
        self.f_hint   = tkfont.Font(family="Courier New", size=11)
        self.f_btn    = tkfont.Font(family="Courier New", size=13, weight="bold")
        self.f_stat   = tkfont.Font(family="Courier New", size=11)
        self.f_msg    = tkfont.Font(family="Courier New", size=18, weight="bold")
        self.f_small  = tkfont.Font(family="Courier New", size=10)

        self.secret_word    = ""
        self.hint           = ""
        self.guessed        = set()
        self.wrong          = 0
        self.game_over      = False
        self.score_win      = 0
        self.score_loss     = 0
        self.letter_buttons = {}

        self._build_ui()
        self.new_game()

    # ── UI Construction ──────────────────────────────────────
    def _build_ui(self):
        # ── Header ──
        hdr = tk.Frame(self, bg=SURFACE, height=60)
        hdr.pack(fill="x")
        tk.Label(hdr, text="💀  H A N G M A N", font=self.f_title,
                 bg=SURFACE, fg=ACCENT).pack(side="left", padx=24, pady=10)

        score_f = tk.Frame(hdr, bg=SURFACE)
        score_f.pack(side="right", padx=24)
        tk.Label(score_f, text="✅ WINS", font=self.f_small, bg=SURFACE, fg=GREEN).grid(row=0, column=0, padx=8)
        self.lbl_wins = tk.Label(score_f, text="0", font=self.f_btn, bg=SURFACE, fg=GREEN)
        self.lbl_wins.grid(row=1, column=0, padx=8)
        tk.Label(score_f, text="❌ LOSS", font=self.f_small, bg=SURFACE, fg=RED).grid(row=0, column=1, padx=8)
        self.lbl_loss = tk.Label(score_f, text="0", font=self.f_btn, bg=SURFACE, fg=RED)
        self.lbl_loss.grid(row=1, column=1, padx=8)

        # ── Main Content ──
        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=20, pady=10)

        # Left — Gallows
        left = tk.Frame(main, bg=BG, width=300)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)

        self.canvas = tk.Canvas(left, width=260, height=300,
                                bg=SURFACE2, highlightthickness=0,
                                bd=0, relief="flat")
        self.canvas.pack(pady=(0, 12))

        # Wrong guess counter bar
        bar_f = tk.Frame(left, bg=BG)
        bar_f.pack(fill="x")
        tk.Label(bar_f, text="WRONG GUESSES", font=self.f_small,
                 bg=BG, fg=TEXT_DIM).pack()
        self.pip_frame = tk.Frame(bar_f, bg=BG)
        self.pip_frame.pack(pady=4)
        self.pips = []
        for i in range(MAX_WRONG):
            p = tk.Label(self.pip_frame, text="●", font=self.f_btn,
                         bg=BG, fg=BTN_DEF)
            p.pack(side="left", padx=3)
            self.pips.append(p)

        # Guessed letters list
        tk.Label(left, text="GUESSED LETTERS", font=self.f_small,
                 bg=BG, fg=TEXT_DIM).pack(pady=(14, 2))
        self.lbl_guessed = tk.Label(left, text="—", font=self.f_hint,
                                    bg=BG, fg=TEXT_DIM, wraplength=250)
        self.lbl_guessed.pack()

        # Right — Word + Keyboard
        right = tk.Frame(main, bg=BG)
        right.pack(side="left", fill="both", expand=True)

        # Hint
        self.lbl_hint = tk.Label(right, text="", font=self.f_hint,
                                 bg=BG, fg=YELLOW)
        self.lbl_hint.pack(pady=(8, 2))

        # Word display
        self.lbl_word = tk.Label(right, text="", font=self.f_word,
                                 bg=BG, fg=WHITE)
        self.lbl_word.pack(pady=12)

        # Status message
        self.lbl_msg = tk.Label(right, text="", font=self.f_msg, bg=BG, fg=GREEN)
        self.lbl_msg.pack(pady=4)

        # Keyboard
        kb_frame = tk.Frame(right, bg=BG)
        kb_frame.pack(pady=8)

        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for r, row in enumerate(rows):
            rf = tk.Frame(kb_frame, bg=BG)
            rf.pack(pady=3)
            for ch in row:
                btn = tk.Button(
                    rf, text=ch, width=3, height=1,
                    font=self.f_btn, bg=BTN_DEF, fg=TEXT,
                    activebackground=BTN_HOVER, activeforeground=WHITE,
                    relief="flat", cursor="hand2", bd=0,
                    command=lambda c=ch: self.guess(c)
                )
                btn.pack(side="left", padx=2)
                self._bind_hover(btn)
                self.letter_buttons[ch] = btn

        # Bottom buttons
        bot = tk.Frame(self, bg=BG)
        bot.pack(pady=10)
        tk.Button(bot, text="🔄  NEW GAME", font=self.f_btn,
                  bg=ACCENT2, fg=WHITE, activebackground=ACCENT,
                  relief="flat", cursor="hand2", padx=18, pady=6,
                  command=self.new_game).pack(side="left", padx=10)
        tk.Button(bot, text="❌  QUIT", font=self.f_btn,
                  bg=BTN_DEF, fg=TEXT_DIM, activebackground=BTN_WRONG,
                  relief="flat", cursor="hand2", padx=18, pady=6,
                  command=self.destroy).pack(side="left", padx=10)

    def _bind_hover(self, btn):
        def on_enter(e):
            if btn["state"] == "normal":
                btn.configure(bg=BTN_HOVER)
        def on_leave(e):
            if btn["state"] == "normal":
                btn.configure(bg=BTN_DEF)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # ── Game Logic ───────────────────────────────────────────
    def new_game(self):
        word_data           = random.choice(WORDS)
        self.secret_word    = word_data[0]
        self.hint           = word_data[1]
        self.guessed        = set()
        self.wrong          = 0
        self.game_over      = False

        # Reset buttons
        for ch, btn in self.letter_buttons.items():
            btn.configure(bg=BTN_DEF, fg=TEXT, state="normal")

        self.lbl_msg.configure(text="", fg=GREEN)
        self.lbl_hint.configure(text=f"Hint: {self.hint}")
        self._update_word_display()
        self._update_pips()
        self._update_guessed_label()
        self._draw_gallows()

    def guess(self, letter):
        if self.game_over or letter in self.guessed:
            return

        self.guessed.add(letter)
        btn = self.letter_buttons[letter]

        if letter.lower() in self.secret_word:
            btn.configure(bg=BTN_RIGHT, fg=GREEN, state="disabled")
            self._update_word_display()
            if all(c in self.guessed.union({c.upper() for c in self.guessed})
                   or c.upper() in self.guessed
                   for c in self.secret_word.upper()):
                self._win()
        else:
            self.wrong += 1
            btn.configure(bg=BTN_WRONG, fg=RED, state="disabled")
            self._update_pips()
            self._draw_gallows()
            if self.wrong >= MAX_WRONG:
                self._lose()

        self._update_guessed_label()

    def _update_word_display(self):
        display = "  ".join(
            c.upper() if c.upper() in self.guessed or c in self.guessed else "_"
            for c in self.secret_word
        )
        self.lbl_word.configure(text=display)

    def _update_pips(self):
        for i, pip in enumerate(self.pips):
            pip.configure(fg=RED if i < self.wrong else TEXT_DIM)

    def _update_guessed_label(self):
        if self.guessed:
            txt = "  ".join(sorted(self.guessed))
        else:
            txt = "—"
        self.lbl_guessed.configure(text=txt)

    def _win(self):
        self.game_over  = True
        self.score_win += 1
        self.lbl_wins.configure(text=str(self.score_win))
        self.lbl_msg.configure(
            text=f"🎉 YOU WON!  The word was '{self.secret_word.upper()}'",
            fg=GREEN)
        for btn in self.letter_buttons.values():
            btn.configure(state="disabled")

    def _lose(self):
        self.game_over   = True
        self.score_loss += 1
        self.lbl_loss.configure(text=str(self.score_loss))
        # Reveal word
        self.lbl_word.configure(
            text="  ".join(c.upper() for c in self.secret_word), fg=RED)
        self.lbl_msg.configure(
            text=f"💀 GAME OVER!  Word was '{self.secret_word.upper()}'",
            fg=RED)
        for btn in self.letter_buttons.values():
            btn.configure(state="disabled")

    # ── Gallows Drawing ──────────────────────────────────────
    def _draw_gallows(self):
        c = self.canvas
        c.delete("all")
        W, H = 260, 300
        pad  = 30

        # Base & pole
        c.create_line(20, H-20, W-20, H-20, fill=TEXT_DIM, width=3)   # base
        c.create_line(70, H-20, 70, 30,     fill=TEXT_DIM, width=3)   # pole
        c.create_line(70, 30,  180, 30,     fill=TEXT_DIM, width=3)   # top
        c.create_line(180, 30, 180, 65,     fill=TEXT_DIM, width=2)   # rope

        n = self.wrong

        # Head
        if n >= 1:
            c.create_oval(160, 65, 200, 105, outline=ACCENT, width=2)

        # Body
        if n >= 2:
            c.create_line(180, 105, 180, 175, fill=ACCENT, width=2)

        # Left arm
        if n >= 3:
            c.create_line(180, 120, 150, 150, fill=ACCENT, width=2)

        # Right arm
        if n >= 4:
            c.create_line(180, 120, 210, 150, fill=ACCENT, width=2)

        # Left leg
        if n >= 5:
            c.create_line(180, 175, 150, 220, fill=ACCENT, width=2)

        # Right leg
        if n >= 6:
            c.create_line(180, 175, 210, 220, fill=ACCENT, width=2)
            # Face — X eyes
            c.create_line(168, 75, 178, 85, fill=RED, width=2)
            c.create_line(178, 75, 168, 85, fill=RED, width=2)
            c.create_line(183, 75, 193, 85, fill=RED, width=2)
            c.create_line(193, 75, 183, 85, fill=RED, width=2)
            # Mouth
            c.create_arc(168, 88, 193, 103, start=200, extent=140,
                         style="arc", outline=RED, width=2)

        # Remaining guesses text
        remaining = MAX_WRONG - self.wrong
        color = GREEN if remaining > 3 else YELLOW if remaining > 1 else RED
        c.create_text(W//2, H-5, text=f"{remaining} guesses left",
                      fill=color, font=("Courier New", 10))


# ── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    app = HangmanApp()
    app.mainloop()
