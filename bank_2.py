user = input("Hi, What is your name? ")
print("\nWelcome to Eggy store" ,user)
print('Please choose a number of your choice.')

userWant = eval(input("\nWe have a selection of Food here!\n1 - Honey Butter\n2 - Toyo\n3 - Sprite \nYou may now choose: "))

if userWant == 1:
    print("Honey butter? That should be 99 pesos" ,user)
elif userWant == 2:
    print("Toyo? That should be 11 pesos" ,user)
elif userWant == 3:
    print("Sprite? That should be 12 pesos" ,user)
else:
    print('Your choice is missing Please choose a number again!')

    print*('How to pay?')
    print('Please Pick a number of your choice: ')

bank = input('\n1.Online Payment\n2.Cash\n3.Back\nChoice:')
if bank == 1:
    print('Thank you for choosing Online Payment.')
elif bank == 2:
    print('Thank you for choosing Cash.')

elif bank == 3:
    print('Now lets back to the Main Menu')
