num=list(input("Enter a sequence of comma seperated 4 digits binary number:").split(','))
res=[i for i in num if int(i,2)%6==0]
print(res)
         
