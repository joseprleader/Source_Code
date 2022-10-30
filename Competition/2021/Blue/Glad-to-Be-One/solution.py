# Intercollegiate Programming Competition 2021 Blue Track Problem 6
# Glad to be One

def main():
    """Run the program as a whole."""

    # Get integer from STDIN
    num = int(input("Enter a positive integer: "))

    # Determine whether our number is glad or not
    glad_num = is_glad(num)
    
    # Print glad number if the number is glad, otherwise don't
    # Reference for Python one-liner if statements
    # https://betterdatascience.com/python-if-else-one-line/
    print("Glad Number") if glad_num else print("Not a Glad Number")

def get_digits(num):
    """Return the digits of a number separated by a list."""

    # Reference for list comprehension in Python
    # https://www.w3schools.com/python/python_lists_comprehension.asp

    return tuple(int(digit) for digit in str(num))

def is_glad(num):
    """If a number is glad return True, otherwise return False."""

    # Make a variable result that will control if the loop to check keeps going on or not
    result = 0

    # Make a list of all gotten results
    # If there is repetition cut the loop off, the number won't be glad
    all_results = []

    # As long as the result is not equal to one, keep checking if the number is glad
    while result != 1:

        # If the number has only one digit, square it and make that the result
        if len(get_digits(num)) == 1:

            result = num ** 2
        
        # If the number has more than one digit, square each and sum them up
        else:
            sub_result = 0
            for digit in get_digits(num):
                square_num = digit ** 2
                sub_result += square_num
            
            # Make the result equal to the total sum of the squares of each digit
            result = sub_result
        
        # Update the value of the number to the gotten result
        num = result

        # If the result is already present in the list of all_results, cut the loop off by returning false
        if result in all_results:
            return False

        # Append the gotten result to the list of all_results
        all_results.append(result)
    
    # By this point there is a sequence that ends in 1, so return True
    return True

if __name__ == "__main__":
    main()