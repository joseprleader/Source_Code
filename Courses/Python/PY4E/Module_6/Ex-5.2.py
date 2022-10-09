# PY4E Module 6: Loops and Iterations Exercise 5.2 

# Input 7, 2, bob, 10 and 4, done to pass the challenge

def main():
    """Run the program as a whole."""

    largest = None
    smallest = None

    # Keep track of loop iterations
    count = 0

    while True:
        num = input("Enter a number: ")
        if num == "done":
            break

        else:
            try:
                num = int(num)
            
            except ValueError:
                print("Invalid input")
                continue
            
            else:
                
                if count == 0:
                    min_num = num
                    max_num = num
                
                elif num < min_num:
                    min_num = num
                
                elif num > max_num:
                    max_num = num
                
                else:
                    pass

                # Only count loop iterations when actual numbers have been entered by the user
                count += 1

    if num != "done":
        print(num)
    
    print("Maximum is " + str(max_num))
    print("Minimum is " + str(min_num))

# Do not run the program when it is imported by another python file
if __name__ == "__main__":
    main()
