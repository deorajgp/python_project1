"""

general utility functions 

"""
import random
import time

# returns parity of a function func after calling it on a list
# if the result of calling the function is even parity is 1 else 0
# funciton assumes that the list of integers is provided with num of elements greater than 0
def parity_checker(func , nums:list[int])->list[int]:
    result = func(nums)
    return [result % 2 == 0 , result]


#Take input from user the last number cant be zero
def take_input_of_n_integers(nums:list[int],mn_size = 1):
    while True:
        try:
            size = 0
            while size<mn_size:
                size = input("Enter the size of list ")
                size = int(size)
                if size<2:
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

            while nums[-1]==0:
                print("The last number cannot be zero so plzz enter something different")
                try:
                    ele = input("Enter the last number")
                    ele = int(ele)
                    nums[-1] = ele
                except ValueError:
                    print("Please enter an integer ")
            
            break

        except ValueError as e:
                print(e)

#executes the functions provided in functions line by line and checks if the result is even or odd
#if odd it appends an integer from 1 to 9 and re-evaluates it max of 3 times

def recurred_function(functions:list,temp:list,par:int)->int:
    for func in functions[:-1]:
        count = 0
        print(f"executing {func.__name__}")
        result =  parity_checker(func,temp)
        time.sleep(1)
        print(f"result obtained {result[1]}")
        parity = result[0] 
        time.sleep(1)

        while count<3 and parity==par: #no of times to append integer is 3 and we have to check till func generates even output

            temp.append(random.randint(1,10))
            print(f"function generated odd result ... appended an integer {temp[-1]}")
            time.sleep(1)
            result =  parity_checker(func,temp)
            print(f"result obtained {result[1]}")
            time.sleep(1)
            parity = result[0] 

            count+=1
        
        print(f"executed {func.__name__}")
        time.sleep(1)
    print(f"executing final function {functions[-1].__name__}")
    time.sleep(1)
    final_result = functions[-1](temp)
    return final_result
