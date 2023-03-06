

def main():
    
    nums = get_n_process_STDIN()

    consec_nums = 0
    prev_num = None

    for num in nums:

        if num == prev_num:
            consec_nums += 1
        
        else:
            consec_nums = 0
        
        if consec_nums == 2:
            break

        prev_num = num
    
    if consec_nums == 2:
        print(f"Consecutive values found for {prev_num}")
    
    else:
        print("Consecutive values not found")


def get_n_process_STDIN():
    """Get and process STDIN data."""

    print("Enter your numbers separated by a space")
    numbers = input().split()
    numbers = [int(num) for num in numbers]

    return numbers

main()