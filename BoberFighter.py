import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import sys

# Define choices and other variables
choices = {'r': ('Rock', 'Scissors'), 'p': ('Paper', 'Rock'), 's': ('Scissors', 'Paper')}
screen_width, screen_height = None, None
bg_photo, rock_photo, paper_photo, scissors_photo, give_up_photo = None, None, None, None, None
result_label = None

# Determine the base path for images
if getattr(sys, 'frozen', False):  # if running as compiled executable
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Define image paths
bg_path = os.path.join(base_path, "beaver.png")
rock_path = os.path.join(base_path, "rock.png")
paper_path = os.path.join(base_path, "paper.png")
scissors_path = os.path.join(base_path, "scissors.png")
give_up_path = os.path.join(base_path, "giveup.png")

def determine_winner(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    user, computer = choices[user_choice]

    if user == computer_choice:
        result_label.config(text=f"Kurwa Bober Tie! Both chose {user}.")
    elif (user, computer_choice) in choices.values():
        result_label.config(text=f"Kurwa Wins! Kurwa chose {user} beats Bobers choice {computer_choice}.")
    else:
        result_label.config(text=f"Bober Wins! Bober chose {computer_choice} beats Kurwas choice {user}.")

def on_choice_click(choice):
    determine_winner(choice)

def exit_application():
    if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
        root.destroy()

# Create the Tkinter window
root = tk.Tk()
root.title("Bober Fighter")
root.configure(background='SystemButtonFace')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes('-fullscreen', True)

# Load the images
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)

rock_image = Image.open(rock_path)
rock_image = rock_image.resize((300, 200))
rock_photo = ImageTk.PhotoImage(rock_image)

paper_image = Image.open(paper_path)
paper_image = paper_image.resize((300, 200))
paper_photo = ImageTk.PhotoImage(paper_image)

scissors_image = Image.open(scissors_path)
scissors_image = scissors_image.resize((300, 200))
scissors_photo = ImageTk.PhotoImage(scissors_image)

give_up_image = Image.open(give_up_path)
give_up_image = give_up_image.resize((300, 200))
give_up_photo = ImageTk.PhotoImage(give_up_image)

# Create and place the background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create buttons for rock, paper, and scissors
for short_code, (choice, _) in choices.items():
    if short_code == 'r':
        button = tk.Button(root, image=rock_photo, command=lambda c=short_code: on_choice_click(c), bd=0)
        button.image = rock_photo
        button.place(x=0, y=0)
    elif short_code == 'p':
        button = tk.Button(root, image=paper_photo, command=lambda c=short_code: on_choice_click(c), bd=0)
        button.image = paper_photo
        button.place(x=screen_width - 300, y=0)
    elif short_code == 's':
        x_coordinate = (screen_width - 0) // 2
        y_coordinate = 0
        button = tk.Button(root, image=scissors_photo, command=lambda c=short_code: on_choice_click(c), bd=0)
        button.image = scissors_photo
        button.place(x=x_coordinate, y=y_coordinate)

# Create the give up button
give_up_button = tk.Button(root, image=give_up_photo, command=exit_application, bd=0)
give_up_button.image = give_up_photo
give_up_button.pack(pady=10)
give_up_button.place(x=screen_width - 300, y=screen_height - 200)

# Create the result label
result_label = tk.Label(root, text="", font=("Helvetica", 26))
result_label.pack(pady=10)
x_coordinate = (screen_width - 1000) // 2
y_coordinate = (screen_height - 100) // 2
result_label.place(x=x_coordinate, y=y_coordinate)

root.mainloop()