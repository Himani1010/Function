def my_function(num):
    i=1
    f=0
    while i<=num:
        if num%i==0:
            f=f+1
        i+=1
    if f==2:
        print(num,"prime number")
    else:
        print(num,"not prime number")
def prime():
    i=1
    while i<=50:
        my_function(i)
        i+=1
prime()
