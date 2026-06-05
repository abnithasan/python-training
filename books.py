l=[2,1,3,1,3,4,2,1,3,4,6,7,8,1,2]
k=3
n=len(l)
s=sum(l[:k])
m=s
for i in range(1,n-k+1):
    s=s-l[i-1]+l[i+k-1]
    m=max(m,s)     
print(m)