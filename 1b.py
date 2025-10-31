def calculate_total_cost(X,Y):
    return X*Y

t = int(input('Enter number of test cases: '))


for _ in range(t):
    
    X, Y = map(int, input("Enter weeks and cost per week: ").split())
    
    
    total_cost = X * Y
    
    
    print('Total amount to pay:', total_cost)

    
    
        
    
