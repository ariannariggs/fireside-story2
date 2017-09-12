
import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    text_new = ""
    indx = 0      
    for pos in range(len(text)):
        if text[pos].isalpha():
            rot = string.ascii_lowercase.index(key[indx % len(key)].lower())
            text_new += rotate_character(text[pos], rot)
            indx = indx +1 
        else:
            text_new += text[pos]
    return text_new

def main():
    text = input('Feed me a note')
    key = input('Type out a key')
    print (encrypt(text, key))

if __name__ == "__main__":
    main()