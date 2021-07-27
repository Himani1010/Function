def two_list(list):
    i= 0
    a=[]
    while i < len(list):
        if list2[i] in list1:
            a.append(list2[i])
        return a
list1 =[12, 312, 42, 123, 5]
list2 = [12, 53, 75, 123, 62, 9]
two_list(list1,list2)
print()
# num_list_sub_20 = numbers_less_than_twenty(num_list)
# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)



# def word(sentence):
# a=sentence.split()
# b=[]
# i=0
# while i<len(a):
#     b.append(a[i])
#     i=i+1
# print(b)
# word("you are my friends")