def my_question(number):
    i=0
    c=0
    while i<len(number):
        if number[i]>c:
            c=number[i]
        i=i+1
        print(c)
my_question(number=[3,5,7,34,2,89,5])