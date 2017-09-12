import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    text_new = ""
    for pos in range(len(text)):
        text_new += rotate_character(text[pos],int(rot))
    return text_new


def main():
    text = input('Feed me a letter')
    key = input('Rotation pls!')
    print (encrypt(text, key))

if __name__ == "__main__":
    main()
