import math
from itertools import combinations
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
combos = [-86, -54, -22, -4, -1, 0, 2, 2 ,5, 7, 14 ,52, 91 , 109]
summation(combos, 243)

