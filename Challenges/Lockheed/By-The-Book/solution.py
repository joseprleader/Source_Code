# Problem 6: By the Book

# Goal: Check an ISBN is valid

def main():

    n = int(input())

    for i in range(n):

        isbn = input()
        isbn_nums = isbn_digits(isbn)
        print(isbn_validity(isbn_nums))

def isbn_digits(isbn):
    """Return each digit of an isbn in a list."""

    isbn_digits = []

    for char in isbn:

        if char == "X":
            char = 10
        
        isbn_digits.append(int(char))
    
    return isbn_digits

def isbn_validity(isbn_nums):
    """Check an ISBN is valid."""

    len_isbn = len(isbn_nums)

    total = 0
    newTotal = 0

    for i in range(len_isbn - 1):

        current = isbn_nums[i] * (len_isbn - i)
        total += current
    
    newTotal = total
    
    while newTotal % 11 != 0:
        newTotal += 1
    
    diff = newTotal - total

    if diff == isbn_nums[-1]:
        return "VALID"
    
    else:
        return "INVALID"
    
main()