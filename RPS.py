#!/usr/bin/env python3

#ascii art found at: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
#Author: christian shank-martel
#Date:Mar 23rd 2023
#Program: RPS.py
#
#Last updated: Mar 25th 3032 by christians hank-martel
import random

def welcome():
    #Print Game banner
    print("""
***************************************************
***************************************************
***************************************************
 ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|   
                                  |_|              
 ____       _                        
/ ___|  ___(_)___ ___  ___  _ __ ___ 
\___ \ / __| / __/ __|/ _ \| '__/ __|
 ___) | (__| \__ \__ \ (_) | |  \__ |
|____/ \___|_|___/___/\___/|_|  |___/

***************************************************
***************************************************
***************************************************
""")
    #print game introduction
    print("""

Welcome player to ROCK, PAPER ,SCISSORS. this program will face you againts 
your own computer in the test of ages...roshambo. now to get started, 
you will need to make your choice...

will it be ROCK?
will it be PAPER?
or will it be SCISSORS?

""")

def user_choice_ascii(choice):
    '''
    This function will tuen the usrs choice into ascii art
    '''
    ascii_art = ""#create var to store the art

    if choice == "rock":#if the user chose rock
        #set ascii_art to Rock ascii
        ascii_art = ("""
*****Rock******
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if choice == "paper":#if the user chose paper
        #set ascii art to Paper
        ascii_art=("""
******Paper*******
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if choice == "scissors":#if the user chose scissors
        #set ascii art to Scissors
        ascii_art=("""
******Scissors******
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    return ascii_art#return ascii_art

def comp_choice_ascii(choice):
    '''
    Make ascii art for what the cpu chose
    '''
    ascii_art = ""#create var to store the art

    if choice == "rock":#if the comp chose rock
        #set ascii_art to Rock ascii
        ascii_art = ("""
******rock******
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---
""")
    if choice == "paper":#if the comp chose paper
        #set ascii art to Paper
        ascii_art=("""
******paper******
      _______
 ____(____    '---
(______
(_______
 (_______
   (__________.---

""")
    if choice == "scissors":#if the comp chose scissors
        #set ascii art to Scissors
        ascii_art=("""
******Scissors******
       _______
  ____(____   '---
 (______
(__________
      (____)
       (___)__.---

""")

    return ascii_art#return ascii_art

def valid_choice(choice):

    valid = bool(False)#make valid bool and set false
    options = ["rock", "paper", "scissors"] #list of options for the computer

    if choice in options:
        valid = True
    else:
        valid = False

    return valid

def winner(user_choice, cpu_choie):
    '''
    this function will determin the winner of the match, takes both user and CPU choice as varuiables
    '''
    winner = ''#make string to see if user won
    if user_choice == "scissors": #if teh user chose rock

        if cpu_choie == "paper": #if the CPU chose paper
            winner = "True"#user Won

        if cpu_choie == "scissors":#if the CPU chose scissors
            winner = "Tie"#user Tied

        if cpu_choie == "rock":
            winner = "False"#the user Won

    if user_choice == "paper": #if teh user chose paper

        if cpu_choie == "paper": #if the CPU chose paper
            winner = "Tie"#user Tied

        if cpu_choie == "scissors":#if the CPU chose scissors
            winner = "False"#user Lost

        if cpu_choie =="rock":
            winner = "True"#User Won

    if user_choice == "rock": #if teh user chose rock

        if cpu_choie == "paper": #if the CPU chose paper
            winner = "False"#user lost

        if cpu_choie == "scissors":#if the CPU chose scissors
            winner = "True"#user won

        if cpu_choie == "rock":
            winner = "Tie"#the match was a tie
    
    return winner

def match_results(user, comp):
    win = winner(user, comp) #find the winner

    #get ascii art for both user and comp
    comp_ascii = comp_choice_ascii(comp)
    user_ascii = user_choice_ascii(user)

    if win == "True": #if the user Won
        print(user_ascii, "\n-------vs-------\n" , comp_ascii)
        print("**************************************")
        print("""__   __                     _       _ 
\ \ / /__  _   _  __      _(_)_ __ | |
 \ V / _ \| | | | \ \ /\ / / | '_ \| |
  | | (_) | |_| |  \ V  V /| | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
        """)
        print("**************************************")

    if win == "False":#if the user Lost
        print(user_ascii, "\n-------vs-------\n" , comp_ascii)
        print("**************************************")
        print("""__   __            _                _ 
\ \ / /__  _   _  | | ___  ___  ___| |
 \ V / _ \| | | | | |/ _ \/ __|/ _ \ |
  | | (_) | |_| | | | (_) \__ \  __/_|
  |_|\___/ \__,_| |_|\___/|___/\___(_)
        """)
        print("**************************************")

    if win == "Tie":#if the match was a tie
        print(user_ascii, "\n-------vs-------\n" , comp_ascii)
        print("**************************************")
        print(""" _ _   _               _   _      _ 
(_) |_( )___    __ _  | |_(_) ___| |
| | __|// __|  / _` | | __| |/ _ \ |
| | |_  \__ \ | (_| | | |_| |  __/_|
|_|\__| |___/  \__,_|  \__|_|\___(_)
        """)
        print("**************************************")

if __name__ == "__main__":
    options = ["rock", "paper", "scissors"] #list of options for the computer

    welcome()#print welcome banner + game intro
    choice = input("The choice is yours...what will it be(type rock,paper,scissors): ")#Take users choice
    choice = choice.lower() #set user input to lowercase for easier validation because the list is in lowercase.
    check = valid_choice(choice)#send user input off to be validated,

    if check == True:
        computerOption = random.choice(options) #This will choose a random option from your list for the computer

        match_results(choice, computerOption)

        

    '''
    DEBUGING/TESTING
    '''

