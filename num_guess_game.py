from tkinter import *
import random

attempts = 10
answer = random.randint(1,99)

def name_submit():
    global btn1
    global label1
    global label2

    name.pack_forget()
    btn_submit.pack_forget()
    
    name1 = name_entry.get()
    label1=Label(root, text="Welcome!" +name1)
    label1.pack()

    label2=Label(root, text="RULES: Guess the number between 1 to 100 within 10 attempts ")
    label2.pack()
    
    name_entry.pack_forget()

    btn1 = Button(root, text="Play", command=game_start)
    btn1.pack()
    
    return

def game_start():
    global entry_window
    global btn1

    label1.pack_forget()
    label2.pack_forget()
    btn1.pack_forget()
    
    global label
    label = Label(root, text="guess the number between 1 and 100")
    label.pack()

    entry_window = Entry(root,width=40, borderwidth=4)
    entry_window.pack()

    global btn_check
    btn_check = Button(root, text="Check", command=check_answer)
    btn_check.pack()

    global btn_quit
    btn_quit = Button(root, text="Quit", command=root.destroy)
    btn_quit.pack()


    global text
    text = StringVar()
    text.set("you have 10 attempts remaining! Good luck!")

    guess_attempts = Label(root, textvariable=text)
    guess_attempts.pack()

    return

def check_answer():
    global attempts
    global text
    global play_again

    play_again = Button(root, text="play again", command=again_play)
    play_again.pack_forget()

    attempts -= 1
    guess = int(entry_window.get())

    if answer == guess:
        text.set("you win! Congrats!!")
        btn_check.pack_forget()
        entry_window.pack_forget()
        play_again.pack()
        
    elif attempts == 0:
        text.set("Game over!")
        btn_check.pack_forget()
        entry_window.pack_forget()
        play_again.pack()
        
    elif guess < answer:
        text.set("Incorrect! you have " + str(attempts) + " attempts remaining! your guess is too low")
    elif guess > answer:
        text.set("Incorrect! you have " + str(attempts) + " attempts remaining! your guess is too high")
    
    return

def again_play():

    global answer
    global attempts
    
    attempts = 10
    answer = random.randint(1,99)
    
    btn_quit.pack_forget()
    play_again.pack_forget()
    
    label.pack()
    entry_window.pack()
    btn_check.pack()
    btn_quit.pack()

    entry_window.delete(0,"end")
    
    text.set("you have 10 attempts remaining! Good luck!")
    
    return
    
root = Tk()

root.title("number guessing game")
root.geometry("500x150")

name = Label(root, text="Enter your name")
name.pack()

name_entry = Entry(root)
name_entry.pack()

btn_submit = Button(root, text="Submit", command=name_submit)
btn_submit.pack()


root.mainloop()
