def my_function(list):
    i=0
    count=0
    while i<len(list):
        if list[i][0]==list[i][-1]:
            count+=1
        i+=1
        # b=str(list[i])
        # a=str(list[i])
        # if b[0]==a[0]:
        #     count=count+1
    print(count)
list=['abc', 'xyz', 'aba', '1221','bcb']
my_function(list)