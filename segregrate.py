l=input().split() # 6 2 1 4 3 7 5
l.sort() #1 2 3 4 5 6 7
res=[]
for i in l:
    if i%2!=0:  #odd numbers are added in the end
        res.append(i)
    else:   #even numbers are added to the front
        res.insert(0,i)
print(res)