# Intercolligiate Programming Competition Gold Track Challenge # 4
# Reverse the Array (Many Times)

# Steps
# 1) Add each number, one at a time, to the end of the new array
# 2) Then reverse the order of the numbers in the new array.
# 3) Repeat this for each number added

def main():
    """Run the program as a whole."""

    new_arr = []

    nums = stdin()

    for num in nums:
        new_arr.append(num)
        new_arr.reverse()
    
    print(new_arr)

def stdin():
    """Return input from STDIN."""

    count_n_nums = input("Enter count, integers separated by a space:\n")
    
    nums = count_n_nums[2:]

    nums = nums.split(" ")

    # Python map function
    # It's used in place of a for loop to perform the same operation across all elements of a list
    # lambda function -> Anonymous Python function

    # map function python referece: https://www.w3schools.com/python/ref_func_map.asp
    # lambda python referece: https://www.w3schools.com/python/python_lambda.asp

    # The code below is equivalent to the following code:

    # for i in range(len(nums)):
    #   nums[i] = int(nums[i])

    nums = map(lambda n: int(n), nums)
    
    return list(nums)


if __name__ == "__main__":
    main()