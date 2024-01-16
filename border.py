import random
import sys
from modern_colorthief import ColorThief
from PIL import Image, ImageOps
from tkinter import filedialog


def yes_or_no(question):
    while True:
        y_or_n = input(f"{question} (y/n)? ")
        if y_or_n.lower().strip() in ["y", "yes"]:
            answer = True
            break
        elif y_or_n.lower().strip() in ["n", "no"]:
            answer = False
            break
        else:
            print("Invalid input")
    return answer


def random_border():
    return list(map(lambda x: random.randrange(256), range(3)))


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
    extension = "png"
    image = filedialog.asksaveasfilename(defaultextension="."+extension)
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
    if yes_or_no("Do you want a dominant colour border "):
        border_colour = ColorThief(user_img_path).get_color()
    else:
        border_colour = get_rgb()

    if yes_or_no("Do you want a random border size "):
        border_size = random.randrange(20)
    else:
        border_size = get_border_size()

    # Modify and preview the image
    user_img_border = ImageOps.expand(user_img, border=border_size, fill=tuple(border_colour))
    user_img_border.show()
    if yes_or_no("Do you want to save the image "):
        save_new_image(user_img_border)


if __name__ == "__main__":
    main()
