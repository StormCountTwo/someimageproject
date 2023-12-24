import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def main():
    def image_popup():
        user_image = filedialog.askopenfilename()
        top = tk.Toplevel(root)
        top.geometry('540x540')
        try:
            im = Image.open(user_image)
            top_image = ImageTk.PhotoImage(im)
            tk.Label(top, image=top_image).pack()
            print(user_image)
            top.mainloop()
        except IOError:
            print("error")

    root = tk.Tk()
    root.title("Image Viewer")
    root.geometry('500x500')
    open_image = (tk.Button(root, text="Open Image", command=image_popup))
    open_image.pack(pady='20')
    root.mainloop()

if __name__ == "__main__":
    main()
