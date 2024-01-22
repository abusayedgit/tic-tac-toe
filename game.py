import tkinter as tk
import tkinter.messagebox

def on_button_click(button):
    global player

    if button["text"] == "" and player == "X":
        button["text"] = "X"
        player = "O"
        check_for_winner()
    elif button["text"] == "" and player == "O":
        button["text"] = "O"
        player = "X"
        check_for_winner()

def check_for_winner():
    for a, b, c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            tkinter.messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            reset_game()
            return

    if all(button["text"] != "" for button in buttons):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_game()

def reset_game():
    global player
    player = "X"
    for button in buttons:
        button["text"] = ""

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize player
player = "X"

# Create buttons
buttons = [tk.Button(root, font=('normal', 40), width=5, height=2, command=lambda i=i: on_button_click(buttons[i])) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

# Define winning combinations
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Start the game loop
root.mainloop()
