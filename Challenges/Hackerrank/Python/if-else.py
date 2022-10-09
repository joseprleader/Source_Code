# Solution to Python If-Else from Hackerrank

#!/bin/python3


# THESE MODULES ARE NOT REQUIRED, BUT THEY WILL APPEAR IN YOUR CHALLENGE SO I LEFT THEM THERE
import math
import os
import random
import re
import sys

# Do not run this program if it in imported by another Python File
if __name__ == '__main__':

    # Get the integer from STDIN and cut off spaces if any
    n = int(input().strip())
    
    # If the integer is odd, print "Weird"
    if n % 2 != 0:
        print("Weird")
    
    # If the integer is even ...
    else:
        # If the even number is between 2 and 5 print "Not Weird"
        if n in range(2, 5 + 1):
            print("Not Weird")
        
        # Otherwise, if the even number is between 6 and 20 print "Weird"
        elif n in range(6, 20 + 1):
            print("Weird")
        
        # Print "Not Weird" in all other cases
        else:
            print("Not Weird")
