"""Make a program that takes a string from STDIN, get the letters present in that
string and count how many times they repeat."""

def main():
    """Run the program as a whole."""

    # Get a string from STDIN
    a_string = input("Enter a string: ")

    # Make a dict to associate letters with how many times they repeat
    letter_n_count = {}

    # Loop through the string
    for char in a_string:

        # Check that the character is alphabetic
        if char.isalpha():
            if char not in letter_n_count:
                letter_n_count[char] = 1
            
            else:
                letter_n_count[char] += 1
    
    print(letter_n_count)

if __name__ == "__main__":
    main()