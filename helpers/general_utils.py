from typing import List
import time

"""

general utility functions 

"""

# returns parity of a function func after calling it on a list
# if the result of calling the function is even parity is 1 else 0
# funciton assumes that the list of integers is provided with num of elements greater than 0
def parity_checker(func , nums:List[int])->List[int]:
    result = func(nums)
    return [result % 2 == 0 , result]


#Take input from user the last number cant be zero
def take_input_of_n_integers(nums:List[int],mn_size = 1):
    while True:
        try:
            size = 0
            while size<mn_size:
                size = input("Enter the size of list ")
                size = int(size)
                if size<mn_size:
                    print("Atleast size 2 must be provided")
                    continue
                else:
                    break

            #enter the elements of nums
            while len(nums)!=size:
                try:
                    ele = input(f"Enter element number {len(nums) + 1} ")
                    ele = int(ele)
                    nums.append(ele)
                except ValueError as e:
                    print("Please enter an integer ")
            #This part uses sleep function from time module in python for enhanced user experience       
            #https://www.programiz.com/python-programming/time/sleep
            while nums[-1]==0:
                print("The last number cannot be zero so plzz enter something different")
                time.sleep(2)
                try:
                    ele = input("Enter the last number")
                    ele = int(ele)
                    nums.append(ele)
                except ValueError:
                    print("Please enter an integer ")
        except ValueError as e:
                raise e
