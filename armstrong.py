n=str(input())
arm=0
length=len(n)
for i in n:
    arm+=int(i)**length
if(arm==int(n)):
    print("armstrong")
else:
    print("not armstrong")