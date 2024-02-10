"""check a string is palindrom or not"""

def check_palindrom(item):
    reve_item = item[::-1]
    if reve_item == item:
        return True
    return False

test = input("enter a string: ")
if check_palindrom(test):
    print(f"the {test} is palindrome")
else:
    print(f"the {test} is not palindrome")