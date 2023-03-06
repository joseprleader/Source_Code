

def main():
    
    digits, weights = get_n_process_STDIN_data()
    weighted_sum = 0

    for i in range(len(digits)):

        product = digits[i] * weights[i]
        weighted_sum += product

    print(f"weighted sum is {weighted_sum}")

def get_n_process_STDIN_data():

    print("Enter the number:")
    num = input()
    weight = 0

    digits = []
    weights = []

    for char in num:
        weight += 1
        digits.append(int(char))
        weights.append(weight)
    
    return digits, weights

main()