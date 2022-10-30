# Intercollegiate Programming Competition 2021 Golden Track 
# Problem 3 Agreeable Numbers

def main():
    """Run the program as a whole."""

    # Get data from STDIN
    print("Enter two numbers separated by a space:")

    # Get numbers separated by a space
    num1, num2 = input().split()

    num1 = int(num1)
    num2 = int(num2)

    # If both numbers are agreeable print "Agreeable numbers"
    if are_agreeable(num1, num2):
        print("Agreeable numbers")
    
    # Otherwise, print "Not agreeable numbers"
    else:
        print("Not agreeable numbers")

def get_divisors(num):
    """Return a list of divisors from a number."""

    # number to regulate while loop (Exclude the number itself)
    num_while = num -1 

    # List of divisors starting with 1
    divisors = [1]

    # Loop through all numbers that are less than the given number excluding one
    while num_while > 1:

        # If the division remainder is 0, the number is a divisor
        if num % num_while == 0:
            divisors.append(num_while)
        
        # Subtract one from num_while
        num_while -= 1

    return divisors

def are_agreeable(num1, num2):
    """Find if two numbers are agreeable according to the list of their divisors."""

    # Find the divisors of both numbers
    div1 = get_divisors(num1)
    div2 = get_divisors(num2)

    # If the sum of the divisors of num1 is equal to num2 and the sum of divisors of num2 is equal to num1
    # the numbers are agreeable, otherwise they are not
    return sum(div1) == num2 and sum(div2) == num1

if __name__ == "__main__":
    main()