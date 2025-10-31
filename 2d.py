def count_even_odd(num):
    even_count=0
    odd_count=0
    for n in num:
        if n%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
input_numbers=input("Enter a series of numbers seperated by space:")
num=list(map(int,input_numbers.split()))
even_count,odd_count=count_even_odd(num)
print('No.of even numberss:',even_count)
print('no.of even numbers:',odd_count)
            
