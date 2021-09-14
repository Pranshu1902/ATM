import time
l = ["Name1", "Name2", "Name3"]
Account = [54864, 54868, 54870]
amount = [1548200, 157864400, 1450000]
pin = [1235, 1259, 1467]

def main(index):
    ind = index
    print("Welcome "+str(n)+"("+str(Account[ind])+")"+"\n")
    command = input("Do you want to withdraw/deposit/get details ")
    print("\n")
    if command=="withdraw":
        am = int(input("Enter amount "))
        if am <= amount[ind]:
            amount[ind]-=am
            print("Withdraw successful! Thank you for using us")
    elif command=="deposit":
        ad = int(input("Enter amount "))
        amount[ind]+=ad
        print("Deposit successful! Thank you for using us")
    elif command=="details":
        print("Name: "+str(l[ind]))
        print("Account number: "+str(Account[ind]))
        print("Amount: "+str(amount[ind])+"\n")
        print("Thank you for using us")
    check = input("Do you want to exit? ")
    if check=="no":
        main(ind)

for i in range(9999999):
    print("--------------Welcome to ATM--------------\n")
    n = input("Enter name ")
    p = int(input("Enter security pin "))
    print("\n")
    if n not in l:
        print("Invalid name\n")
    else:
        ind = l.index(n)
        if p!=pin[ind]:
            print("Incorrect pin\n")
        else:
            main(ind)
            print("Exiting...")
            time.sleep(3)
