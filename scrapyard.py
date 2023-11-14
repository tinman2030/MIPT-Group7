import math
from itertools import combinations
import tkinter as tk

def adder(input1, input2):

    result = input1 + input2
    return((result))
#Worst case is 2^n, where n is the cardinality of our set, this is the max number of subsets of a set of size n(including null set)
#so we want to have the subsets to be at least 2, cause we want the sums
def make_subset(my_set, r):
    if r<2:
        raise ValueError("Subset size 'r' must be at least 2")
    subsets = combinations(my_set, r)
    return subsets

def summation(my_set, target):
    combos = []
    for i in range(1, len(my_set) +1):
        combos.extend(combinations(my_set,i))
    combos_list = [list(comb) for comb in combos]
    unique_combo_list = []

    [unique_combo_list.append(x) for x in combos_list if x not in unique_combo_list]
    count = 0
    for set in unique_combo_list:
        result = sum(set)
        if result == target:
            count += 1
            print(set)
    print(count)

def int_to_binary_list(n):
    # Convert the integer to a binary string
    binary_str = bin(n)

    # Remove the '0b' prefix from the binary string
    binary_str = binary_str[2:]

    # Create a list from the binary string
    binary_list = [int(bit) for bit in binary_str]

    return binary_list
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

def add_binary():
    bit1 = entry_bit1.get()
    bit2 = entry_bit2.get()

    try:
        # Convert binary strings to lists of integers
        bit1_list = [int(bit) for bit in bit1]
        bit2_list = [int(bit) for bit in bit2]

        # Perform binary addition step by step
        result = []
        carry = 0
        steps = []

        for i in range(len(bit1_list) - 1, -1, -1):
            sum_bits = bit1_list[i] + bit2_list[i] + carry
            result.insert(0, sum_bits % 2)
            carry = sum_bits // 2
            steps.append((list(bit1_list), list(bit2_list), carry, result.copy()))

        # Display the steps in the GUI
        display_steps(steps)

        # Display the final result in the result label
        result_label.config(text=f"Result: {''.join(map(str, result))}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter binary numbers.")

def display_steps(steps):
    # Create a new window for displaying steps
    step_window = tk.Toplevel(root)
    step_window.title("Binary Addition Steps")

    # Add labels for each step
    for step_num, step in enumerate(steps, 1):
        bit1_str = ''.join(map(str, step[0]))
        bit2_str = ''.join(map(str, step[1]))
        carry = step[2]
        result_str = ''.join(map(str, step[3]))

        step_label = tk.Label(step_window, text=f"Step {step_num}: {bit1_str} + {bit2_str} + {carry} = {result_str}")
        step_label.pack()

# Function to add binary numbers (as given in the previous response)

# GUI setup
root = tk.Tk()
root.title("Binary Adder")

# Entry widgets for binary numbers
label_bit1 = tk.Label(root, text="Binary Number 1:")
label_bit1.pack()
entry_bit1 = tk.Entry(root)
entry_bit1.pack()

label_bit2 = tk.Label(root, text="Binary Number 2:")
label_bit2.pack()
entry_bit2 = tk.Entry(root)
entry_bit2.pack()

# Button to perform addition
add_button = tk.Button(root, text="Add", command=add_binary)
add_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
