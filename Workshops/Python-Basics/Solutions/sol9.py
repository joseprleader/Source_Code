"""Exercise 9
Write two functions, one that returns true when a number is even and another that
returns true when a number is odd.
Then make a program that continuously asks the user for a number and print out if
that number is even or odd.
Exit the loop when the user enters “Stop”."""

def main():
    """Run the program as a whole."""
    
    num = input("Enter a number: ")

    while num != "Stop":
        num = int(num)

        if not is_odd(num):
            print("It's even")
        
        else:
            print("It's odd.")
        
        num = input("Enter a number: ")

def is_odd(num):
    """Return True if a number is odd."""
    if num % 2 != 0:
        return True
    
    else:
        return False

main()