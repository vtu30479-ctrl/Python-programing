list=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    list.append([name,score])
second_highest=sorted(set([score for name,score in list]))[1]
print('\n'.join(sorted([name for name,score in list if score==second_highest])))
               
