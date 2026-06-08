# def recurse(n):
#     if n==0:
#         return n
#     print(n, end=" ")
#     recurse(n-1)

# a=5
# recurse(a)

# def recurse(n):
#     if n==6:
#         return n
#     print(n, end=" ")
#     recurse(n+1)

# a=1
# recurse(a)

# def recurse(n):
#     if n==0:
#         return n
#     print(n, end=" ")
#     recurse(n-2)
# a=10
# recurse(a)

# def recurse(n):
#     if n==12:
#         return n
#     print(n, end=" ")
#     recurse(n+2)
# a=2
# recurse(a)

# def recurse(n):
#     if n==0:
#         return 
#     if n%2==0:
#         print(n, end=" ")
#     recurse(n-1)
#     if n%2==0 and n>3:
#         print(n, end=" ")
# a=10
# recurse(a)

# def recurse(n):   
#     if n==0:
#         return 
#     print(n,end=" ")
#     recurse(n-1)
#     if n>1:
#         print(n,end=" ")
# a=5
# recurse(a)


# def recurse(n):
#     if n==0:
#         return 200
#     x=recurse(n-1)
#     print(n,end=" ")
#     return x
# x=recurse(5)
# print(x)
    

def recurse(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    recurse(n,m+1)
    print(m+1,end=" ")
n=5
recurse(n)