from tkinter import*
import pandas
from random import choice, randint
BACKGROUND_COLOR = "#B1DDC6"

# --------------------window-----------------------------
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----------------csv manager---------------------------
word_choice = {}
word_list = pandas.read_csv('D:/PycharmProjects/flash-card-project-start/data/french_words.csv')
word_list_dict = word_list.to_dict(orient='records')


# ------------------flip card---------------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=card_image_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=f"{word_choice['English']}", fill='white')


# --------------------next word function------------------------
def next_question():
    global word_choice
    word_choice = choice(word_list_dict)
    french_choice = word_choice['French']
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=f'{french_choice}', fill='black')
    canvas.itemconfig(canvas_image, image=card_image_front)
    window.after(3000, func=flip_card)


# ---------------------------canvas design-----------------------
canvas = Canvas(width=800, height=526)
card_image_front = PhotoImage(file='D:/PycharmProjects/flash-card-project-start/images/card_front.png')
card_image_back = PhotoImage(file='D:/PycharmProjects/flash-card-project-start/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_image_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=1, column=1, columnspan=2)

# ---------------------------buttons design--------------------------
cross_button = Button(text='good')
cross_image = PhotoImage(file='D:/PycharmProjects/flash-card-project-start/images/wrong.png')
cross_button.configure(bg=BACKGROUND_COLOR, image=cross_image, highlightthickness=0, command=next_question)
cross_button.grid(row=2, column=1)

good_button = Button(text='good')
good_image = PhotoImage(file='D:/PycharmProjects/flash-card-project-start/images/right.png')
good_button.configure(bg=BACKGROUND_COLOR, image=good_image, highlightthickness=0, command=next_question)
good_button.grid(row=2, column=2)

next_question()

# ------------------------keeps the window open until canceled-------------------
window.mainloop()
