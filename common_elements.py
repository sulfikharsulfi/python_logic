"""its a python program for finding common elemnts of two lists """

def common_elements(list1,list2):
    common = []
    for i in list1:
        if i in list2:
            if i not in common:
                common.append(i)
    return common

list1 = [1,2,4,5]
list2 = [2,6,3,7]

print(f"the common elemnts of list1 and list2 is {common_elements(list1,list2)}")