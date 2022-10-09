# Solution for Lists Python challenge from Hackerrank

# Do not run this program if this file is imported by another Python File
if __name__ == '__main__':

    # Take a number from STDIN
    N = int(input())
    
    # Initialize an empty list to insert numbers into it. We'll call it crazy list from now on
    crazy_list = []
    
    # Loop through all integers from 0 to N
    for i in range(N):
        
        # Extract a command from STDIN and split it to a list 
        # Ex: The string "I am the best" becomes the list ["I", "Am", "the", "best"]
        command = input().split(" ")
        
        # If the insert command comes from STDIN, then insert to the crazy list the 2nd and 3rd elements of the command list
        if 'insert' in command:
            crazy_list.insert(int(command[1]),int(command[2]))
        
        # If the print command comes from STDIN, print the crazy list
        elif 'print' in command:
            print(crazy_list)
        
        # If remove comes from STDIN, then remove from the crazy list the 2nd element of the command list 
        elif 'remove' in command:
            crazy_list.remove(int(command[1]))
        
        # If append comes from STDIN, then append to the crazy list the 2nd element of the command list
        elif 'append' in command:
            crazy_list.append(int(command[1]))
        
        # If sort comes from STDIN, sort the crazy list from least to greatest
        elif 'sort' in command:
            crazy_list.sort()
        
        # If pop comes from STDIN, then remove the last element of the crazy list
        elif 'pop' in command:
            crazy_list.pop()
        
        # In all other cases, reverse the order of the crazy list
        else:
            crazy_list.reverse()
        