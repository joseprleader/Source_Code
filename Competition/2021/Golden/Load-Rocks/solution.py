# IPC 2021 Gold Track Challenge #6
# Load Rocks

# Steps to solve this challenge
# 1) Get a list of all numbers less than the given weight
# 2) Iterate through them to find consecutive numbers that add up to the given weight
# 3) Store a combination of numbers in a list
# 4) Store all combinations in a list called combinations


def main():
    """Run the program as a whole."""

    weight = int(input("Enter weight of rock order: "))

    nums_less_weight = list(range(1,weight))

def sum_combos(nums, result):
    """Find all combinations of consecutive numbers that add up to a specific number."""

    combs = []

    # Start out with the smallest numbers and add them all up
    # If the result is less than what we're looking for, keep adding
    # If the result is the number we're looking for, then get the participating numbers and add them to a list
    # If the result is greater than the number we're looking for, start the sequence with the next number

    no_more_combs = False

    while not no_more_combs:

        searched_sum = 0

        for num in nums:

            # Keep track of the current combination of numbers
            current_comb = []

            if searched_sum < result:
                searched_sum += num
                current_comb.append(num)
            
            elif searched_sum == result:
                combs.append(current_comb)
                searched_sum = 0
                # clear out the list of current combinations
                current_comb.clear()
                # remove the first element of the list of numbers and keep on going
                nums.pop(0)
            
            else:
                searched_sum = 0
                # clear out the list of current combinations
                current_comb.clear()
                # remove the first element of the list of numbers and keep on going
                nums.pop(0)
            
            # If there is only one number in the list of numbers, there are no more possible
            # combinations, so, set no_more_combs to true
            if len(nums) < 2:
                no_more_combs = True
    
    return combs

if __name__ == "__main__":
    main()