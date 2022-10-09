"""Make a program that continuously asks the user for a number, but force exit from it
when the user does not enter digits."""

num = input("Enter a number: ")

while True:
    if not num.isnumeric():
        break
    print(num)
    num = input("Enter a number: ")