def calculator(a,b):  
    i=0
    while i<len(a) and len(b):  
        if c=="+":
            print(a[i]+b[i])
        elif c=="-":
            print(a[i]-b[i])
        elif c=="*":
            print(a[i]*b[i])
        elif c=="/":
            print(a[i]/b[i])
        elif c=="//":
            print(a[i]//b[i])
        elif c=="%":
            print(a[i]%b[i])
        else:
            print("error")
        i=i+1

a=[5, 10, 50, 20]
b=[2, 20, 3, 5]
c=input("enter a symble ")
calculator(a,b)