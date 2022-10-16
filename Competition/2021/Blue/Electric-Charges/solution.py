# Intercollegiate Programming Competition 2021 Blue Track Problem 1
# Electric Charges
import math

def main():
    """Execute the program as a whole."""

    # Ask the user for the hours of electricity spent
    hours = int(input("Enter the KW hours used: "))

    # Get the bill to be paid
    bill_to_pay = total_bill(hours)

    # Print out the result to STDOUT
    print("Amount owed is $" + str(bill_to_pay))

def cents_to_dollars(cents):
    """Converts cents to dollars."""
    
    return cents / 100

def round_up(number, decimals = 0):
    """Properly round up numbers when decimal place is 5 or more."""

    product = 10 ** decimals
    return math.ceil(number * product) / product

def total_bill(hours):
    """Calculate the total bill to return."""

    # Bill to be paid
    bill = 0

    # Electricity rates to be paid
    rate_before_1000 = cents_to_dollars(7.633)
    rate_after_1000 = cents_to_dollars(9.259)

    # Add extra rate if hours are more than 1000
    if hours > 1000:
        hours_after_1000 = hours - 1000
        bill_before_1000 = 1000 * rate_before_1000
        bill_after_1000 = hours_after_1000 * rate_after_1000
        bill = bill_before_1000 + bill_after_1000

    else:
        bill = hours * rate_before_1000
    
    # round() function is used to round decimal numbers. In this case to two decimal places
    return round_up(bill,2)

# Do not execute the code 
if __name__ == "__main__":
    main()