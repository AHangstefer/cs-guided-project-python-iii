"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice 
except except for one. Write a function that finds the element that only 
appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    for num in nums:
        if nums.count(num) == 1:
            return num


#Search for the only unique number
#use function like count()
#or loop over each other item to see if theres duplicates
#maybe it returns boolean
print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))

#or we can make a dictionary and add numbers that haven't been repeated

def single_number(nums):
    single_number_dict = {}

    for num in nums:
        #check if we have seen the number already
        if num in single_number_dict:
            single_number_dict[num] += 1
        else:
            #otherwise if first time seeing the numebr
            single_number_dict[num] = 1

    print(single_number_dict)
    #Find the numer thats only seen once
    for key, value in single_number_dict.items():
        if value == 1:
            return key 

print(single_number([5,2,3,2,3]))
   

