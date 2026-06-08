
def reduce(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+reduce(n//2)
    else:
        return 1+min(reduce(n-1),reduce(n+1))


n=15
print(reduce(n))