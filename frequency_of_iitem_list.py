"""frequancy of item in a list"""

def freequency_num(items):
    frequency_i = {}
    for item in items:
        if item not in frequency_i:
            frequency_i[item] = 1
        else:
            frequency_i[item] += 1
    return frequency_i

test = [1,3,4,5,6,4,3,2,5,6,4,2]
print(f"the frequeny of items from{test} is {freequency_num(test)}")