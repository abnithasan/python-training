l=[1,2,3,4,5,6,7]

k=int(input())
n=len(l)
k=k%n

def rotate(i,j):
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1

rotate(0,k)
rotate(k+1,n-1)
rotate(0,n-1)
print(l)