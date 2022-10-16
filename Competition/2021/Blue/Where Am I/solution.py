# Intercollegiate Programming Competition 2021 Blue Track Problem 4
# Where Am I?

# Q1 -> (+,+)
# Q2 -> (-,+)
# Q3 -> (-,-)
# Q4 -> (+,-)

def main():
    """Run the program as a whole."""

    # Take the coordinates from STDIN and split it into a list
    coors = input("Enter X and Y separated by a space: ").split()

    # No need to convert coordinates to integers, just check if the '-' character is present
    # Check which coordinates are positives or negatives
    # Conditions for Q1
    if '-' not in coors[0] and '-' not in coors[1]:
        print("Q1")
    
    elif '-' in coors[0] and '-' not in coors[1]:
        print("Q2")
    
    elif '-' in coors[0] and '-' in coors[1]:
        print("Q3")
    
    else:
        print("Q4")

# Do not run this code if this script is imported by another Python file
if __name__ == "__main__":
    main()
