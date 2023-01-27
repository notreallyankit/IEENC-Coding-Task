def prime(x):
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
        
    else:
        return True

def hcf(n1,n2):
    if n1==0 or n2==0:
        return 0
    elif n1==n2:
        return n1
    elif n1>n2:
        return hcf(n1-n2,n2)
    elif n1<n2:
        return hcf(n1,n2-n1)

def coprime(n1,n2):
    if hcf(n1,n2)==1:
        return("Co-prime numbers")
    else:
        return("Not co-prime numbers")

def circular(N) :
    p=0
    m=N
    l=len(str(m))
    if prime(N):
        while p!=m:
            q=m//(10**(l-1))
            r=m%(10**(l-1))
            p=(r*10)+q
            if prime(p):
                m=p              
            else:
                return False
        return True
    else:
        return False
    
#Menu
ans="y" 
while ans=="y":
    print("""1. Check if it is prime number.
2.Check if it is coprime.
3. Check if it is circular prime.""")
    choice=int(input("Enter option number:"))

    if choice==1:
        num=int(input("Enter a number:"))
        s=prime(num)
        if s== True:
            print("It is a prime number.")
        else:
            print("It is not a prime number.")

    if choice==2:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        s=coprime(num1,num2)
        print(s)

    if choice==3:
        num=int(input("Enter a number:"))
        if circular(num):
            print("Circular prime")
        else:
            print("Not circular prime")

    ans=input("would you like to continue(y/n):")
