# Solution to Loops Python challenge from Hackerrank

# Do not run this program if it is imported by another Python Program
if __name__ == '__main__':

    # Take a number from STDIN
    n = int(input())
    
    # Loop through numbers from 0 to n (excluding n)
    for i in range(0, n):
        # Print the square of the current number
        print(i ** 2)