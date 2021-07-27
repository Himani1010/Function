i=0
c=0
def kbc(que):
    i=0
    while i<len(que):
        print(i+1, que[i])
        i+=1
que=[["what is the capital of India"],["capital of uttarakhand"], ["pink city of India"]]

def options(op):
    j=0
    while j<len((op[i])):
        print(j+1, op[i][j])
        j+=1
op=[["Dehli", "Punjab","Indore", "Banglore"],["Kotdwara","Rishikesh", "dehradun","haridwar"],["Kashmir", "Jaipur","Surat","Raipur"]]

def solution(Ans):
    c=0
    user=int(input("ener your answer: "))
    if user==Ans[i]:
        print("congratulations")
    elif user==5050:
        if c==0:
            k=0
            while k<len(fifty[i]):
                print(k+1, fifty[i][k])
                k+=1
            c+=1

            an=int(input("Choose your Answer"))
            if an==answer[i]:
                print("Correct Answer")
            else:
                print("wrong answer")
                # break
        else:
            print("you have already used lifeline")
            n=int(input("select your answer"))
            if n==solution[i]:
                print("congrats")
            else:
                print("You loss")
    else:
        print("You loss the game")
        # break           

Ans=[1, 3, 2]
fifty=[["Dehli", "Punjab"],["kotdwara","dehradun"],["jaipur", "Rishikesh"]]
answer=[1,2,1]
# def main():
kbc(que)
options(op)
solution(Ans)
# main()

