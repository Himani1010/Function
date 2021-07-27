def calculator(a,b):      
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    elif c=="//":
        print(a//b)
    elif c=="%":
        print(a%b)
    else:
        print("error")

a=int(input("enter a number "))
b=int(input("enter a number "))
c=input("enter a symble ")
calculator(a,b)