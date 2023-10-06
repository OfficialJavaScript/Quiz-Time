#!/usr/bin/python3

# Import necessary libraries
import os, platform, random, time

# This function checks to see what operating system the end user is running, and uses that OS's clear function. If they aren't running a support OS they get line spacing instead.
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin" or "Linux":
        os.system('clear')
    elif unsupported_os == True:
        print("""
              
              
              
              
              
              
              
              
              """)
    else:
        print("You have somehow bypassed checks. Restarting Application....")
        start()
        
# Define Start Functions, Print's the name of the application, clearing the screen each time a new character is added.
def start():
    clear_screen()
    WORD = "Sebastian's Quiz"
    built_word = ""
    times_repeated = 0
    while times_repeated != len(WORD) and times_repeated < len(WORD):
        built_word = f'{built_word + WORD[times_repeated]}'
        print(built_word)
        times_repeated += 1
        time.sleep(0.09)
        clear_screen()

def check_architecture():
    operating_system = platform.system()
    if operating_system.lower() == "windows":
        print("You are using {}".format(operating_system))
    elif operating_system.lower() == "darwin":
        print("You are using {}".format(operating_system))
    elif operating_system.lower() == "linux":
        print("You are using {}".format(operating_system))
    else:
        global unsupported_os
        unsupported_os = True
        print("Your Operating System ({}) is Not Supported.".format(operating_system))
        unsupported_os_question = input("Would you like to continue? ")
        if unsupported_os_question.lower() == "yes":
            print("Screen won't be able to clear, We will Instead add extra lines inbetween quizzes.")
            time.sleep(2)
        elif unsupported_os_question.lower() == "no":
            print("Sorry for the inconvenience")
            print("Sorry to See you go ):")
            time.sleep(3)
            closing()
        else:
            print("You didn't answer.")
            print("""
                  
                  
                  """)
            check_architecture()
def closing():
    WORD = "Closing"
    numdots = random.randint(1, 9)
    dots = ""
    for num in range(numdots):
        clear_screen()
        dots = f'{dots + "."}'
        print(f'{WORD + dots}')
        time.sleep(0.25)
    exit()

check_architecture()
start()

# quiz_choice = input("What kind of quiz would you like to do? ")