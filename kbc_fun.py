def my_que(a):
    i=0
    while i<len(a):
        print(i+1,a[i])
        i=i+1
def my_option(b):
    i=0 
    j=0
    while j<len(b[j]):
        print(j+1,b[j][i])
        j=j+1
        i=i+1
def my_solution(c):
    k=0
    if user==solution[k]:
        print("congratulations")
    else:
        print("you loss the game")
    

    
que=["How many girls in your class",
    "what is capital of uttarakhand",
    "pink city of indai"]
my_que(que)


option=[["four", "nine", "seven", "eight"],["Dehradun", "kotdwara", "dugadda", "Rishikesh"],["Agra", "Jaipur", "Kashmir", "Banglore"]]
my_option(option) 

user=int(input("enter any answer :"))
solution=[3,1,2]
my_solution()


