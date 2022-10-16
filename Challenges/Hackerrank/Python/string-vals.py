# Solution of challenge String Validators from Hackerrank

# Info on the any() Python function -> https://www.w3schools.com/python/ref_func_any.asp
# Info on list comprehension ->        https://www.w3schools.com/python/python_lists_comprehension.asp

if __name__ == '__main__':
    s = input()

    # Check if there is any alphanumeric character in the string s
    print(any(char.isalnum() for char in s))

    # Check if there is any alphabetic character in the string s
    print(any(char.isalpha() for char in s))

    # Check if there is any numeric character in the string s
    print(any(char.isdigit() for char in s))

    # Check if there is any lowercase characters in the string s
    print(any(char.islower() for char in s))

    # Check if there is any uppercase characters in the string s
    print(any(char.isupper() for char in s))
    