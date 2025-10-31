def op_decorator(func):
    def wrapper(x,y):
        print('Performing arithmetic operation:')
        result=func(x,y)
        print('operation completed')
        return result
    return wrapper
@op_decorator
def add(x,y):
    return x+y
@op_decorator
def divide(x,y):
    if y==0:
        return('Cant divide by zero')
    else:
        return x/y
result_add=add(5,3)
print('Result of addition:',result_add)
div=divide(15,0)
print('Result of division:',div)
