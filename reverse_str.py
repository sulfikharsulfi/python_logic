"""find revers of a string """

def rev_str(item):
    return item[::-1]

test = input("enter a string")
print(f"the reverse of {test} is {rev_str(test)}")