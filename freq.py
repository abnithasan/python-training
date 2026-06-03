l=[1,3,1,3,1,2,1,4,2,2,2,2,2]
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)            
