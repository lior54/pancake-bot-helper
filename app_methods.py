from PIL import Image, ImageTk
import tkinter as tk
import pancake

def initwindow(app:pancake.App):
    #setting title
    app.root.title("pancake bot helper")
    #change icon
    app.icon = tk.PhotoImage(file="icon.png")
    app.root.iconphoto(True,app.icon)
    #setting window size
    width=600
    height=500
    screenwidth = app.root.winfo_screenwidth()
    screenheight = app.root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    app.root.geometry(alignstr)
    app.root.pack_propagate(False)
    app.root.minsize(int((screenwidth - 450) / 2), int((screenheight - 350) / 2))
    app.root.maxsize(width, height)
    # Show image using label
    app.img = Image.open("pancake.jpg")
    app.img = app.img.resize((600, 500))
    app.img = ImageTk.PhotoImage(app.img) # type: ignore #note for vs code, ignore it
    label1 = tk.Label(app.root, image=app.img)
    label1.place(x=0, y=0, relwidth=1, relheight=1)


