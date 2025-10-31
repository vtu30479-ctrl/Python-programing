def fibonacci():
    a,b=0,1
    for _ in range (10):
        yield a
        a,b=b,a+b
fibonacci_series=fibonacci()
for number in fibonacci_series:
    print(number,end=" ")
