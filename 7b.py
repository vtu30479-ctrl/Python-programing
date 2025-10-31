def cube(n):
    prod=1
    for i in range(1,n+1):
        prod*=i**3
    return prod
n=int(input('Enter the value ofN:'))
result=cube(n)
print('Cube of first',n,'natural numbers is',result)
