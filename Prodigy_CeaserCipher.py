import os

def menu(option):
    key = 0
    option = option.upper()

    if option == "E" or option == "D":
        menu_option(option, key)
        
    else:
        option = input("Please select the correct option :")
        menu(option)

def menu_option(option, key):

    msg = ""

    if option == "E":
        e_msg = input("Input the message you would like to ENCRYPT :\n")
        key = int(input("Input the key, it should be a number between 1-25 :\n"))

        if key < 1 or key > 25:
            while key < 1 or key > 25:
                key = int(input("Input a valid key (1-25): \n"))
        
        os.system('cls')

        c_encrypt(e_msg, key, msg)


    if option == "D":
        d_msg = input("Input the message you would like to DECRYPT :\n")
        key = int(input("Input the key, it should be a number between 1-25 :\n"))

        if key < 1 or key > 25:
            while key < 1 or key > 25:
                key = int(input("Input a valid key (1-25): \n"))

        os.system('cls')

        d_encrypt(d_msg, key, msg)


def c_encrypt(e_msg, key, msg):

    for i in range(len(e_msg)):

        if e_msg[i].isupper():
            msg += chr((ord(e_msg[i]) + key - 65) % 26 + 65)

        elif e_msg[i].islower():  
            msg += chr((ord(e_msg[i]) + key - 97) % 26 + 97)

        else:
            msg += e_msg[i]

    print("Your Orignal Message Was :\n",e_msg,"\n\nYour Encrpyted Message Is :\n",msg,"\n\nAnd The Key You Used Is :\n",str(key),"\n")

    retry = input("If You Would Like To Encrypt Or Decrypt Another Message Type YES \n")

    retry = retry.upper()

    if retry == "YES":

        os.system('cls')

        print('Enter one of the Following: \nE : To encrpyt your message\nD : To decrypt yor message')
        option = input('Enter Here : ')

        os.system('cls')

        menu(option)
    
    else:
        print("Thank You For Using This Program")




def d_encrypt(d_msg, key, msg):

    for i in range(len(d_msg)):

        if d_msg[i].isupper():
            msg += chr((ord(d_msg[i]) - key - 65) % 26 + 65)

        elif d_msg[i].islower():  
            msg += chr((ord(d_msg[i]) - key - 97) % 26 + 97)

        else:
            msg += d_msg[i]
    
        print("Your Orignal Message Was :\n",d_msg,"\n\nYour Decrpyted Message Is :\n",msg,"\n\nAnd The Key You Used Is :\n",str(key),"\n")

    retry = input("If You Would Like To Encrypt Or Decrypt Another Message Type YES \n")

    retry = retry.upper()

    if retry == "YES":

        os.system('cls')

        print('Enter one of the Following: \nE : To encrpyt your message\nD : To decrypt yor message')
        option = input('Enter Here : ')

        os.system('cls')

        menu(option)
    
    else:
        print("Thank You For Using This Program")

    


print('Enter one of the Following: \nE : To encrpyt your message\nD : To decrypt yor message')
option = input('Enter Here : ')

os.system('cls')

menu(option)