# Module 5 of PY4E: Conditional Statements Exercise 4.6

# Enter 45 hours and 10.50 as the hourly rate

# From now on we'll encapsulate our main code (The one that makes everything work) in the main() function

# Its advantages are that you don't have to worry about where you declare your functions and that you may see
# what a program really does from the start by declaring the main() function first.
# It also let's us filter what code gets executed when we import external python files which will be covered later.

# Recommendation: Always write docstrings for your function, except for when they are redundant.

def main():
    """Run the whole program as a whole."""

    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Hourly Rate: "))
    p = computepay(hrs, rate)
    print("Pay", p)

def computepay(h, r):
    """Calculate the total pay due to a employer."""
    if h > 40:
        normal_pay = 40 * r
        extra_hours = h - 40
        extra_rate = r * 1.5
        extra_pay = extra_hours * extra_rate
        pay = normal_pay + extra_pay
    
    else:
        pay = h * r
    
    return pay

# Execute the code only when this program is run directly and not imported from another python file
if __name__ == "__main__":
    main()