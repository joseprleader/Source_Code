# Determine how many one bits are present in a number of base 10
# Determine how many numbers between zero and the given number have the same number of one bits

import sys

def main():
    
    nums = get_data_from_file(sys.argv[1])

    for num in nums:

        bin_rep = get_binary_str(num)
        one_bits = get_nums_of_1_bits(bin_rep)

        # Get number of numbers between 0 and num that have the same number of 1 bits
        between_nums = list(range(1, num))
        same_1_bits = lambda between_num : get_nums_of_1_bits(get_binary_str(between_num)) == one_bits
        nums_equal_1s = len(list(filter(same_1_bits, between_nums)))

        # Print result to the console
        print(f"{num} has {one_bits}-1 bits. There are {nums_equal_1s} other numbers with {one_bits}-1 bits between 0 and {num}.")

def get_data_from_file(file_name):

    with open(file_name) as f:
        lines = f.readlines()
    
    return list(map(int, lines))

def get_nums_of_1_bits(bin_num):

    is_1_bit = lambda bit : bit == "1"

    return len(list(filter(is_1_bit, bin_num)))

def get_binary_str(num):

    return format(num, 'b')

main()