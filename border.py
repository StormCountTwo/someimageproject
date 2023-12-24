from PIL import Image, ImageOps
from tkinter import filedialog


def get_rgb():
    try:
        red = int(input("Enter red value (0-255): "))
        green = int(input("Enter green value (0-255): "))
        blue = int(input("Enter blue value (0-255): "))
        return red, green, blue
    except ValueError:
        print("Invalid input")
        return get_rgb()


def main():
    user_img_path = filedialog.askopenfilename()
    user_img = Image.open(user_img_path)
    border_colour = get_rgb()
    user_img_border = ImageOps.expand(user_img, border=20, fill=tuple(border_colour))
    user_img_border.show()


if __name__ == "__main__":
    main()
