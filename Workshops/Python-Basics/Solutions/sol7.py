"Make a program that prints out all even numbers from 1 to 100."

for number in range(1, 100 + 1):
    if number % 2 != 0:
        continue
    
    print(number)