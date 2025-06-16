from typing import List

"""

general utility functions 

"""

# returns parity of a function func after calling it on a list
# if the result of calling the function is even parity is 1 else 0
# funciton assumes that the list of integers is provided with num of elements greater than 0
def parity_checker(func , nums:List[int])->List[int]:
    result = func(nums)
    return [result % 2 == 0 , result]

def take_input_of_n_integers(nums:List[int]):
    while True:
        try:
            size = input("Enter the size of list ")
            size = int(size)
            break
        except ValueError:
            print("Please enter an integer ")

    #enter the elements of nums
    while len(nums)!=size:
        try:
            ele = input(f"Enter element number {len(nums) + 1} ")
            ele = int(ele)
            nums.append(ele)
        except ValueError:
            print("Please enter an integer ")
