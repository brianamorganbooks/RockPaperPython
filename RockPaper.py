# Rock Paper Python V1.0
# Written by Gabe Conway 4/23/2020
# Standard rock paper scissors game with two AI modes, best out of three rounds. Random mode will choose a random selection.
# Smart mode will base its choice on statistics. The strategy is based on experiments of Zhejiang University.

import random

#Variable declaration
roundNumber = 1
userScore = 0
CPUScore = 0

#functions
def coreLogic(CPU,User):
     if User == 'rock' :
        if CPU == 'rock' :
            return 'tie'
        if CPU == 'paper' :
            return 'lose'
        if CPU == 'scissors' :
            return 'win'
     if User == 'paper' :
        if CPU == 'rock' :
            return 'win'
        if CPU == 'paper' :
            return 'tie'
        if CPU == 'scissors' :
            return 'lose'
     if User == 'scissors' :
        if CPU == 'rock' :
            return 'lose'
        if CPU == 'paper' :
            return 'win'
        if CPU == 'scissors' :
            return 'tie'

def gameLogic(Difficulty,Choice):
    global roundNumber
    global userLastChoice
    #Smart mode will be random on first round. Stats will be used on round 2 & 3
    if roundNumber == 1 :
        Difficulty = 'random'
    if Difficulty == 'random':
        #Generate a random selection and return
        roundNumber +=1
        userLastChoice = Choice
        options = ['rock' , 'paper' , 'scissors']
        CPUChoice = random.choice(options)
        print("CPU chose " + CPUChoice)
        return coreLogic(CPUChoice,Choice)
    if Difficulty == 'smart':
        #round is the 2nd or 3rd, using stats on last play to win. 
        roundNumber +=1
        if userLastChoice == 'rock' :
            CPUChoice = 'scissors'
        if userLastChoice == 'paper' :
            CPUChoice = 'rock'
        if userLastChoice == 'scissors' :
            CPUChoice = 'paper'
        print("CPU chose " + CPUChoice)
        return coreLogic(CPUChoice,Choice)
            
def resultProcess(result) :
    global userScore
    global CPUScore
    if result == 'win' :
        print("You won!")
        userScore +=1
    if result == 'tie' :
        print("You tied!")
    if result == 'lose' :
        print("You Lost!!")
        CPUScore +=1
        
def scoreProcess() :
    if userScore == 2 :
        print(name + " won 2 out of three rounds! Your mother should be proud!")
        exit()
    elif CPUScore == 2 :
        print(name + " lost out of three rounds! Your father must be disappointed")
        exit()

def inputValidate(choice) :
    if choice not in ['rock' , 'paper', 'scissors'] :
        raise Exception('Invalid choice')

#collect input options
print("Welcome to Gabe's Rock Paper Scissors Game!")
print("Please enter you name:")
name = input()
print("Hello " + name)
print ("Please select difficulty: random or smart")
userSelectedDifficulty = input()

#validate input
if userSelectedDifficulty not in ['random' , 'smart'] :
    raise Exception('Invalid difficulty')

#collect first round
print("This game is best out of 3 rounds. Please make your first choice.")
print("Round number:", roundNumber)
print("Options are 'rock paper scissors'")
choice = input()
inputValidate(choice)

resultProcess(gameLogic(userSelectedDifficulty,choice))

#collect second round
print("Round number:",roundNumber,"Your Score:",userScore,"CPU Score:",CPUScore)
print("Options are 'rock paper scissors'")
choice = input()
inputValidate(choice)

resultProcess(gameLogic(userSelectedDifficulty,choice))

#check if anyone one yet
scoreProcess()

#Collect last round, assuming nobody won last round
print("Last Round!","Your Score:",userScore,"CPU Score:",CPUScore)
print("Options are 'rock paper scissors'")
choice = input()
inputValidate(choice)

resultProcess(gameLogic(userSelectedDifficulty,choice))

#find out who won or if tie
if CPUScore > userScore :
    print(name + " lost out of three rounds! Your father must be disappointed")
    exit()
elif CPUScore == userScore :
    Print(name + " and CPU tied! Please play again :)")
else :
    print(name + " won best out of three rounds! Your mother should be proud!")
    exit()