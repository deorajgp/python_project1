import random
import helpers.general_utils
from helpers.math_utils import *
from helpers.general_utils import *
from typing import List
"""
check even odd condition based on the result of given function and do ammendments according to that

"""

#storage for list of integers
nums = []

#enter the size of nums
while True:
    try:
        size = input("Enter the size of list")
        size = int(size)
        break
    except ValueError:
        print("Please enter an integer")

#enter the elements of nums
while len(nums)!=size:
    try:
        ele = input(f"Enter element number {len(nums) + 1}")
        ele = int(ele)
        nums.append(ele)
    except ValueError:
        print("Please enter an integer")


functions = [add,mul,div]
temp = nums.copy()

for func in functions:
    nums_copy = temp.copy()
    count = 0
    parity = parity_checker(func,nums_copy)
    while count<3 and parity==0: #no of times to append integer is 3 and we have to check till func generates even output
        nums_copy.append(random.randint(1,100))
        parity = parity_checker(add,nums_copy)
    if parity == 1:
        temp = nums_copy
    
    print(f"executed {func.__name__}")

print(f"final list {temp}")
        