# Take input from STDIN, get it’s length and make a substring that takes everything
# but the last character.

sentence = input("Enter a sentence: ")

len_sentence = len(sentence)

last_index = len_sentence - 1

print(sentence[0:last_index])