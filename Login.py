from tkinter import *

window = Tk()

label = Label(window, text= "Username:",bg= "black",fg= "#00FF00")
label.pack()

entry = Entry(window, bg="White")
entry.pack()

label1 = Label(window, text= "Password:",bg= "black",fg= "#00FF00")
label1.pack()

entry1 = Entry(window, bg="White")
entry1.pack()

check_button = Checkbutton(window,text="Remember me!")
check_button.pack()

login = Button(window,text="Login")
login.pack()

reg = Button(window,text="Register")
reg.pack()
window.Username:()
