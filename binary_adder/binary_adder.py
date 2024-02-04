import math
from itertools import combinations
#getting the different combinations of a list
def make_combos(my_set):
    my_set = [x for x in my_set if x != 0]

    if len(my_set) < 2:
        raise ValueError("Size of the set must be greater than 2")

    combos = []
    for i in range(2, len(my_set) +1):
        combos.extend(combinations(my_set,i))
    combos_list = [list(comb) for comb in combos]
    unique_combo_list = []

    [unique_combo_list.append(x) for x in combos_list if x not in unique_combo_list]

    return unique_combo_list
#doing the binary addition as we do in the adder
def add_binary_numbers(bit1, bit2):
    carry = 0
    result = []

    # Make sure both input lists have the same length by adding zeros to the front of the shorter one
    max_len = max(len(bit1), len(bit2))
    bit1 = [0] * (max_len - len(bit1)) + bit1
    bit2 = [0] * (max_len - len(bit2)) + bit2

    for i in range(max_len - 1, -1, -1):
        sum_bits = bit1[i] + bit2[i] + carry
        result.insert(0, sum_bits % 2)  # Insert the least significant bit to the front
        carry = sum_bits // 2  # Set the carry for the next iteration

    if carry:
        result.insert(0, carry)  # If there's a carry after all iterations, add it to the front

    return result
#Converting a list of decimal numbers to make a list of binarys numbers
def decimal_to_binary_list(numbers):
    binary_list = []
    
    for num in numbers:
        if num < 0:
            raise ValueError("Input numbers must be positive integers.")
        binary_representation = []
        
        # Handle the case of zero separately
        if num == 0:
            binary_representation.append(0)
        else:
            while num > 0:
                binary_representation.insert(0, num % 2)
                num = num // 2
        
        binary_list.append(binary_representation)
    
    return binary_list
#Take a list of decimal integers and converts them to binary, and adds them in binary and then returns the sum of a list... in binary
def add_decimal_numbers_in_binary(numbers):
    binary_list = decimal_to_binary_list(numbers)
    result_binary = [0]  # Initialize the result to 0 in binary

    for binary in binary_list:
        result_binary = add_binary_numbers(result_binary, binary)

    return result_binary
def make_sublists(list,n):
    i = 0
    big_list = []
    while i*n < len(list):
        big_list.append(list[i*n:(i+1)*n])
        i += 1
    big_list.append(list[i*n:])

    return big_list


def main():
    user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string by spaces and convert the substrings into integers
    try:
        numbers = [int(num) for num in user_input.split()]
        print("You entered:", numbers)
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
    #making the combos
    combinations = make_combos(numbers)
    
    print(make_sublists(combinations,8))

    
if __name__ == "__main__":
    main()
