

def main():
    
    letter_n_num = {
        "A" : 2,
        "B" : 2,
        "C" : 2,
        "D" : 3,
        "E" : 3,
        "F" : 3,
        "G" : 4,
        "H" : 4,
        "I" : 4,
        "J" : 5,
        "K" : 5,
        "L" : 5,
        "M" : 6,
        "N" : 6,
        "O" : 6,
        "P" : 7,
        "Q" : 7,
        "R" : 7,
        "S" : 7,
        "T" : 8,
        "U" : 8,
        "V" : 8,
        "W" : 9,
        "X" : 9,
        "Y" : 9,
        "Z" : 9
    }

    final_phone_num = ""

    print("Enter the phone number:")
    user_phone_num = input()

    for char in user_phone_num:

        if char.isalpha():

            final_phone_num += str(letter_n_num[char.upper()])
        
        else:
            final_phone_num += char
    
    print(final_phone_num)

main()