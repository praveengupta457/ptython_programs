
x=int(input("enter you value: "))

match x:
    case 0:
        print("x is zero")

    case 1:
        print("the x is 1")
    case _:
        print("default case", x)

 