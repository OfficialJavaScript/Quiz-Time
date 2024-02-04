#!/usr/bin/python3

# Define Constants
INVALID_INPUT_MESSAGE = "That is not a valid input."
VALID_CHOICES = ['a', 'b', 'c', 'd']
CORRECT_MESSAGE = "You are correct!"
INCORRECT_MESSAGE = "You are incorrect."

# This function as the name suggests prints the question and the different possibilites, as well as that it checks if the user has entered A, B, C, or D, if they have the continue to the last check where the code checks if they got the answer correct or not. But if they fail the ABCD test, they are greeted with a Invalid Input message (caused by them not Entering A, B, C or D.)
def ask_question(question, possible_answer, correct_answer):
    while True:
        global points
        print(f'\n{question}\n\n{possible_answer[0]}\n{possible_answer[1]}\n{possible_answer[2]}\n{possible_answer[3]}\n')
        answer = input("What is your choice? ").lower().strip()
        if answer not in VALID_CHOICES:
            print(INVALID_INPUT_MESSAGE)
            continue
        
        if answer == correct_answer:
            print(CORRECT_MESSAGE)
            points += 1
            break
        
        else:
            print(INCORRECT_MESSAGE)
            break

# First it asks the user their name, if they don't enter anything and just press enter they get a Invalid Input error and get chucked into a loop until its not empty.
name = input("What's your name? ")
while not name:
    print(INVALID_INPUT_MESSAGE)
    name = input("What's your name? ")

# Here we greet the user,and ask if they would like to play my quiz. 
print(f"Hello and Welcome {name} to Sebastian's Quiz!!")
play = input("Would you like to play my quiz? (y or n) ").lower()
if play == "y":
    print("Awesome, lets get started!")
else:
    print("Sorry to see you go ):") 
    exit()
    
# Here we start a loop that calls the ask_question with the questions, possible answers, and answer included in the calling process.
while True:
    points = 0
    ask_question("What is Google Dork? ", ['A) A feature in Google\'s search engine that allows users to customize their search results based on personal preferences.', 'B) A specialized search query used to find specific information on the internet.', 'C) A term used to describe someone who is highly skilled in using Google for advanced search techniques.', 'D) A malicious software developed by hackers to exploit vulnerabilities in Google\'s search engine.'], "b")
    ask_question("What is the common standard port for HTTP? ", ['A) Port 20', 'B) Port 53', 'C) Port 80', 'D) Port 443'], "c")
    ask_question("What is the core of the Linux operating system called? ", ['A) Kernel', 'B) Shell', 'C) GUI', 'D) Compiler'], "a")
    ask_question("What does bash stand for? ", ['A) Binary Advanced Scripting Host', 'B) Basic Application Shell', 'C) Bash isn\'t an acronym; it\'s just a name', 'D) Bourne Again Shell'], "d")
    ask_question("What are filenames that are preceded with a dot? ", ['A) Hidden files', 'B) System files', 'C) Configuration files', 'D) Temporary files'], "a")
    ask_question("What does the PWD command do? ", ['A) Prints the working directory', 'B) Performs a password reset', 'C) Displays the process ID of the current shell', 'D) Executes a privileged command'], "a")
    # Here we print the users score.
    print(f"Well done {name} you got {points} out of 6!, thats {round(points / 6 * 100, 2)}%!!")
    # Here the user gets asked if they would like to continue, if they say no the code says its goodbyes and exit the program.
    play_again = input("Would you like to play again? (y or n) ")
    if play_again.lower() == "y":
        print("Awesome!")
    else:
        print("Sorry to see you go ):") 
        break