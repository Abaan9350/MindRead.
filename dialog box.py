import tkinter as tk
from tkinter import messagebox

class CharacterGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Character Guessing Game")

        self.label = tk.Label(master, text="Is your character a boy?")
        self.label.pack()

        self.yes_button = tk.Button(master, text="Yes", command=self.ask_question)
        self.yes_button.pack(side=tk.LEFT)

        self.no_button = tk.Button(master, text="No", command=self.ask_question)
        self.no_button.pack(side=tk.RIGHT)

    def ask_question(self):
        question = self.label.cget("text")

        if question == "Is your character a boy?":
            self.label.config(text="Does he wear spectacles?")
        elif question == "Does he wear spectacles?":
            # Add logic for the next question and so on...

            # For demonstration purposes, showing a message box at the end
            messagebox.showinfo("Result", "You are thinking of Raihan!")

def main():
    root = tk.Tk()
    app = CharacterGuessGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
