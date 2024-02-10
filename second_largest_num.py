"""find the second largest number from a list"""


def second_largest_num(list1):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in list1:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

list1 = [12,4,3,5,6,8,51,54]
print(f"the second largets num is {second_largest_num(list1)}")