"""largest num of a list"""

def largest_num(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

list_num = [3,2,4,1,5]
print(f"the largest num of {list_num} is {largest_num(list_num)}")