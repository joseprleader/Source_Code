# Solution of challenge Input() from Hackerrank

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Get data from STDIN and split it into a list
ui = input().split()

# Convert the first list element into an integer
x = int(ui[0])

# Evaluate the algebraic expression and check if it is equal to the second element of the list
print(eval(input()) == int(ui[1]))
