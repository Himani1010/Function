def perfact(a):
    i=1
    sum=0
    while i<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if a==sum:
        print("it is a prefect number")
    else:
        print("it is not prefect number")
a=int(input("enter any number"))
perfact(a)