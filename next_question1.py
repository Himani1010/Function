def eligible_for_vote(a):
    if a<18:
        print("not elible for vote")
    else:
        print("elible for vote")
a=int(input("enter a number"))
eligible_for_vote(a)