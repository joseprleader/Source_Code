# Intercollegiate Programming Competition 2021 Blue Track Problem 3
# Largest Quotient

def main():
    """Run the program as a whole."""

    # Get numbers separated by a space, the last 0 is the end.
    print("Enter integers separated by a space.")
    nums = input("End with 0: ")
    nums_list = format_data(nums)
    
    # Print the maximum quotient
    print(largest_quotient(nums_list))

def format_data(nums_string):
    """Convert the given string of numbers to a list of numbers."""
    
    # Split the string into a list
    nums_list = nums_string.split()

    # Exclude the last number, a 0.
    nums_list = nums_list[:-1]

    # Convert all strings digits to integers
    for i in range(len(nums_list)):
        nums_list[i] = int(nums_list[i])
    
    # Return the list to the user
    return nums_list

def largest_quotient(nums_list):
    """Return the largest quotient from a list of numbers."""

    # Get the largest number from the list
    max_num = int(max(nums_list))

    # Get the minimum number from the list
    min_num = int(min(nums_list))

    # Divide both numbers and get the largest quotient
    max_quotient = max_num / min_num

    # Return the maximum quotient
    return int(max_quotient)

# Do not run this code if this script is imported by anohter Python file
if __name__ == "__main__":
    main()
