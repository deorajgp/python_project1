from typing import List

"""

general utility functions 

"""

# returns parity of a function func after calling it on a list
# if the result of calling the function is even parity is 1 else 0
# funciton assumes that the list of integers is provided with num of elements greater than 0
def parity_checker(func , nums:List[int])->bool:
    result = func(nums)
    return result % 2 == 0
