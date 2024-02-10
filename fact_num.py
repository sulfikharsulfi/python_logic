"""factorial of a num """

def fact_num(item):
    if item == 0:
        return 1
    else:
        return item*fact_num(item-1)
    
num = int(input("enter a num: "))
print(f"factoriial of {num} is {fact_num(num)}")