# IPC 2019 Problem 1: Number Frequency

# Only consider numbers from 1 to 100

def main():
    # Make a dictionary to count how many times each number happens
    num_n_times = {}

    # Get data from STDIN and process it
    nums = get_n_process_STDIN_data()

    # Loop through all elements in nums array
    for num in nums:    
        # If element is in dict, add 1 to it
        try:
            num_n_times[num] += 1
        
        # If element is not in dict, add a count of 0 to it
        except KeyError:
            num_n_times[num] = 1
        
    # Loop through the count dict
    for key, value in num_n_times.items():
        print(f"{key} occurs {value} times")

def get_n_process_STDIN_data():
    """Get data from STDIN and get it ready to use."""

    print("Enter your numbers separated by a space")

    # Get input from the user
    nums = input()

    # Convert the input into a list of items separated by space
    nums = nums.split()

    # Make a list of integers with numbers that are in the range 1-100
    nums = [int(num) for num in nums if int(num) >= 1 and int(num) <= 100]

    # Sort the list of numbers from lowest number to greatest number
    nums.sort()

    return nums

main()