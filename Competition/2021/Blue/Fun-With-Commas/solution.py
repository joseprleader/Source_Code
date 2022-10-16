# Intercollegiate Programming Competition 2021 Blue Track Problem 2
# Fun With Commas

def main():
    """Run the whole program as a whole."""

    # Words given by the user, excluding 'quit'
    all_words = []

    # Ask the user for a word to input
    word = input("Enter next word or quit: ")

    # Keep prompting the user for words until the word 'quit' is entered
    while word != "quit":
        # Add the entered word to the list of all_words
        all_words.append(word)
        word = input("Enter next word or quit: ")
    
    # Concatenate all words in the required format
    concatenate_words(all_words)

def concatenate_words(words):
    """Concatenate words of a list in a string of 
    the format: a, b, c and d."""

    # Final string to be printed
    final_str = ""

    # Index to keep track of words
    index = 0

    # Iterate through all words of the list except the last one
    for word in words[:-1]:

        # Add the comma for words that are before the one in index -2 (The one before the last word in the list)
        if index != len(words) - 2:
            to_concat = word + ", "
        
        else:
            to_concat = word + " "
        
        final_str += to_concat
        index += 1
    
    # If more than one word was given, add 'and' to the end
    if len(words) > 1:
        # Add the "and [last word]" to the final string
        final_str += "and " + words[-1]
    
    else:
        final_str = words[-1]

    # Print the final string
    print(final_str)

# Do not run this code if this script is imported by another python file
if __name__ == "__main__":
    main()