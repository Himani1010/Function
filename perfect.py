def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if sum==num:
        print(i,"Perfect number")
    else:
        print(i,"not perfect number")
def perfect_num():
    i=1
    while i<=1000:
        perfect(i)        
        i+=1
perfect_num()