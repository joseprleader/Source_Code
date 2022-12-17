# Programming Challenge from Codewars
# Python: Rot13

# string module
# contains a bunch of useful constants related to the alphabet

# import string
# string.ascii_letters -> All lowercase and uppercase letters of the English alphabet
# string.ascii_uppercase -> All uppercase letters of the English Alphabet
# string.ascii_lowercase -> All lowercase letters of the English Alphabet

# It contains many more constants related to common string patters, so check it out at:
# https://docs.python.org/3/library/string.html

import string

def rot13(message):
    """Use Caesar Cipher Algorithm to move letters 13 positions up in the alphabet."""

    rot13_message = ""
    
    for char in message:
        
        # Only work with lowecase or uppercase letters
        if char in string.ascii_letters:
            
            # Check whether the letter is uppercase or not
            if char.isupper():
                alpha_index = string.ascii_uppercase.find(char)

                rot13_index = mod_sum(alpha_index)

                rot13_letter = string.ascii_uppercase[rot13_index]

            else:
                alpha_index = string.ascii_lowercase.find(char)

                rot13_index = mod_sum(alpha_index)

                rot13_letter = string.ascii_lowercase[rot13_index]
            
            rot13_message += rot13_letter
        
        else:
            # Concatenate the original char to the string
            rot13_message += char
    
    return rot13_message


def mod_sum(num,base=13,limit=25):
    """Add a number to a constant considering a limit."""

    result = num + base

    if result > limit:
        return result % base
    
    else:
        return result