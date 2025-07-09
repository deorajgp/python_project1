import math

"""

helper functions to perform on the array of integers

"""



# function to perform addition of all the elements and return the sum
def add(nums:list[int])->int:
    return sum(nums)


#function to perform multiplication of all the elements and return the result
def mul(nums:list[int])->int:
    return math.prod(nums)

#function to perform division of first number with last number
def div(nums:list[int])->int:
    if nums[-1] == 0:
        raise ValueError("Cant divide by zero as last number is zero")
    
    return nums[0]//nums[-1]