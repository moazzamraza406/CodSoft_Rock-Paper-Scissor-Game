import random as rn

rock = '''
    _______
---'    ___)
       (____)
       (____)
----___(__)
'''

paper = ''' 
    _______
---'    ___)____
             ____)
              ____)
             ____)
----____________)
'''

scissors = ''' 
    _______
---'    ___)____
             ____)
      ____________)
       (____)
----___(__)
'''

game_images = [rock, paper, scissors]

running = True
while running :

    user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
    if user_choice >= 3 or user_choice < 0 :
        print("You entered invalid number, You lose.")

    else :
        print(game_images[user_choice])
        computer_choice = rn.randint(0,2)
        print("Computer Chose:")
        print(game_images[computer_choice])
        if computer_choice == user_choice :
            print("Its a Draw")
            if not input('Playing_again? (y/n)').lower() == 'y':
                running = False

        elif computer_choice == 0 and user_choice == 2 :
            print("You lose")
            if not input('Playing_again? (y/n)').lower() == 'y':
                running = False

        elif user_choice == 0 and computer_choice == 2 :
            print("You win")
            if not input('Playing_again? (y/n)').lower() == 'y':
                running = False

        elif computer_choice > user_choice :
            print("You lose")
            if not input('Playing_again? (y/n)').lower() == 'y':
                running = False

        elif user_choice > computer_choice :
            print("You win")
            if not input('Playing_again? (y/n)').lower() =='y':
                running = False

print('Thanks for playing')