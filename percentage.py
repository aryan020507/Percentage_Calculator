print("What you want to find kindly pick one")
print("1. Percentage.\n2.Obatined Value.\n3. Total Value.\n4. Check percenatge Increase or Decrease or its Original Value.\nKindly Enter any one number you want between 1, 2, 3 and 4 to find.")

try:
    input1=int(input())
    
except ValueError:
    print("Incorrect! Please enter a Number.")
    exit()
if(input1==1):
    try:
        obtained=float(input("Enter Obtained value: "))
        total=float(input("Enter Total Value: "))
        if total == 0:
            print("Cannot Execute.")
        else:
            percentage=(obtained*100)/total
            print(percentage)
    except ValueError:
        print("Incorrect! Please enter a Number.")
elif(input1==2):
    try:
        total=float(input("Enter Total Value: "))
        percentage=float(input("Enter Percentage'%'(from 1-100% only): "))
        if(percentage<=0):
            print("Cannot Execute.")
        else:
            obtained=(percentage*total)/100
            print(obtained)
    except ValueError:
        print("Incorrect! Please enter a Number.")
elif(input1==3):
    try:
        percentage=float(input("Enter Percentage'%'(from 1-100% only): "))
        obtained=float(input("Enter Obtained value: "))
    except ValueError:
        print("Incorrect! Please enter a Number.")
        exit()
    if(percentage<=0):
        print("Cannot Execute.")
    else:
        total=(100*obtained)/percentage
        print(total)
elif(input1==4):
    try:
        print("\n.what you want to know?\n1. Increased.\n2. Decreased.\n3. Original Value.\n(Choose any one of them.)")
        input2=int(input())
        if(input2==1):
            n_val=float(input("Enter New Value: "))
            o_val=float(input("Enter Old Value: "))
            if(o_val==0):
                print("Cannot Execute.")
            else:
                increase=((n_val-o_val)/o_val)*100
                print(increase)
        elif(input2==2):
            n_val=float(input("Enter New Value: "))
            o_val=float(input("Enter Old Value: "))
            if(o_val==0):
                print("Cannot Execute.")
            else:
                decrease=((o_val-n_val)/o_val)*100
                print(decrease)
        elif(input2==3):
            print("\n1. Increase Value to Original Value.\n2. Decrease Value to Original.\n Choose any one of them.")
            input3=int(input())
            if(input3==1):
                current=float(input("Enter Current Value: "))
                x=float(input("How much percent increased: "))
                original=current/((100+x)/100)
                print(original)
            elif(input3==2):
                current=float(input("Enter Current Value: "))
                x=float(input("How much percent decreased: "))
                original=current/((100-x)/100)
                print(original)
            else:
                print("Invalid Input.")
        else:
            print("Invalid Input.")
    except ValueError:
        print("Incorrect! Please enter a Number.")
else:
    print("Invalid Input.")

print("\nReuse it if required 😊\n")
