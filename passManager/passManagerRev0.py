import os
import useful
from pathlib import Path
from EncryptDecrypt import CryptoGraphy
from Generator import Generator
from Password import Password
from getpass import getpass


# https://stackoverflow.com/questions/5214578/print-string-to-text-file
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
useful.Terminal.clear()

actions = {
    "add" : "PasswordManager.addPass()",
    "edit" : "PasswordManager.edit()",
    "remove" : "PasswordManager.remove()",
    "list" : "PasswordManager.listPass()",
    "save" : "PasswordManager.save()",
    "close" : "PasswordManager.close()",
    "delete profile" : "PasswordManager.delete()"
} 
rBrkt = "{"
lBrkt = "}"

pathToDir = Path(__file__).parent.absolute().__str__() + "\\$70ra93"
passFilePath = Path(f"{pathToDir}\\passwordFile.store")
pathToLoginFile = Path(f"{pathToDir}\\login.encrypted")
class PasswordManager:
    mstrPWStor = {}
    storeContents = ""
    def login():

        # if pathToFile.is_file(): os.remove(pathToFile)

        # if the login file doesn't exist, have the user create an account
        if not pathToLoginFile.is_file():
            firstName = input("What is your first name? ")
            lastName = input("What is your last name? ")
            loginUser = input('What do you want your username to be? ')
            loginPass = Password( getpass('What do you want as your password? ') )
            # os.removedirs(Path( pathToDir ))

            # loops until the user puts in a max strength password, a strength of 5
            while True:
                if loginPass.check(5):
                    namePass = f"{rBrkt}'First name' : '{firstName}', 'Last name' : '{lastName}', 'UserName' : '{loginUser}', 'Password' : '{loginPass.txt}'{lBrkt}"
                    
                    # generate a key based on the namePass string, then encrypt namePass with that key, that key is also the global encryption key
                    CryptoGraphy.genKey(namePass, pathToDir)
                    CryptoGraphy.encrypt(namePass, f"{pathToDir}", f"{pathToLoginFile}")
                    break
                # set the txt value of loginPass to the ui
                loginPass.set( getpass('That password is not very secure, try a different one: ') )

        # if the login file exists
        if pathToLoginFile.is_file():
            namePass = CryptoGraphy.decrypt(pathToLoginFile, pathToDir)
            # namePass is decrypted into a string, so eval it to turn it into the dictionary it is
            namePass = eval(namePass)
            username = namePass["UserName"]
            password = namePass["Password"]
            
            fails = 0
            while True:
                useful.Terminal.clear()
                print(f"Attempts: {fails}")
                if fails == 3:
                    useful.Terminal.clear()
                    print("You have reached the maximum number of attempts.")
                    quit()

                fails += 1
                if useful.Terminal.inputChecker(input("What's your username? "), username) and useful.Terminal.inputChecker(getpass("What's your password? "), password):
                    break
                    
            PasswordManager.openApp()
                

    def openApp():
        while True:    
            if passFilePath.is_file():
                file = open(f"{passFilePath}", 'r')
                PasswordManager.storeContents = file.read()
                file.close()
                if PasswordManager.storeContents != "":
                    PasswordManager.storeContents = CryptoGraphy.decrypt(passFilePath, pathToDir)
                break
            else:
                open(f"{passFilePath}", 'wb').close()
        useful.Terminal.clear()
        # set the global dict of all passwords to the dict from the decrypted file
        if PasswordManager.storeContents == "":
            PasswordManager.mstrPWStor = {}
        else:
            PasswordManager.mstrPWStor = eval(PasswordManager.storeContents)
    
        
        while True:
            
            userChoice = input(f"What do you want to do; {useful.Strings.lstToStr(actions, ', ', False)}? ")
            if userChoice in actions:
                eval(actions[userChoice])
            PasswordManager.save()
            
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def addPass():
        # ask the user what catagory the password is in, and where the password is used
        if PasswordManager.mstrPWStor.keys().__str__() == "dict_keys([])":
            catagory = input("What do you want to call your first catagory? ")
            passFor = input("Where is this password going to be used? ")
        else:
            while True:
                catagory = input(f"What category is this password; {useful.Strings.lstToStr(PasswordManager.mstrPWStor, ', ', False)}, or enter a new name to create a new catagory? ")
                passFor = input("Where is this password going to be used? ")
                break

        # ask the user what the password is, or generate one for them
        ui = getpass("Type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong: ")
        while True:
            useful.Terminal.clear()
            if ui.isdigit():
                if 3 <= int(ui) + 2 <= 5:
                    if not catagory in PasswordManager.mstrPWStor:
                        PasswordManager.mstrPWStor[catagory] = {}
                    randPass = Password( Generator.genPass(int(ui) + 2) )
                    PasswordManager.mstrPWStor[catagory][passFor] = randPass.getPass()
                    break
            else:
                passTemp = Password(ui)
                if passTemp.check():
                    if not catagory in PasswordManager.mstrPWStor:
                        PasswordManager.mstrPWStor[catagory] = {}
                    PasswordManager.mstrPWStor[catagory][passFor] = passTemp.getPass()
                    break
            ui = getpass("That password was insecure, type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong: ")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        

    def edit():
        # ask the user what catagory the password is in
        PasswordManager.listPass()
        cat = input(f"What category is the password in ")
        while not cat in PasswordManager.mstrPWStor:
            useful.Terminal.clear()
            PasswordManager.listPass()
            cat = input("That's not a category, try again ")
        
        # ask the user where the password gets used
        useful.Terminal.clear()
        PasswordManager.listPass()
        place = input("What is the password to ")
        while not place in PasswordManager.mstrPWStor[cat]:
            useful.Terminal.clear()
            PasswordManager.listPass()
            place = input("That place isn't in the records, try again ")
        
        # ask the user what they want the new password to be, or generate one for them
        ui = getpass("Type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong: ")
        while True:
            useful.Terminal.clear()
            if ui.isdigit():
                if 3 <= int(ui) + 2 <= 5:
                    if not cat in PasswordManager.mstrPWStor:
                        PasswordManager.mstrPWStor[cat] = {}
                    randPass = Password( Generator.genPass(int(ui) + 2) )
                    PasswordManager.mstrPWStor[cat][place] = randPass.getPass()
                    break
            else:
                passTemp = Password(ui)
                if passTemp.check():
                    if not cat in PasswordManager.mstrPWStor:
                        PasswordManager.mstrPWStor[cat] = {}
                    PasswordManager.mstrPWStor[cat][place] = passTemp.getPass()
                    break
            ui = getpass("That password was insecure, type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong: ")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove():
         # ask the user what catagory the password is in
        PasswordManager.listPass()
        cat = input(f"What category is the password in ")
        while not cat in PasswordManager.mstrPWStor:
            useful.Terminal.clear()
            PasswordManager.listPass()
            cat = input("That's not a category, try again ")
        
        # ask the user where the password gets used
        useful.Terminal.clear()
        PasswordManager.listPass()
        place = input("What is the password to ")
        while not place in PasswordManager.mstrPWStor[cat]:
            useful.Terminal.clear()
            PasswordManager.listPass()
            place = input("That place isn't in the records, try again ")
        PasswordManager.mstrPWStor[cat].pop(place)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # formats as a string all the passwords from the global dict, so the can be printed
    def listPass():
        result = ""
        for i in PasswordManager.mstrPWStor:
            result += f'\n{i}'
            for j in PasswordManager.mstrPWStor[i]:
                result += f'\n    {j} : {PasswordManager.mstrPWStor[i][j]}'
        useful.Terminal.clear()
        print(result)


    def delete():
        if input(f"Are you sure you want to delete your profile, {useful.Terminal.Color.RED}WARING: THIS WILL PERMANANTLY DELETE ALL SAVED PASSWORDS, THERE IS NO GOING BACK!!!!!!!!{useful.Terminal.Color.END}, type yes to confirm ") == "yes":
            os.remove(pathToLoginFile)
            os.remove(passFilePath)
            os.remove(Path(f"{pathToDir}\\key.key"))
            quit()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def close():
        PasswordManager.save()
        quit()

    def save():
        CryptoGraphy.encrypt(f"{PasswordManager.mstrPWStor}", pathToDir, passFilePath)

PasswordManager.login()


