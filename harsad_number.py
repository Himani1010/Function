def harshad_number(num):
    sum=0
    n=num
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if n%sum==0:
        return n,"harshad number"
    else:
        return "not a harshad"
def harshad():
    i=1
    while i<=100:
        print(harshad_number(i))
        i+=1
harshad()