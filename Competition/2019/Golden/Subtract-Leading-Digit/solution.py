# Given a starting and ending number, on a loop substract the first digit of each number until the number is
# equal or less than the ending number
def main():
    
    print("Enter the starting number:")
    n1 = int(input())

    print("Enter the ending number:")
    n2 = int(input())

    print(f"{substact_1_digit(n1, n2)} numbers in sequence")

def substact_1_digit(n1, n2):

    # Set the current number that'll go through the loop
    curr_n = n1

    # Set a variable for the times we've run this loop
    times_run = 0
    while curr_n > n2:

        # Increase the times loop has been run by 1
        times_run += 1
        # Substract this number by the first digit
        curr_n -= int(str(curr_n)[0])
    
    return times_run

main()