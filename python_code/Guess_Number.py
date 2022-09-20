import random


user_input= int(input("Please enter your number : "))
n=random.randrange(1,5)
while n != user_input:
    print("please type correct number")
    if user_input < n:
        print("You have entred low number")
        user_input=int(input("please enter the number : "))
    elif user_input >n :
        print("You have entred too high ")
        user_input=int(input("please enter the number : "))
    else:
        break
print("you have typed correct")        
