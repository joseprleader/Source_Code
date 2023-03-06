# IPC Problem 7: Sentence Maker

# a) Process data from STDIN
# b) Check if the sentence can be made from the characters given
# b) Return output to the console

def main():

    # Check if it is possible to form sentence
    possible = ""
    
    # Get data from STDIN
    chars, sentence = getSTDIN()

    # Process each as a character array
    char_arr_for_chars = get_char_list(chars)
    char_arr_for_sentence = get_char_list(sentence)

    for char in char_arr_for_sentence:

        try:
            char_arr_for_chars.remove(char)
        
        except:
            possible = "not possible"
            break

    if len(possible) == 0:
        possible = "possible"
    
    print(possible)
    

def getSTDIN():
    """Get input from STDIN."""

    print("Enter the list of letters:")
    chars = input()

    print("Please enter the sentence to be formed:")
    sentence = input()

    return chars, sentence

def get_char_list(string):
    """Returns a list of all alphabetic characters from a string"""

    charlist = []

    for char in string:

        if char.isalpha():
            charlist.append(char)
    
    return charlist

main()