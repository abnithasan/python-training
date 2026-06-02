n=int(input())
temp=n
length=1
s=0
while(temp>0):
    digit=temp%10
    s+=digit**length
    temp//=10
    length+=1

print(s)