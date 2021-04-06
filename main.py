
#  Improvements
# - Account opening amount 
# - Balance Enquiry
# - Deposit functionality
# - withdrawal functionality



import random

database = {}  # dictionary


def init():

    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):

        login()
    elif(haveAccount == 2):

        register()
    else:
        print("You have selected invalid option")
        init()


def login():

    print("********* Login ***********")

    isLoginSuccessful = False

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                isLoginSuccessful = True
                bankOperation(userDetails)

    if(isLoginSuccessful == False):
        print('Invalid account or password')
        login()


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    opening_balance = int(
        input("How much do you want to open your account with? \n"))

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name,
                               last_name, email, password, opening_balance]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bankOperation(user):

    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input(
        "What would you like to do? (1) A/C Balance (2) deposit (3) withdrawal (4) Logout (5) Exit \n"))

    if(selectedOption == 1):
        showBalance(user)

    elif(selectedOption == 2):
        depositOperation(user)

    elif(selectedOption == 3):
        withdrawalOperation(user)

    elif(selectedOption == 4):
        logout()

    elif(selectedOption == 5):
        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)


def showBalance(user):
    print("Your A/C balance is %d " % (user[4]))


def withdrawalOperation(user):
    withdrawalAmount = int(input('How much would you like to withdraw? \n'))
    if ((user[4]) > withdrawalAmount):
        newBalance = ((user[4]) - withdrawalAmount)
        user[4] = newBalance
        print("Your new balance is: %d" % newBalance)
        print("Please take your cash")
        print("Thank you for banking with us")
    else:
        print("insufficient funds")


def depositOperation(user):
    depositAmount = int(input('How much would you like to deposit? \n'))
    currentBalance = (depositAmount + (user[4]))
    user[4] = currentBalance
    print("Your new balance is: %d" % currentBalance)
    print("Thank you for banking with us")


def generationAccountNumber():

    return random.randrange(1111111111, 9999999999)


def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

init()
