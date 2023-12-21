myList = []
n = int(input("Enter number of elements to be input into the list\n"))
for i in range(0,n):
    print("Enter element",i+1,": ",end='')
    element = int(input())
    myList.append(element)
print("\nThe input list is",myList)
sum = 0
for i in range(0,n):
    sum = sum + myList[i]
average = float(sum/n)
print("The average of the entered values is",round(average,6))
