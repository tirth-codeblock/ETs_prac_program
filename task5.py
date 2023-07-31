num = int(input("enter the value :"))


for i in range(0,num+1):
    for j in range(0, num+1):
        if(i+j==num/2 or i-j==num/2 or j-i==num/2 or j+i==(num+(num/2)) or (i+j>=num/2 and j-i<=num/2 and i<num/2) or (i-j<num/2 and j+i<=(num+(num/2)) and  i>=num/2)):
            print('*', end='')
        else:
            print(end=" ")
    print()