from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_list = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    word_list = original_data.to_dict(orient="records")

else:
    word_list = data.to_dict(orient="records")





def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(flash_card_text, text=f'{current_card['French']}', fill="black")
    canvas.itemconfig(flash_card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_card, image=card_back)
    canvas.itemconfig(title, text='English', fill='White')
    canvas.itemconfig(flash_card_text, text=f'{current_card['English']}', fill='White')


def is_known():
    word_list.remove(current_card)
    next_card()
    new_data = pd.DataFrame(word_list)
    new_data.to_csv('./data/words_to_learn.csv', index=False)


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card = canvas.create_image(400, 265, image=card_front)
title = canvas.create_text(400, 150, text='Title', font=("Arial", 25, 'italic'))
flash_card_text = canvas.create_text(400, 265, text='word',
                                     font=("Arial", 35, 'normal'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
check_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)
correct_btn = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
correct_btn.grid(column=1, row=1)

next_card()
window.mainloop()
