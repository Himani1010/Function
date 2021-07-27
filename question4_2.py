def add_numbers_list(a,b):
    i=0
    sum=0
    while i<len(a) and i<len(b):
        sum=a[i]+b[i]
        print(sum)
        i=i+1
a=[50, 60, 10] 
b=[10, 20, 13]
add_numbers_list(a,b)