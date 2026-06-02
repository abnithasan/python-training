l1=input().split()
l2=[]
for i in l1:
    if l1.count(i)%2!=0 and i not in l2:
        l2.append(i)
print(l2)