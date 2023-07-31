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


# result
marks = int(input("Entre your marks :"))

if(90<marks<=100):
   print("Grade A")
elif(80<marks<=90):
   print("Grade B")
elif(60<marks<=80):
   print("Grade C")
elif(40<=marks<=60):
   print("Grade D")
elif(0<=marks<40):
   print("Fail")
else:
   print("Invalid Marks")