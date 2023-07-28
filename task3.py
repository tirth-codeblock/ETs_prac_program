t=int(input("Enter a number :"))
s=10.5
if t>0:
    print("number is positive")
    if t %2==0:
        print("number is even")
        a=t*s
        print(a)
    else :
        print("number is odd")
        b=t+t
        print(b)

elif t<0 :
    print("number is negetive")
    if t %2==0:
        print("number is even")
        c=s/t
        print(c)
    else :
        print("number is odd")
        d=t-t
        print(d)
else :
    print("Invalid Input")

