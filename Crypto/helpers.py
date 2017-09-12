import string

def alphabet_position(letter):
    value = string.ascii_lowercase.index(letter)
    return value
    

def rotate_character(char, rot):
    if char.isalpha(): 
        value = string.ascii_lowercase.index(char.lower())
        rotation = rot + value
        new_num = rotation % 26
        new_letter = string.ascii_lowercase[new_num]
        new_cypher = []
        if char.isupper() == True:
            return new_letter.upper()
        else:
            return new_letter
    else:
        return char 
    