print("===Creating Account===")

email = input("Input your email : ")
password = input("Input your Password : ")

print("Account Succesfully create! ^-^*")
while True:
    
    print("===Login===")
    em = input("Input your email : ")
    pas = input("Input your Password : ")

    if em == email and pas == password:
        print("Account Successfully Login")
        break
    else:
        print("Wrong Email or Password!!!")
