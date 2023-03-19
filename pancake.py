import os
os.chdir(os.path.abspath(os.path.dirname( __file__ )).replace("\\lib\\library.zip", ""))#should help if program being executed from another folder. ".replace" is to change directory in the exe file
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import sqlite3
import app_methods


class App:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.wm_attributes("-topmost", 1)
        self.icon = tk.PhotoImage()
        self.img = Image.Image()
        app_methods.initwindow(self)
        
        self.CDtrivia = 0
        self.BtTrivia = tk.Button(root, text="Trivia", command=self.start_countdown_trivia)
        self.BtTrivia.place(relx=0.05, rely=0.1, width=135, height=40)

        self.CDwork = 0
        self.BtWork = tk.Button(root, text="Work", command=self.start_countdown_work)
        self.BtWork.place(relx=0.05, rely=0.3, width=135, height=40)

        self.CDfish = 0
        self.BtFish = tk.Button(root, text="Fish", command=self.start_countdown_fish)
        self.BtFish.place(relx=0.05, rely=0.5, width=135, height=40)

        self.CDhighlow = 0
        self.BtHighlow = tk.Button(root, text="High low", command=self.start_countdown_highlow)
        self.BtHighlow.place(relx=0.05, rely=0.7, width=135, height=40)

        self.BtTriviaAnswer = tk.Button(root, text="Get answer", command=self.get_answer)
        self.BtTriviaAnswer.place(relx=0.5, rely=0.5, width=135, height=40)

        self.txtrivia = tk.Text(root)
        self.txtrivia.place(relx=0.375, rely=0.175, width=270, height=80)

        self.labelAns = tk.Label(root, text="")
        self.labelAns.place(relx=0.45, rely=0.7, width=200, height=40)


    def get_answer(self):
        self.labelAns.config(text="")
        text = self.txtrivia.get(1.0, "end-1c")
        text = text.strip("\n ")
        if text == "":
            self.labelAns.config(text="please enter question")
        else:
            conn = sqlite3.connect('./tdb.db')
            sql = f'SELECT answer FROM trivia where question like "%{text}%";'
            cursor = conn.execute(sql).fetchall()
            self.labelAns.config(text=cursor[0][0])
            conn.close()


    def start_countdown_trivia(self):
        self.BtTrivia.config(state="disabled")
        if self.CDtrivia > 0:
            self.CDtrivia = 600
        else:
            self.CDtrivia = 600  # reset the countdown timer
            self.update_button_trivia()


    def update_button_trivia(self):
        if self.CDtrivia == 120:
            self.BtTrivia.config(state="normal")
        if self.CDtrivia > 0:
            self.BtTrivia.config(text="Trivia ({}:{})".format(int(self.CDtrivia / 60), str(self.CDtrivia % 60).rjust(2,"0")))
            self.CDtrivia -= 1
            root.after(1000, self.update_button_trivia)  # schedule the next update after 1 second
        else:
            self.BtTrivia.config(text="Trivia")  # reset the button text


    def start_countdown_work(self):
        self.BtWork.config(state="disabled")
        if self.CDwork > 0:
            self.CDwork = 300
        else:
            self.CDwork = 300  # reset the countdown timer
            self.update_button_work()


    def update_button_work(self):
        if self.CDwork == 60:
            self.BtWork.config(state="normal")
        if self.CDwork > 0:
            self.BtWork.config(text="Work ({}:{})".format(int(self.CDwork / 60), str(self.CDwork % 60).rjust(2,"0")))
            self.CDwork -= 1
            root.after(1000, self.update_button_work)  # schedule the next update after 1 second
        else:
            self.BtWork.config(text="Work", state="normal")  # reset the button text


    def start_countdown_fish(self):
        self.BtFish.config(state="disabled")
        if self.CDfish > 0:
            self.CDfish = 60
        else:
            self.CDfish = 60  # reset the countdown timer
            self.update_button_fish()


    def update_button_fish(self):
        if self.CDfish == 15:
            self.BtFish.config(state="normal")
        if self.CDfish > 0:
            self.BtFish.config(text="Fish ({}:{})".format(int(self.CDfish / 60), str(self.CDfish % 60).rjust(2,"0")))
            self.CDfish -= 1
            root.after(1000, self.update_button_fish)  # schedule the next update after 1 second
        else:
            self.BtFish.config(text="Fish")  # reset the button text
    

    def start_countdown_highlow(self):
        self.BtHighlow.config(state="disabled")
        if self.CDhighlow > 0:
            self.CDhighlow = 30
        else:
            self.CDhighlow = 30  # reset the countdown timer
            self.update_button_highlow()


    def update_button_highlow(self):
        if self.CDhighlow == 10:
            self.BtHighlow.config(state="normal")
        if self.CDhighlow > 0:
            self.BtHighlow.config(text="High low ({}:{})".format(int(self.CDhighlow / 60), str(self.CDhighlow % 60).rjust(2,"0")))
            self.CDhighlow -= 1
            root.after(1000, self.update_button_highlow)  # schedule the next update after 1 second
        else:
            self.BtHighlow.config(text="High low")  # reset the button text


if __name__ == "__main__":
    root = tk.Tk()
    global app
    app = App(root)
    root.mainloop()