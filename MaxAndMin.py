l=[]

def maxi(t):
    f=0
    for i in t:
        if i>=f:
            f=i
        else:
            continue
    return f

def mini(p):
    y=maxi(p)
    for i in p:
        if i<=y:
            y=i
        else:
            continue
    return y

n=int(input("Enter number of inputs:"))
for i in range(1,n+1):
    a=int(input("Enter a number:"))
    l.append(a)

ma=maxi(l)
mi=mini(l)
print("Maximum element of array is:",ma)
print("Minimum element of array is:",mi)