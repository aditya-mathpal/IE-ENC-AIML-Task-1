while True:
    operation = input("Enter the operation you want to perform: +, -, x, /\n")
    match operation:
        case "+":
            a = float(input("Enter the values\n"))
            b = float(input("+ "))
            print("=",round(a+b,6))
        case "-":
            a = float(input("Enter the values\n"))
            b = float(input("- "))
            print("=",round(a-b,6))
        case "x":
            a = float(input("Enter the values\n"))
            b = float(input("x "))
            print("=",round(a*b,6))
        case "/":
            a = float(input("Enter the values\n"))
            b = float(input("/"))
            print("=",round(a/b,6))
        case _:
            print("That's not a valid operation")
