"""Write a small program that asks the user how the feel today.
● If they say “bad” or “Bad” print out: “How can I help”?
● If they say “regular” or “Regular” print out: “You had a boring day.”
● If they say “good” or “Good” print out: “Nice”.
● If they say “awesome” or “Awesome” print out: “You conquered the world
today.”
● For all other cases print out. “Meh, I didn’t even care in the first place."""

# Take mood from STDIN
mood = input("How do you feel today? ")

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