# PY4E Module 7: Strings Exercise 6.5 

def main():
    """Run the program as a whole."""
    text = "X-DSPAM-Confidence:    0.8475"

    first_index = text.find("0")
    last_index = text.find("5")

    whole_num = float(text[first_index:last_index + 1])

    print(whole_num)

if __name__ == "__main__":
    main()
