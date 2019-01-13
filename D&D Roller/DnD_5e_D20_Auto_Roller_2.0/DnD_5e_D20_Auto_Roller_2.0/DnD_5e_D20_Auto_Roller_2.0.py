#To allow us to do random stuff
import random

#For future calculations in more than one function. Proficiency is changed by the user based on their level
proficiency = 3
modifier = 0
answer_proficiency = ""
dice_roll = 0

#To select attribute and to use proficiency_int for future calculations. Only gone through once per action.
def Introduction():
    global modifier
    global answer_proficiency
    #Use index for ability score array. Str, Dex, Con, Int, Wis, Cha. Dictionary by Undermybrella to add clarity for users
    ability_scores = {"str":8, "dex":18, "con":12, "int":10, "wis":14, "cha":14}
    #Introduction
    print("What ability will you be using?")
    #User chooses which ability the action will require
    answer_ability = input("Str, Dex, Con, Int, Wis, or Cha?").lower()
    #Assigns modifier_int with the appropriate ability score.
    if answer_ability in ability_scores:
        modifier = ability_scores[answer_ability]
        modifier = int(modifier / 2)
        modifier -= 5
        #Determine whether to add proficiency_int or not
        print("Are you proficient in this action?")
        answer_proficiency = input("Yes or No?").lower()
    else:
        print("You did not enter a correct response. Do it over!")
        Introduction()

def Random_Roll():
    #Allows variables to be global or whatever
    global dice_roll
    #The D20 that makes or breaks you
    rolling = True
    # while rolling is true
    while rolling:
        # create x, a random number between 0 and 99
        x = random.randint(0, 99)
        # create y, a random number between 0 and 99
        y = random.randint(0, 99)
        # if x is less than 2 and y is between 0 and 10
        if x == 0 and y == 0:
            pass
        elif (x < 2 and y < 10) or (x == 2 and y == 0):
            # And set roll of False
            rolling = False
    dice_roll = (x * 10) + y
    #If required for adv/dis or if another action is taken.
    rolling = True

def Prof_Plus_Bonuses():
    global dice_roll
    global omodifier
    global answer_proficiency
    global proficiency
    #Calculations for including or excluding proficiency_int
    if  answer_proficiency == "yes" or answer_proficiency == "y":
        print("The d20 hits the table! The number reveals itself, giving you the formula " + str(dice_roll) + " + " + str(modifier) + " + " + str(proficiency))
        total_with_prof = dice_roll + modifier + proficiency
        print("Your total is " + str(total_with_prof) + "!")
    elif answer_proficiency == "no" or answer_proficiency == "n":
        print("The d20 hits the table! The number reveals itself, giving you the formula " + str(dice_roll)  + " + " + str(modifier))
        total_without_prof = dice_roll + modifier
        print("Your total is " + str(total_without_prof) + "!")
    else:
        #To catch if the user entered garbage
        print("Try again.")
        print("Are you proficient in this action?")
        answer_proficiency = input("Yes or No?").lower()
        Prof_Plus_Bonuses()
    Crits()

#To check whether the user wants to perform the same action again to indicate advantage or disadvantage
def Doubles():
    print("Do you have advantage/disadvantage on this roll?")
    reroll = input("Yes or No.").lower()
    if reroll == "yes" or reroll == "y":
        #Lets them roll another d20
        Random_Roll()
        Prof_Plus_Bonuses()
        Restart()
    elif reroll == "no" or reroll == "n":
        #Moves to the possibly last step.
        print("Okay...")
        Restart()
    else:
        print("Try again.")
        Doubles()

#To check to see if the user had so much fun playing that they wanted to do another action that required a different ability
def Restart():
    print("Would you like to perform another action?")
    restart = input("Yes or No.").lower()
    if restart == "yes" or restart == "y":
        #Takes them back to the beginning
        Introduction()
    elif restart == "no" or restart == "n":
        #Steers them towards the exit
        print("Okay...")
    else:
        #User enters incorrect response
        print("Try again.")
        Restart()

#To remind the player if they roll a natural 1/20. Spoilers: you can't crit succeed or fail ability and skill checks!
def Crits():
    if dice_roll == 0:
        print("You rolled a natural 1!")
    elif dice_roll == 20:
        print("You rolled a natural 20!")
    else:
        pass
        
#Down the rabbit hole
def Program():    
    print("Welcome to Crispybro's D20 Program! Assistance provided by /u/UndermyBrella")
    Introduction()
    Random_Roll()
    Prof_Plus_Bonuses()
    Doubles()

#Turned into one function so that the entire program can restart if needed.
Program()

#To signify the user that the program will now shut off.
print("There are no gods, only dice. You only have yourself to blame for using my shitty program.")
input('Press ENTER to exit')

"""
Current Issues:
n/a...or at least bug testing hasn't confirmed any syntax errors.

Steps:
1) User selects ability and if to include proficiency. modifier and answer_proficiency variables should have changed
2) Random_Roll function outputs a random roll. dice_roll should have changed.
3) Prof_Plus_Bonuses takes the answer_proficiency to answer if statement and takes dice_roll, modifier, and maybe proficiency to output an answer.
3.1) If they crit on a roll, Crits function will remind them.
4) Doubles function asks if they have advantage/disadvantage. If so, starts over at step 2, otherwise, continues on.
5) Restart function asks if they want to perform a different action. Brings them to step 1 if they say yes.
6) Done
"""
