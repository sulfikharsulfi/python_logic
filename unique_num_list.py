"""find unique numbers from a list"""


def find_unique_num(list1):
    unique_num_list = []
    for i in list1:
        if i not in unique_num_list:
            unique_num_list.append(i)
    return unique_num_list


list1 = [2,3,4,2,4,2,5,2,4,1]
print(f"find the unique num list {find_unique_num(list1)}")