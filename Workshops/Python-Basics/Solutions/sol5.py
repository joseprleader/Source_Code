"""Take the program from Small Exercise 4 to keep asking the user how they feel
until they enter the string “Stop”"""

# Take input from STDIN
mood = input("How do you feel today? ")

while mood != "Stop":

    if mood == "bad" or mood == "Bad":
        print("How can I help?")

    elif mood == "regular" or mood == "Regular":
        print("You had a boring day.")

    elif mood == "good" or mood == "Good":
        print("Nice.")

    elif mood == "awesome" or mood == "Awesome":
        print("You conquered the world today.")

    else:
        print("Meh, I didn't care in the first place.")
    
    mood = input("How do you feel today? ")