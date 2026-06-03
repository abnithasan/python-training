l=[1,2,3,4]
last=len(l)-1

for i in range(len(l)//2):
    first=l[i]
    l[i]=l[last]
    l[last]=first
    last-=1
    
print(l)

