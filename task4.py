n = int(input("Enter the number of row :"))

#1st pattern
for i in range(n):
    print('1' * i)

#2nd pattern

num=1
for i in range(1,n+1):
    for j in range(1, i+1):
        print(num,end=" ")
        num=num+1
    print()

#3rd pettern

for i in range(n, 0, -1):
    print('*' * i)

#4th pattern
m=n-1

for i in range(n):
    for j in range(m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print(" *", end="")
    print('\r')

#5th pattern





