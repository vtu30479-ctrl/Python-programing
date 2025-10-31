p=int(input('Enter the principal amount:'))
r=int(input('Enter the rate amount:'))
t=int(input('Enter the time in years:'))
CI=p*((1+r/100)**t)-p
print('The compound interest is:',CI)
