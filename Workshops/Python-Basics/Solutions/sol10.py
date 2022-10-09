"""Make a program that continually asks the user for integers. Then add only even
numbers to a list and print that list."""

def main():
    """Run the program as a whole."""

    even_nums = []

    # Take a number form STDIN
    num = input("Enter a number: ")

    # Keep running the loop until the user enters "Stop"
    while num != "Stop":
        # Convert the number to an integer
        num = int(num)

        # Only append to the list even numbers
        if num % 2 == 0:
            even_nums.append(num)
        
        num = input("Enter a number: ")
    
    print(even_nums)

# Do not run this program if it is imported by another Python file
if __name__ == "__main__":
    main()