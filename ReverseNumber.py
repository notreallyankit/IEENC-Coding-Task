def rev(x):
    sol=0
    while x>0:
        r=x%10
        sol=sol*10+r
        x=x//10
    return sol

print("TO PRINT REVERSE OF A NUMBER")
num=int(input("Enter a number:"))
ans=rev(num)
print("Reverse of the number is:",ans)