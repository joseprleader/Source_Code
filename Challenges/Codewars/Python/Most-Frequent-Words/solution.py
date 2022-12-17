# Programming Challenge from CodeWards 4 kyu

# Most frequently used words in a text

import string

def main():
    """Run the program as a whole."""

    top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")

def remove_char(string, char):
    """Remove a character from a string."""

    # Convert the string to a list
    string_lst = [char for char in string]

    # Remove the given char from the list
    string_lst.remove(char)

    # Convert it all back to a string
    return "".join(string_lst)

def top_3_words(text):

    # Convert the given text to lowercase
    textToLower = text.lower()
    
    # Replace any considered withespace character with an authentic whitespace
    white_punc = remove_char(string.punctuation, "'")

    # replace all white punctuation by whitespace character
    textToLower = textToLower.replace(white_punc, " ")

    print(textToLower)


if __name__ == "__main__":
    main()