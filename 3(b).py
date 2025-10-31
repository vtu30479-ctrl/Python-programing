from math import pow
def compute_armstrong(x):
    n = len(str(x)) 
    armstrong_sum = sum(pow(int(i), n) for i in str(x))
    return armstrong_sum == x
number = int(input("Enter a number: "))
if compute_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
