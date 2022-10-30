# Intercollegiate Programming Competition 2021 Golden Track Problem 1
# Find the Missing Side

# Right Triangle Sides:
#       AB -> Cathetus
#       BC -> Cathetus
#       AC -> Hypothenuse

# Import the math module to deal with square roots
import math

# GLOBAL VARIABLE FOR TRIANGLE SIDES NAMES
SIDES_NAMES = ("AB", "BC", "AC")

def main():
    """Run the program as a whole."""

    # Get data from STDIN for the first side
    first_data = get_stdin_data("first")
    second_data = get_stdin_data("second")

    # Get the name of the thrid triangle side
    missing_name = get_name(first_data, second_data)

    # Get the length of the third triangle
    missing_length = get_length(first_data, second_data)

    # Show the results to STDOUT in the appropiate format
    print(f"{missing_name} {missing_length}")

def get_stdin_data(order_val):
    """Get data from STDIN for this challenge."""

    # Order val would be equal to first or second

    side = input(f"Enter {order_val} segment: ")
    length = int(input(f"Enter {order_val} length: "))

    # Return side and length as a tuple
    return side, length

def is_hypo(side_data):
    """Return true if side is hypothenuse, otherwise return false."""

    return "AC" in side_data

def get_name(first_data, second_data):
    """Get the name of the missing side of the triangle."""

    # Save the names of the given sides in a tuple
    given_sides = (first_data[0], second_data[0])

    # Loop through the list of all possible triangle side names
    for side_name in SIDES_NAMES:

        # If a side is not present in the tuple of given sides, return it.
        # For that is the name of the missing side
        if not side_name in given_sides:
            return side_name

def get_length(first_data, second_data):
    """Get the length of the missing side of the triangle."""

    # Store the given lengths in a tuple
    given_lengths = (first_data[1], second_data[1])

    # Check if any of the given sides is a hypothenuse
    first_hypo = is_hypo(first_data)
    second_hypo = is_hypo(second_data)

    # If none of the given sides are hypothenuse, then the missing side is a hypothenuse
    # If the missing side is a hypothenuse, use the formula:
    # math.sqrt(first_len ** 2 + second_len ** 2) to find its length
    if not (first_hypo or second_hypo):
        missing_side = math.sqrt(given_lengths[0] ** 2 + given_lengths[1] ** 2)
    
    # Otherwise, if the first side is the hypothenuse, then the missing side is a cathetus
    # If the missing side is a cathetus and the first a hypothenuse, use the following formula:
    # math.sqrt(first_len ** 2 - second_len ** 2)
    elif first_hypo:
        missing_side = math.sqrt(given_lengths[0] ** 2 - given_lengths[1] ** 2)
    
    # In all other cases, the second given side is the hypothenuse
    # Use the following formula to calculate the length of the missing side
    # math.sqrt(second_len ** 2 - first_len ** 2)
    else:
        missing_side = math.sqrt(given_lengths[1] ** 2 - given_lengths[0] ** 2)
    
    # math.sqrt() returns a float, drop all decimal places with math.floor()
    
    return math.floor(missing_side)

if __name__ == "__main__":
    main()