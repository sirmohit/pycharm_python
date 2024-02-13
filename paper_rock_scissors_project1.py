import random
user_input = int(input("Enter your choice: Type 0 for Rock,1 for Paper and 2 for Scissor."))
if(user_input > 2 or user_input):
    print("you enter a invalid number and you loose")
else:
    computer_choice = random.randint(0,1)
    print("computer_chice: ")
    print(computer_choice)
    if(computer_choice == user_input):
        print("This is draw")
    elif(computer_choice == 0 and user_input == 2):
        print("user loose")
    elif(user_input == 0 and computer_choice == 2):
        print("user wins")
    elif(computer_choice > user_input):
        print("computer wins")
    elif(user_input>computer_choice):
        print("user will win")




