# Intercollegiate Programming Competition 2021 Gold Track
# Problem 2 Single Digit

def main():
    """Run the program as a whole."""

    # Take number from STDIN
    num = input("Enter the number: ")

    # Get the list of digits from the number
    digits = split_to_digits(num)

    # List to be used in the while loop to find final single digit
    resultingList = digits[:]

    # Variable that controls if the final result is one single digit
    oneDigit = len(resultingList) == 1

    # As long as the final result is not a single digit, keep subtracting
    while not oneDigit:

        resultingList = get_sub_digits(resultingList)

        if len(only_one(resultingList)) == 1 or len(resultingList) == 1:
            oneDigit = True
    
    # Print results to STDOUT
    if only_one(resultingList):
        print(only_one(resultingList)[0])
    
    else:
        print(resultingList[0])


def split_to_digits(num):
    """Split a number into a list of its digits."""

    # Convert the number into a string
    # Loop through every single digit and add them to
    # a list as integers

    # List Comprehension in Python
    # https://www.w3schools.com/python/python_lists_comprehension.asp
    return [int(digit) for digit in str(num)]


def only_one(digits):
    """From a list of digits, check there is only one element greater than 0."""

    # Make a list of items greater than 0
    greater_0 = []

    # Loop through the list of digits
    for digit in digits:

        if digit > 0:
            greater_0.append(digit)
    
    return greater_0

def get_sub_digits(digits):
    """Return the digits resulting from subtracting a list of digits."""

    # Final list of sub digits
    sub_digits = []

    # Loop through all digits but the last one
    for i in range(len(digits) - 1):

        # Don't consider negative results
        # Instead use absolute value
        sub_digit = abs(digits[i] - digits[i + 1])
        
        # Append the result to the list of sub-digits
        sub_digits.append(sub_digit)
    
    return sub_digits

if __name__ == "__main__":
    main()