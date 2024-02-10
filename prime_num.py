"""check a number is prime number or not"""

def check_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int((num**0.5)+1)):
            if num % i == 0:
                return False
            else:
                return True
            

number = int(input("enter a number :"))
if check_prime(number): 
    print(f"the given num {number} is prime")
print("not prime")