import sys
from Square import Square

def main():
    
    # Get data from file
    size, values = get_data_from_file(sys.argv[1])

    # Create square and get its diagonals
    square = Square(size, values)

    diag_l, diag_r = square.diagonals

    # Get the sum of all diagonals
    diags_sum = sum(diag_l) + sum(diag_r)

    print(f"Sum of diagonals is {diags_sum}")
    
def get_data_from_file(file_name):

    with open(file_name) as f:

        data = f.read().split()
        size = int(data[0])
        values = list(map(int, data[1:]))

    return size, values

main()