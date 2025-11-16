

def activity1():
    a = "pogi"
    print("a means pogi")

def activity2():
    name = input("What is your name .? ")
    print("Hi", name , "Welcome to the Matrix")

def activity3():
    print("\"Ang order ko ay bulalo bat niyoko bibigyan ng noodles\"")

def activity4():
    name = input("Input your name : ")
    print("Your name has ",len(name), "characters")

def activity5():    
    anything =eval(input("Input something : "))
    
    print("The data type of something is",type(anything))
    
    answer = 6 + anything
    
    print("the answer is ", answer)

def activity6():    
    n1 = eval(input("Enter the first number: "))
    n2 = eval(input("Enter the second number: "))

    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    #solution = ((n1/n2) * 1005) // 300
    print("\nThe sum of", n1, "and", n2, "is", s)
    print("The difference of", n1, "and", n2, "is", d)
    print("The product of", n1, "and", n2, "is", p)
    print("The quotient of", n1, "and", n2, "is", q)
    print(n1, "exponent by", n2, "is", n1**n2)
    print("The remainder of", n1, "and", n2, "is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1//n2)

def activity7():
    a = 100

    print("The value of a is", a)

    a += 12
    a /= 12
    a -= 42
    a *= 2
    print("The value of a is", a)

def activity8():
    balance = '1000'
    withdrawal = '500'

    withdraw = eval(input("Enter the amount: "))
    print(withdrawal <= balance)
    print("amount = balance", balance)

def activity9():
    username = 'christian'
    password = 'pogiako405'

    print(username == 'christian')  # True
    print(password == 'pogiako405')  # True
    print((username == 'christian') or (password == 'pogiako405'))  # True
    print((username == 'christian') and (password == 'pogiako405'))
    print(not((username == 'christian') and (password == 'pogiako405')))

def activity10():

#name
#student or not
#fare or bayad
#discount

    passenger = input("Input your name: ")
    passenger1 = input("Are you a student (yes / no): ")
    fare = eval(input("Pay: "))

    if passenger1.lower() == "yes" :
        discount = fare * .16
        new_fare = fare - 2.0
        print("Congrats discount has been approved your newfare is",new_fare,  "Enjoy your ride with us")
    else:
        print("Sorry your request on the discount has not been approved")

def activity11():

    temp = eval(input("Enter the Temperature: "))

    if temp <= 0:
        print("Temperature outside is freezing cold")
    elif temp >= 1 and temp <= 20:
        print("Temperature outside cold")
    elif temp >= 21 and temp <30:
        print("Temperature outside lukewarm")
    elif temp >= 31 and temp <= 40:
        print("Temperature outside warm")
    elif temp >= 41 and temp <= 50:
        print("Temperature outside above boiling hot")
    elif temp >= 51:
        print("Temperature outside above boiling hot")
    else:
        print("invalid temperature")	

