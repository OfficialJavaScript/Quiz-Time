#!/usr/bin/python3

# Import necessary libraries
import os, platform, random, time, codecs

# This function checks to see what operating system the end user is running, and uses that OS's clear function. If they aren't running a support OS they get line spacing instead.
def create_variables():
    global unsupported_os
    global MENU_CHOICES
    global QUIZ_CHOICES
    global last_page
    global no_data
    global users
    global new_user
    global quiz_name
    global quiz_topic
    global user_to_use
    unsupported_os = False 
    last_page = ""
    no_data = True
    users = []
    new_user = ""
    quiz_name = ""
    quiz_topic = "a"
    user_to_use = ""
    MENU_CHOICES = """1. Start
2. Leaderboard
3. Settings
4. Exit
"""
    QUIZ_CHOICES = """1. Multi-Choice
2. True or False
3. Odd One Out
4. Random
"""

def check_architecture():
    operating_system = platform.system()
    if operating_system.lower() == "windows":
        clear_screen()
        print("You are using {}".format(operating_system))
        time.sleep(1)
    elif operating_system.lower() == "darwin":
        clear_screen()
        print("You are using {}".format(operating_system))
        time.sleep(1)
    elif operating_system.lower() == "linux":
        clear_screen()
        print("You are using {}".format(operating_system))
        time.sleep(1)
    else:
        clear_screen()
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
            print("You didn't answer.\n\n\n\n")
            check_architecture()
    
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')
    elif unsupported_os == True:
        print("""
                
                
                
                
                
                
                
                
            """)
    else:
        print("You have somehow bypassed checks. Restarting Application....")
        time.sleep(1)
        start()

# Define Start Functions, Print's the name of the application, clearing the screen each time a new character is added.
def start():
    built_word = "" 
    times_repeated = 0
    clear_screen()
    WORD = "Sebastian's Quiz"
    while times_repeated != len(WORD) and times_repeated < len(WORD):
        built_word = f'{built_word + WORD[times_repeated]}'
        print(built_word)
        times_repeated += 1
        time.sleep(0.09)
        clear_screen()
    clear_screen()
    print("Welcome to Sebastian's Quiz!")
    time.sleep(1)
    menu()
            
def closing():
    clear_screen()
    print("Exiting the application will cause all data to be reset\n")
    exit_warning = input("Are you sure you would like to exit? ")
    if exit_warning.lower() == "yes":
        WORD = "Closing"
        numdots = random.randint(1, 9)
        dots = ""
        for num in range(numdots):
            clear_screen()
            dots = f'{dots + "."}'
            print(f'{WORD + dots}')
            time.sleep(0.25)
        clear_screen()
        exit()
    elif exit_warning.lower() == "no":
        if last_page == "menu":
            menu()
        else:
            print("Unfortunately we couldn't return you to your last page ):\n\nWe are returning you to the menu now.")
            time.sleep(1.5)
            menu()
    else:
        print("We could not peform that task, returning back to exit menu. Please enter Yes or No.")
        time.sleep(3)
        closing()
        
def add_user(new_user, quiz_name):
    clear_screen()
    users.append(new_user)
    print("New User added Successfully\n\nWe are sending you back to the Quiz Choice Menu.")
    time.sleep(1)
    quiz_starting(quiz_name)

def multi_choice():
    if quiz_name != "Multi_Choice":
        print("How did you make it here, this is the multi_choice quiz, going back to the quiz choice screen.")
        choose_quiz_type()
    

def play_quiz(quiz_name, user_to_use):
    clear_screen()
    if user_to_use == "":
        print("A user has not been chosen, we will restart the quiz starting process.\n\nSorry for the inconvenience.")
        time.sleep(1.5)
        quiz_starting(quiz_name)
    elif quiz_name == "Multi-Choice":
        print(quiz_name)
        
    elif quiz_name == "True or False":
        print()
    elif quiz_name == "Odd One Out":
        print()
    elif quiz_name == "Random":
        print()
    elif quiz_name != "":
        print("There has been an error in the quiz choosing process, we are restarting to the main page to help fix this problem.")
        time.sleep(1)
        menu()
    else:
        print("You have not chosen a quiz.")
        time.sleep(1)
        choose_quiz_type()

def quiz_starting(quiz_name):
    clear_screen()
    if users == []:
        print("We have detected that there are no users.\n")
        new_user = input("What is your name? ")
        add_user(new_user, quiz_name)
    elif quiz_name == "" or quiz_topic == "":
        problem = ""
        if quiz_name == "" and quiz_topic == "":
            problem ="Quiz Type or Topic"
            print("You have not chosen a {}".format(problem))
        elif quiz_name == "":
            problem = "Quiz Type"
            print("You have not chosen a {}".format(problem))
        elif quiz_topic:
            problem = "Quiz Topic"
            print("You have not chosen a {}".format(problem))
    else:
        if len(users) > 1:
            user_to_use = input("Please choose a user to choose {}: ".format(users))
            print("Welcome {} to Sebastian's Quiz!\n".format(user_to_use))
            print("Lets get started, you have chosen {} as the topic and {} as the type.".format(quiz_topic, quiz_name))
            time.sleep(1)
            clear_screen()
            play_quiz(quiz_name, user_to_use)
        else:
            user_to_use = users[0]
            print("Welcome {} to Sebastian's Quiz!\n".format(users[0]))
            print("Lets get started, you have chosen {} as the topic and {} as the type.".format(quiz_topic, quiz_name))
            time.sleep(1)
            clear_screen()
            play_quiz(quiz_name, user_to_use)

def choose_quiz_type():
    clear_screen()
    print(QUIZ_CHOICES)
    try:
        quiz_choice = int(input("What kind of quiz would you like to do? "))
        if quiz_choice == 1:
            quiz_name = "Multi-Choice"
            quiz_starting(quiz_name)
        elif quiz_choice == 2:
            quiz_name = "True or False"
            quiz_starting(quiz_name)
        elif quiz_choice == 3:
            quiz_name = "Odd One Out"
            quiz_starting(quiz_name)
        elif quiz_choice == 4:
            quiz_name = "Random"
            quiz_starting(quiz_name)
        else:
            quiz_name = "True or False"
            quiz_starting(quiz_name)
    except ValueError:
        print("That is not a valid Input.")
        time.sleep(1)
        choose_quiz_type()
        
def leaderboard():
    clear_screen()
    if no_data == True:
        print("There is Currently no data recorded, go and play a quiz!")
        time.sleep(1)
        menu()
    else:
        print("THIS NEEDS TO BE FINISHED")
        time.sleep(1)
        menu()
        
def settings():
    settings = ""
    print(settings)
    time.sleep(10)
    menu()
    
def menu():
    global last_page
    clear_screen()
    print(MENU_CHOICES)
    last_page = "menu"
    try:
        menu_choice = int(input("What would you like to do? "))
        if menu_choice == 1:
            choose_quiz_type()
        elif menu_choice == 2:
            leaderboard()
        elif menu_choice == 3:
            settings()
        elif menu_choice == 4:
            closing()
        else:    
            print("Thats not a choice.")
            time.sleep(1)
            menu()
    except ValueError:
        print("That is not a valid Input.")
        time.sleep(1)
        menu()
        
create_variables()
check_architecture()
start()
