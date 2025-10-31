def categorize(tid): 
    adult = list(filter(lambda x: x % 2 == 0, tid)) 
    child = list(filter(lambda x: x % 2 != 0, tid)) 
    return adult, child
tid = [101, 202, 305, 410, 513, 620, 723, 830, 945, 1050] 
adult, child = categorize(tid) 
print("Adult Tickets:", adult) 
print("Child Tickets:", child) 
