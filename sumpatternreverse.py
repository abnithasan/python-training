n=int(input())
temp=n
length=0
s=0
sd=0
while(temp>0):
    digit=temp%10
    length+=1
    temp//=10


while(n>0):
    sd=n%10
    s+=sd**length
    length-=1
    n//=10
print(s)
