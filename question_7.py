def my_function(n1,n2):
    if len(n1)>len(n2):
        print(n1)
    elif len(n1)==len(n2):
        print(n1,n2)
a=input("enter a text")
b=input("enter a text")
my_function(a,b)