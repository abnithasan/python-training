password="Abnitha67a#"
u,l,space,s,d=False,False,False,False,False

for i in password:
    if i.isupper():
        u=True
    elif i.islower():
        l=True
    elif i.isspace():
        space=True
    elif i.isdigit():
        d=True
    else:
        s=True

if len(password)>8 and u and l and d and s and not space:
    print("Valid")
else:
    print("Invalid")
