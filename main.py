from helpers.math_utils import *
from helpers.general_utils import *
"""
check even odd condition based on the result of given function and do append to rerun that function til a particular parity is reached 
in this case even

"""

#storage for list of integers
nums = []

#enter the size of nums
take_input_of_n_integers(nums,2)


functions = [add,mul,div]
temp = nums.copy()

result = recurred_function(functions,temp,0)#functions contain list of functions and  temp is list of numbers and 0 is parity

print(f"original list {nums}")
print(f"final list {temp}")
print(f"final result {result}") 