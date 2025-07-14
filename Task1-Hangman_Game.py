import tkinter as tk
import random


words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []


def guess_letter():
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if letter in guessed_letters:
        message.set("You already guessed that letter.")
        return

    guessed_letters.append(letter)

    if letter in word:
        for idx, l in enumerate(word):
            if l == letter:
                guessed[idx] = letter
        message.set("Correct Guess!")
    else:
        attempts -= 1
        message.set(f"Wrong Guess! Attempts left: {attempts}")

    word_display.set(f"Guess the fruit name: {' '.join(guessed)} ")
    guessed_display.set("Guessed: " + ", ".join(guessed_letters))

    canvas.delete("all")
    draw_hangman()

    if "".join(guessed) == word:
        message.set("🎉 You Won!")
        entry.config(state='disabled')
        guess_button.config(state='disabled')
    elif attempts == 0:
        message.set(f"💀 Game Over! Word was: {word}")
        entry.config(state='disabled')
        guess_button.config(state='disabled')

def draw_hangman():
    if attempts <= 5:
        canvas.create_oval(70, 50, 110, 90)  # Head
    if attempts <= 4:
        canvas.create_line(90, 90, 90, 150)  # Body
    if attempts <= 3:
        canvas.create_line(90, 100, 60, 130)  # Left arm
    if attempts <= 2:
        canvas.create_line(90, 100, 120, 130)  # Right arm
    if attempts <= 1:
        canvas.create_line(90, 150, 60, 180)  # Left leg
    if attempts <= 0:
        canvas.create_line(90, 150, 120, 180)  # Right leg

root = tk.Tk()
root.title("Hangman Game")

word_display = tk.StringVar(value=" ".join(guessed))
message = tk.StringVar()
guessed_display = tk.StringVar(value="Guessed: ")

tk.Label(root, textvariable=word_display, font=("Arial", 24)).pack(pady=10)
tk.Label(root, textvariable=message, fg="red").pack()
tk.Label(root, textvariable=guessed_display).pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=5)

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

canvas.create_line(20, 180, 180, 180)  # Base
canvas.create_line(50, 180, 50, 20)    # Pole
canvas.create_line(50, 20, 90, 20)     # Beam
canvas.create_line(90, 20, 90, 50)     # Rope

root.mainloop()

