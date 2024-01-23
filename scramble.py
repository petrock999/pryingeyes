import tkinter as tk
import random

def scramble_char(char):
    """ Scramble a character """
    if char.isalpha():
        return random.choice('abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return char

def on_key_press(event):
    global actual_text
    if event.keysym == 'BackSpace':
        actual_text = actual_text[:-1]
        text_widget.delete("end-2c")
    else:
        char = event.char
        if char:
            actual_text += char
            scrambled_char = scramble_char(char)
            text_widget.insert(tk.END, scrambled_char)

def save_file():
    global actual_text
    with open("saved_text.txt", "w") as file:
        file.write(actual_text)
    actual_text = ""
    text_widget.delete('1.0', tk.END)
    print("Text saved to saved_text.txt")

# Initialize the actual text
actual_text = ""

# Create the main window
root = tk.Tk()
root.title("Scramble Text App")
root.configure(bg='#f0f0f0')

# Create a Text widget
text_widget = tk.Text(root, wrap='word', height=10, width=40, font=("Arial", 12), bg="#ffffff", fg="#333333")
text_widget.pack(pady=20, padx=20)

# Bind the key press event
text_widget.bind("<KeyPress>", on_key_press)

# Create a Save button
save_button = tk.Button(root, text="Save Text", command=save_file, font=("Arial", 10), bg="#4CAF50", fg="white")
save_button.pack(pady=20, padx=20)

# Set focus to the text widget
text_widget.focus_set()

# Start the GUI event loop
root.mainloop()
