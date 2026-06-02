l1=input().split()
for i in range(len(l1)):
    if l1.count(i)>1:
        l1.remove(i)
l1.sort()
print(l1)