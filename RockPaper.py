# Rock Paper Python V1.0
# Written by Gabe Conway 4/23/2020
# Standard rock paper scissors game with two AI modes, best out of three rounds. Random mode will choose a random selection.
# Smart mode will base its choice on statistics. The strategy is based on experiments of Zhejiang University.

import random

#Variable declaration

userScore = 0
CPUScore = 0
options = ['rock' , 'paper' , 'scissors']
gameModes = ['random' , 'smart']
userLastChoice = None
beats={
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

#functions
def coreLogic(CPU,User):
    if User == CPU :
        return "tie"
    if beats[CPU] != User:
        return "lose"
    else:
        return "win"

def randomMode():
    CPUChoice = random.choice(options) 
    print("CPU chose " + CPUChoice)
    return CPUChoice

def smartMode():
    beats={
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    CPUChoice = beats[userLastChoice]
    print("CPU chose " + CPUChoice)
    return CPUChoice
        
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
    if choice not in options :
        raise Exception('Invalid choice')
    return choice

#collect input options
print("Welcome to Gabe's Rock Paper Scissors Game!")
print("Please enter you name:")
name = input()
print("Hello " + name)
print (f"Please select difficulty: {gameModes}")
Difficulty = input()
#validate input
if Difficulty not in gameModes :
    raise Exception('Invalid difficulty')

#collect first round
print("This game is best out of 3 rounds. Please make your first choice.")
roundNumber = 1
while roundNumber < 4:
    print("Round number:",roundNumber,"Your Score:",userScore,"CPU Score:",CPUScore)
    print(f"Options are {options}")
    choice = inputValidate( input() )
    
    if Difficulty == 'random':
        CPUChoice = randomMode()
        resultProcess( coreLogic(CPUChoice,choice) )

    if Difficulty == 'smart':
        if roundNumber == 1:
            CPUChoice = randomMode()
            resultProcess( coreLogic(CPUChoice,choice) )
        else: 
            CPUChoice = smartMode()
            resultProcess( coreLogic(CPUChoice,choice) )

    roundNumber +=1
    scoreProcess()
    userLastChoice = choice

#find out who won or if tie
if CPUScore > userScore :
    print(name + " lost out of three rounds! Your father must be disappointed")
elif CPUScore == userScore :
    print(name + " and CPU tied! Please play again :)")
else :
    print(name + " won best out of three rounds! Your mother should be proud!")