import random
import sys
from modern_colorthief import ColorThief
from PIL import Image, ImageOps
from tkinter import filedialog


def random_border():
    rgb = [None] * 3
    for i in range(3):  # Loops thrice for red, green, and blue values in that order
        rgb[i] = random.randrange(256)  # 0-255 limit due to RGB cap
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


# Save as image as argument
# TODO: Add image file type option, as .png is the current default
def save_new_image(final_image):
    image = filedialog.asksaveasfilename(defaultextension=".png")
    if image:
        saved_final = final_image
        saved_final.save(image)



def main():
    user_img_path = filedialog.askopenfilename()

    # To fix, prevent user from uploading non-image instead of using exception
    try:
        user_img = Image.open(user_img_path)
    except Exception:
        sys.exit()

    # Loops questions until valid input
    while True:
        border_colour_bool = input("Do you want a dominant colour border (y/n)?")
        if border_colour_bool.lower().strip() in ["y", "yes"]:
            border_colour = ColorThief(user_img_path).get_color()
            break
        elif border_colour_bool.lower().strip() in ["n", "no"]:
            border_colour = get_rgb()
            break
        else:
            print("Please enter only y or n")
            continue

    while True:
        border_size_bool = input("Do you want a random border size (y/n)?")
        if border_size_bool.lower().strip() in ["y", "yes"]:
            border_size = random.randrange(20)
            break
        elif border_size_bool.lower().strip() in ["n", "no"]:
            border_size = get_border_size()
            break
        else:
            print("Please enter only y or n")
            continue

    # Modify and preview the image
    user_img_border = ImageOps.expand(user_img, border=border_size, fill=tuple(border_colour))
    user_img_border.show()

    while True:
        save_bool = input("Do you want to save the image (y/n)?")
        if save_bool.lower() in ["y", "yes"]:
            save_new_image(user_img_border)
            break
        elif save_bool.lower() in ["n", "no"]:
            break
        else:
            print("Please enter only y or n")
            continue

if __name__ == "__main__":
    main()