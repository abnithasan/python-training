#dynamic sliding window where the number of the subarray with the max value(length-wise) is returned
#in this problem, subarray 4 has the max length of elements 
l1=[2,1,6,2,1,2,4,7,8,1,2]
k=10
r,l,s,m=0,0,0,0
while r<len(l1):
    s+=l1[r]
    while s>k:
        s-=l1[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)