import time as t
import random as r
import sys as s

verify = True
while verify == True:
    print("")
    userWallet = input("Please enter a whole pound value you wish to start with...\n[£]: ")
    try:
        val = int(userWallet)
    except ValueError:
        print("")
        print("Invalid wallet amount")
        print("")
        verify = True
    else:
        print("")
        print("----------------------------------------------------------------")
        print("You wish to start with £", userWallet)
        print("----------------------------------------------------------------")
        verifyWallet = input(
            "If this is correct, please enter 'Y', otherwise enter anything else to adjust your wallet\n[?]: ")
        if verifyWallet == "Y" or verifyWallet == "y":
            if int(userWallet) >= int(100):
                print("")
                check = input("Your wallet is very large, please ensure you bet responsibly. Are you sure you wish to continue?\n[Y/N]: ")
                if check == "Y" or check == "y":
                    verify = False
                    print("")
                    print("----------------------------------------------------------------")
                    print("£", userWallet, "has been added to your wallet")
                    print("----------------------------------------------------------------")
                    startAmount = int(userWallet)
                elif check == "N" or check == "n":
                    verify = True
            else:
                verify = False
                print("")
                print("----------------------------------------------------------------")
                print("£", userWallet, "has been added to your wallet")
                print("----------------------------------------------------------------")
                game = True
t.sleep(2)
#-------Game Module-------
loop = True
while loop == True:
    print("")
    bid1 = int(input("How much would you like to bid?\n[Amount, £]: "))
    if int(bid1) > int(userWallet):
        print("You only have £", userWallet, "in your wallet")
        print("")
        loop = True
    else:
        loop = False
        userWallet = int(userWallet) - bid1
        print("Placing down £", bid1, "...")
        rGen1 = r.randint(1,30)
        #print(rGen1)
        if rGen1 % 2 == 0:          #Checking module
            numberIsEven = True
        else:
            numberIsEven = False
        if rGen1 % 10 == 0:
            numberOf10 = True
        else:
            numberOf10 = False
        if rGen1 < 5:
            numberBelow5 = True
        else:
            numberBelow5 = False
        if rGen1 > 1:

            # Iterate from 2 to n / 2
            for i in range(2, rGen1 // 2):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (rGen1 % i) == 0:
                    isNumberPrime = False
                    break
            else:
                isNumberPrime = True

        else:
            isNumberPrime = False

        if numberIsEven == True:                #Reward module
            userWallet = int(userWallet) * 2
        else:
            pass

        if numberOf10 == True:
            userWallet = int(userWallet) * 3
        else:
            pass

        if numberBelow5 == True:
            userWallet = int(userWallet) * 2
        else:
            pass

        if isNumberPrime == True:
            userWallet = int(userWallet) * 5
        else:
            pass

        print("")
        print("Rolling...")
        t.sleep(2)
        print("----------------------------------------------------------------")
        print("Wallet amount: £",userWallet)
        print("----------------------------------------------------------------")
        t.sleep(2)
        if userWallet == 0:
            print("You've ran out of funds in your wallet! Thanks for playing!")
        else:
            reRun = input("Would you like to roll again?\n[Y/N]: ")
            if reRun == "N" or reRun == "n":
                print("You started with: £",startAmount)
                print("You are cashing out: £",userWallet)
                print("")
                loop = False
                s.exit()
            elif reRun == "Y" or reRun == "y":
                loop = True