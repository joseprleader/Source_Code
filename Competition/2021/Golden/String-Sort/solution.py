# Intercollegiate Programming Competition Gold Track 2021 Challenge #5
# String Sort

def main():
    """Run the program as a whole."""

    words = stdin()
    words = sorted(words, key=len)
    print(words)

def stdin():
    """Get relevant input from the console."""

    count = int(input("Enter count of words: "))
    words = []

    for i in range(count):
        word = input("Enter next word: ")
        words.append(word)
    
    return words

if __name__ == "__main__":
    main()