mytuple = tuple(input("Enter 5 space separated fruits\n").split())
print("The generated tuple is ", mytuple, "\n")
mytuple2 = mytuple
mytuple2 += tuple(input("Enter another fruit to update the tuple\n").split())
print("\nThe original tuple was", mytuple, "and the new tuple is", mytuple2)