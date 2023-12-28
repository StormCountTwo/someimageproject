import logging
import random
import sys

from PIL import Image, ImageOps
from tkinter import filedialog

def random_border():
    rgb = [None] * 3
    for i in range(3):
        rgb[i] = random.randrange(256)
        print(rgb[i])
    return rgb


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

    try:
        user_img = Image.open(user_img_path)
    except AttributeError:
        sys.exit()

    border_bool = input("Do you want a random border (y/n)?")
    if border_bool.lower() == "y":
        border_colour = random_border()
        border_size = random.randrange(20)
        print(border_colour)
    elif border_bool.lower() == "n":
        border_colour = get_rgb()
        border_size = get_border_size()
        print(border_colour)
    user_img_border = ImageOps.expand(user_img, border=border_size, fill=tuple(border_colour))
    user_img_border.show()


if __name__ == "__main__":
    main()