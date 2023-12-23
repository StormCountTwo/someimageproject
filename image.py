import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def image_popup():
    user_image = filedialog.askopenfilename()
    top = tk.Toplevel(root)
    try:
        im = Image.open(user_image)
        top_image = ImageTk.PhotoImage(im)
        tk.Label(top, image=top_image).pack()
        top.mainloop()
        print("valid image")
    except:
        print("error")


root = tk.Tk()
root.geometry('500x500')

open_image = tk.Button(root, text="Open Image", command=image_popup).pack(pady='20')

root.mainloop()
