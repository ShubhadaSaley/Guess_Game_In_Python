import random
import sys
import time

'''-----------------------------------------------------'''
def exit_game():
    print("Thank You!!")
    sys.exit()
'''------------------------------------------------------'''
name=input("Hi what is your name?")
while name=='':
    name=input("Please enter your name: ")
time.sleep(0.5)
if name=='exit':
    exit_game()
print("Welcome {} Let's play game" .format(name))
###########################################################

def instructions():
    print("Instructions of Game")
    time.sleep(1)
    print("This is Guess_word_Game!!! A fun game!!!")
    time.sleep(1.5)

    print("1.. At the start time you will be given number of letters in a word and the category of word which belong to.")
    time.sleep(3)
    print("2.. You have to guess a letter one by one and your letter inserted to the word.")
    time.sleep(3)
    print("3.. Wrong letter will decrease the guess counter.")
    time.sleep(3)
    print("4.. Once guess counter become zero you loose the game.")
    time.sleep(3)
    print("5.. Try to find word at maximum guess counter.")
    time.sleep(3)
    print("6.. Type 'exit'(and press enter) anytime to exit playing.")
    time.sleep(3)
    print("7.. Do not enter more than one letter, if you entered more than one letter only first letter is consider.")
    time.sleep(3)

    while True:
        start1=input("Are you ready to play?\nPress enter to Continue....")
        if start1=='exit':
            exit_game()
        elif start1 not in '':
            print("Invalid Input!!")
            continue
        if start1 in '':
            break
time.sleep(1)
instructions()
##########################################################################

print("Great Let's start the game")
time.sleep(1)
print("------------------------------------------------------------------")
print()
print("Code by Shubhada Saley")
time.sleep(2)

#Main code starts here
ascii_letters='abcdefghijklmnopqrstuvwxyz'
#list of words in Game
fruits = ['apple', 'olive', 'tomato', 'melon', 'litchi',
          'mango', 'lime', 'kiwi', 'grapes', 'cherry',
          'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
          'orange', 'papaya', 'pear', 'peach', 'berry']

animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
           'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
           'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
           'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
           'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
           'squirrel', 'tiger', 'vulture']

accessories =['ring', 'bangle', 'lipstick', 'handbag', 'crown',
               'necklace', 'watch', 'caps', 'glasses', 'wallet',
               'belts', 'comb', 'pendent', 'earring', 'scarf',
               'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
               'jacket', 'boots', 'socks', 'stocking', 'muffler',
               'gloves', 'umbrella', 'ribbon']

stationary =['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
              'files', 'fevicol', 'inkpot', 'chalk', 'duster',
              'glue', 'paper', 'cutter', 'chart', 'colours',
              'stapler', 'marker', 'staples', 'clips', 'calculator',
              'envelope', 'register']

list = fruits + animals + accessories + stationary
############################################################
while True:
    word=random.choice(list) #random function choose any random word from list
    print("Your word has",len(word), "letters")
    print()
    #showing category of word to player
    if word in fruits:
        print("Your word is name of a fruit")
    elif word in animals:
        print("Your word is name of a animal")
    elif word in accessories:
        print("Your word is name of a accessory")
    elif word in stationary:
        print("Your word is name of a stationary")

    time.sleep(1.5)
    turns=11 - len(word) #No.of free chances of guess
    if len(word)>=8:
        turns=4
    print("You have left {} free chances to guess the word".format(turns))
    time.sleep(1.5)

    while True:
        start=input("Press enter to start guessing...") #only press enter
        if start == 'exit':
            exit_game()
        elif start not in '':
            print("Invalid Input")
            continue
        else:
            break
    guesses=''
    while turns>0:
        failed=0
        guess=input("Guess a character: ").lower()
        if guess=='exit':
            exit_game()
        if guess in '':
            print("Please enter a valid character")
            continue
        else:
            guess = guess

        if guess in guesses:
            print("You have already entered this character")
            continue

        guesses += guess

        for char in word:
            if char in guesses:
                print(char, " ", end="")
            else:
                print("_ ", end="")
                failed+=1

        if failed==0:
            print("\nCongratulations! You won!!\n")
            time.sleep(1.5)
            print("\nThe word is {}".format(word))
            time.sleep(1.5)
            break

        if guess in word:
            print("\nExcellent! {} is in the word".format(guess))
        if guess not in word:
            if guess not in ascii_letters:
                print("\nPlease enter valid character")
            else:
                print("\nWrong! It seems that {} not in word".format(guess))

                turns-=1
            if turns!=0:
                print("\nYou have" ,turns, "more guesses left")
            elif turns==0:
                print("\nGrr!!You have no more guesses")
                time.sleep(1)
                print("\nSorry!! You loose")
                time.sleep(1)
                print("\nThe word was {}".format(word))
                time.sleep(1.5)
                print("\nNo problem better luck next time")
    time.sleep(1.8)
#######################################################################
    while True:
        play_again=input("\nDo you want to play again?? \nType y or n: ")
        if play_again in ('y','yes','n','no'):
            break
            print("Invalid input")
    if play_again in ('y','yes'):
        print("Ok")
        time.sleep(1)
        continue
    elif play_again in ('n','no'):
        print("Thank You for playing! Good Bye!!")
        time.sleep(1)
        break
