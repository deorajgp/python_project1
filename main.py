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
take_input_of_n_integers(nums)


functions = [add,mul]
temp = nums.copy()

#executes the functions provided in functions line by line and checks if the result is even or odd
#if odd it appends an integer from 1 to 9 and re-evaluates it max of 3 times
for func in functions:
    count = 0
    print(f"executing {func.__name__}")
    result =  parity_checker(func,temp)
    print(f"result obtained {result[1]}")
    parity = result[0] 

    while count<3 and parity==0: #no of times to append integer is 3 and we have to check till func generates even output

        temp.append(random.randint(1,10))
        print(f"function generated odd result ... appended an integer {temp[-1]}")
        result =  parity_checker(func,temp)
        print(f"result obtained {result[1]}")
        parity = result[0] 

        count+=1
    
    print(f"executed {func.__name__}")

final_result = div(temp)

print(f"original list {nums}")
print(f"final list {temp}")
print(f"final result {final_result}")
        