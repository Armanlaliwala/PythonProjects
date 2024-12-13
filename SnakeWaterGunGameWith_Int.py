import random
def check(comp, user):
    if comp == user:
        return 0
        
    if (comp ==0 and user == 1) or (comp ==2 and user == 0) or (comp ==1 and user == 2):
        return -1
    
    return 1

comp = random.randint(0,2)
user = int(input("0 for snake, 1 for water, 2 for gun"))
if user < 0 or user > 2:
    print("Invalid input! Please enter 0, 1, or 2.")
else:
    print(f"user  = {user}")
    print(f"computer  = {comp}")
    score = check(comp, user)
    if score == 0:
        print("it is a draw")
    elif score == 1:
        print("you win")
    else:
        print("you lose")
    