# Solution of challenge Polar Coordinates from Hackerrank

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Info on cmath module ->       https://www.w3schools.com/python/module_cmath.asp

# Take a complex number from STDIN and consider it as such
complex_num = complex(input())

# Convert the complex number to polar coordinates
print(cmath.polar(complex_num)[0])
print(cmath.polar(complex_num)[1])
