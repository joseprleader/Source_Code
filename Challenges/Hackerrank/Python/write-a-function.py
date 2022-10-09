# Solution of challenge Write a function from Hackerrank

def is_leap(year):
    """Return True if the given year is a leap year. Otherwise, return False."""

    # If the given year is not divisible by 4, it is not a leap year.
    if year % 4 != 0:
        return False
    
    # Otherwise, if the given year is divisible by 4 ...
    else:

        # If the year is not divisible by 100, is it a leap year
        if year % 100 != 0:
            return True
        
        # If the year is divisible by 400, it is also a leap year
        elif year % 400 == 0:
            return True
            
        # Return false for all other cases
        else:
                return False
