# ATM GUI (2nd version)- you can create new user as well!!!

from os import name
import tkinter
from tkinter import *
import csv


window = tkinter.Tk()
window.title("ATM")
window.geometry("500x500")
window.resizable(0,0)

label = tkinter.Label(window, text="Welcome to ATM", font= ("Arial Bold", 40))
label.place(x=30,y=40)

fields = ["Name", "Passcode", "Number", "Amount"]

# reading csv

file = open("data", "r")
csv_reader = csv.reader(file)

lists_from_csv = []
for row in csv_reader:
    lists_from_csv.append(row)


# make change

def withdraws(index):
    num = int(lists_from_csv[index+1][3])
    if num >= int(amount_adjusted.get()):
        num -= int(amount_adjusted.get())
    else:
        raise "Not enough amount Error"
    lists_from_csv[index+1][3] = num
    c.itemconfig(val, text="Your balance: "+str(lists_from_csv[index+1][3]))

def deposits(index):
    num = int(lists_from_csv[index+1][3]) + int(amount_adjusted.get())
    lists_from_csv[index+1][3] = num
    # updating the output
    c.itemconfig(val, text="Your balance: "+str(lists_from_csv[index+1][3]))

def leave():
    c.destroy()
    exit.destroy()
    deposit.destroy()
    withdraw.destroy()
    amount_adjusted.destroy()
    invalid.destroy()

# get input

def getTextInput():
    result = account_input.get()
    result2 = pass_input.get()

    # verifying identity in csv
    index = -1
    for i in range(1,len(lists_from_csv)):
        if result==lists_from_csv[i][2] and result2==lists_from_csv[i][1]:
            index = i-1
            break
    if index==-1:
        global invalid

        invalid = tkinter.Label(window, text="Invalid Entry", font= ("Arial Bold", 15), foreground="red")
        invalid.place(x=180,y=300)
        raise "Invalid Entry error"

    # creating a new canvas to display details
    global c

    c = Canvas(window,bg = "light blue",height = "500", width="500")
    c.pack()
    # displaying information
    c.create_text(230,80,fill="red",font=("Arial", 25),text="Welcome "+lists_from_csv[index+1][0])
    c.create_text(170,150,fill="green",font=("Arial", 20),text="Account number: "+str(lists_from_csv[index+1][2]))
    global val
    val = c.create_text(160,200,fill="green",font=("Arial", 20),text="Your balance: "+str(lists_from_csv[index+1][3]))
    # money input
    c.create_text(260,300,fill="blue",font=("Arial", 15),text="Enter amount:")

    # input of amount
    global amount_adjusted
    amount_adjusted = tkinter.Entry(window, width=17)
    amount_adjusted.place(x=205,y=320)

    # buttons
    global deposit, withdraw, exit
    deposit = tkinter.Button(window,text="Deposit",bg="yellow",height=2,width=20,command=(lambda: deposits(index)))
    deposit.place(x=90, y=360)
    withdraw = tkinter.Button(window,text="Withdraw",bg="violet",height=2,width=20,command=(lambda: withdraws(index)))
    withdraw.place(x=260, y=360)
    exit = tkinter.Button(window,text="Exit",bg="red",height=2,width=20,command=leave)
    exit.place(x=170, y=420)

# submit user
def submit_details():
    record = [name.get(), pin.get(), numbers, depo.get()]
    if "" not in record:
        lists_from_csv.append(record)
        canvas.create_text(240,340,fill="blue",font=("Arial", 20),text="User Created!")
    else:
        raise "Enter Valid Value Error"

    # updating the csv file
    with open("data", "w", newline='') as f:
        write = csv.writer(f)
        write.writerows(lists_from_csv)

# home
def home():
    canvas.destroy()
    name.destroy()
    pin.destroy()
    depo.destroy()
    submit.destroy()
    back.destroy()

# create user

def create_user():
    global canvas
    canvas = Canvas(window,bg = "cyan",height = "500", width="500")
    canvas.pack()
    # taking details commands
    global numbers
    numbers = str(int(lists_from_csv[len(lists_from_csv)-1][2])+1)
    canvas.create_text(130,80,fill="black",font=("Arial", 20),text="Enter Name:")
    canvas.create_text(113,140,fill="black",font=("Arial", 20),text="Enter Pin:")
    canvas.create_text(170,200,fill="black",font=("Arial", 20),text="Account No: "+numbers)
    canvas.create_text(140,260,fill="black",font=("Arial", 20),text="Initial Deposit:")

    # reading the input
    global name, pin, depo
    name=tkinter.Entry(window, width=40)
    name.place(x=210,y=72)
    pin=tkinter.Entry(window, width=40)
    pin.place(x=210,y=130)
    depo=tkinter.Entry(window, width=30)
    depo.place(x=240,y=253)

    # submit
    global submit, back
    submit = tkinter.Button(window,text="Create User",bg="light green",height=2,width=40,command=submit_details)
    submit.place(x=100, y=370)

    # return to home page
    back = tkinter.Button(window,text="Back",bg="yellow",height=2,width=40,command=home)
    back.place(x=100, y=430)

# login
account = tkinter.Label(window, text="Account No.", font= ("Arial Bold", 15))
account.place(x=60,y=200)

password = tkinter.Label(window, text="Password", font= ("Arial Bold", 15))
password.place(x=60,y=250)

enter = tkinter.Button(window,text="Login",bg="light green",height=2,width=40,command=getTextInput)
enter.place(x=100, y=340)

# adding new user
new_user_text = tkinter.Label(window, text="New here?", font= ("Arial Bold", 10))
new_user_text.place(x=210,y=410)
new_user = tkinter.Button(window,text="Create Account",bg="pink",height=2,width=40,command=create_user)
new_user.place(x=100, y=440)

# input
account_input=tkinter.Entry(window, width=20)
account_input.place(x=190,y=210)

pass_input=tkinter.Entry(window, width=5)
pass_input.place(x=190,y=255)


window.mainloop()

# saving to csv file

with open("data", "w", newline='') as f:
    write = csv.writer(f)
    write.writerows(lists_from_csv)
