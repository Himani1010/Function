def min_function(list):
    i=0
    min=list[0]
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i=i+1
    print(min)
min_function(list=[8,6,4,-8,4,50,2,7])