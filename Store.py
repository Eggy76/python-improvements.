user = input("Hi, What is your name? ")
print("\nWelcome to Eggy store" ,user)

userWant = eval(input("\nWe have a selection of Food here!\n1 - Honey Butter\n2 - Toyo\n3 - Sprite \nYou may now choose: "))

if userWant == 1:
    print("Honey butter? That should be 99 pesos" ,user)
elif userWant == 2:
    print("Toyo? That should be 11 pesos" ,user)
elif userWant == 3:
    print("Sprite? That should be 12 pesos" ,user)
