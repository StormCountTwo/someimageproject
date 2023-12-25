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


def get_border_size():
    try:
        border_size = int(input("Enter border size (in pixels): "))
        return border_size
    except ValueError:
        print("Invalid input")
        return get_border_size()


def main():
    user_img_path = filedialog.askopenfilename()
    user_img = Image.open(user_img_path)
    border_colour = get_rgb()
    border_size = get_border_size()
    user_img_border = ImageOps.expand(user_img, border=border_size, fill=tuple(border_colour))
    user_img_border.show()


if __name__ == "__main__":
    main()
