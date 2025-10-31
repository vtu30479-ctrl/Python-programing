def get_age():
    while True:
        try:
            age=int(input('Enter your age:'))
            if age<0:
                raise ValueError('Age cant be negative')
            return age
        except ValueError as ve:
            print('Invalid input:',ve)
try:
    age=get_age()
    print('Your age is:',age)
except:
    print('AN error occured:',ve)
        
            
