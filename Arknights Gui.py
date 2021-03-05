import tkinter as tk
import time
from tkinter.constants import BOTTOM
from PIL import Image, ImageTk
import os
import sys

window = tk.Tk()

topFrame = tk.Frame(
    master=window,
    width=50,
    height=5,
)

middleFrame = tk.Frame(
    master=window,
    height=5,
    width=50,

)

entryFrame = tk.Frame(
    master=window
)

middleFrame.pack(
    fill=tk.BOTH,
    side=tk.BOTTOM,
    expand=True
)

topFrame.pack(
    fill=tk.BOTH, side=tk.TOP, expand=True
)

labelTopFrame = tk.Label(
    master=topFrame,
    text="Arknights Elite Materials Finder",
    fg="black",
    # width=100,
    font=(None,15), height=5, width=50
)
labelTopFrame.pack()

labelMiddleFrame = tk.Label(
    master=topFrame,
    text="Enter name of the Operator",
)
labelMiddleFrame.pack()

entry = tk.Entry()
entry.pack()

window.title("Arknights Material Finder")

print(entry)

def keypress(event):
    name = entry.get()
    if name == 'W':
        name = 'WWWWWWWWWWW'
    entry.delete(0, tk.END)
    images = findPicture(name)
    openImages(images, name)

def openImages(pics, name):
    new_window = tk.Toplevel(window)

    image = ImageTk.PhotoImage(Image.open(pics[0]))
    image2 = ImageTk.PhotoImage(Image.open(pics[1]))

    title1 = tk.Label(new_window, text="Elite 1 Materials", font=22)
    title1.pack()

    panel = tk.Label(new_window, image=image)
    panel.image = image
    panel.pack()

    title2 = tk.Label(new_window, text="Elite 2 Materials", font=22)
    title2.pack()

    panel2 = tk.Label(new_window, image=image2)
    panel2.image = image2
    panel2.pack()

    new_window.title("Elite Materials for " + name)

def findPicture(person):
    collection = []
    for root, dirs, files in os.walk('Elite Mats Ark'):
        for file in files:
            if ".png" in file:
                name = r"Elite Mats Ark"'\\' + file
                collection.append(name)
    pics = []
    for x in collection:
        if person in x:
            pics.append(x)
    return pics

def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join('path', 'Elite Mats Ark')

window.bind("<Return>", keypress)
window.mainloop()


