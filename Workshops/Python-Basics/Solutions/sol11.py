"""Get how many times the numbers 50 appears in the tuple."""

def main():
    """Run the program as a whole."""

    nums = (30,50,20,10,50,30,40,40,20,50,80,100,50)

    # Count how many times the number 50 occurs in this tuple
    times_50 = nums.count(50)

    print(times_50)

if __name__ == "__main__":
    main()