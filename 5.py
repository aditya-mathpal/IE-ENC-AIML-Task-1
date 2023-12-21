print("This program compares 3 values")
a = []
for i in range(1,4):
    print("Enter value",i,": ",end='')
    b = float(input())
    a.append(b)
print("\nYour input numbers are",a)

def compare(x,y):
    print(x,end='')
    if(x>y):
        print(" is greater than ",end='')
    elif(x<y):
        print(" is lesser than ",end='')
    else:
        print(" is equal to ",end='')
    print(y)
i=0
while(i<2):
    compare(a[i],a[i+1])
    i += 1
compare(a[0],a[2])

