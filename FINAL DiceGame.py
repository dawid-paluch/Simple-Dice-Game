#imported things
import csv
import random as rnd

#functions
def findLoginInfo ():
    csvFile = open ('user information.csv')
    userInfo = (csvFile)
    userList = []
    heading = True
    for row in userInfo:
        if heading == False:
            user=row.strip().split(",")
            heading = ['Name','Username','Password']
            data = zip(heading,user)
            userDataDict =dict (data)
            userList.append(userDataDict)
        heading = False
    csvFile.close()
    return (userList)
def newUser():
    userList = findLoginInfo()
    validName = False
    while validName == False:
        validName = True
        name = input("What name would you like to show up as you in game?")
        nameLength = len(name)
        if nameLength < 3:
            validName = False
            print("Your password is too short. It should be at least three characters long.")
        elif nameLength > 12:
            validName = False
            print("Your name is too long. It should be less than thirteen characters long.")
    validUsername = False
    while validUsername == False:
        username = input("What would you like the username for your account to be?")
        username = username.lower()
        availability = True
        for item in userList:
            if item['Username'] != username and availability == True:
                validUsername = True
            else:
                validUsername = False
                availability = False
        if availability == False:
            print("This username is taken. Please try again.")
        usernameLength = len(username)
        if usernameLength < 3:
            validUsername = False
            print("Your username is too short. It should be at least three characters long.")
        elif usernameLength > 12:
            validUsername = False
            print("Your username is too long. It should be less than thirteen characters long.")
    validPassword = False
    while validPassword == False:
        validPassword = True
        password = input("What would you like your password to be?")
        passwordLength = len(password)
        if passwordLength < 3:
            validPassword = False
            print("Your password is too short. It should be at least three characters long.")
        elif passwordLength > 18:
            validPassword = False
            print("Your password is too long. It should be less than nineteen characters long.")
        
    newUserInfo = [{'Name':name,'Username':username,'Password':password}]
    try:
        fileHandle = open('user information.csv', 'r+')
        fileContent = fileHandle.read()
        if fileContent.strip()=='':
            fileHandle.write('Name,Username,Password\n')
        for item in newUserInfo:
            fileHandle.write('{Name},{Username},{Password}'.format(**item))
            fileHandle.write('\n')
        fileHandle.close()
    except OSError:
        print('Can\'t write to file!')   
def logIn(loggedInUser):
    loggedIn = False
    while loggedIn == False:
        userList = findLoginInfo()
        username = input("What is your username?")
        password = input("What is your password?")
        username = username.lower()
        for item in userList:
            if item['Username'] == username and item['Password'] == password and username != loggedInUser:
                name = item['Name']
                loggedIn = True
        if loggedIn == False:
            print("Your username or password doesn't exist or is already in use.")
            newAccount = input("If you would like to make a new account type yes.")
            if newAccount == "yes":
                    newUser()
    return(name,username)
def rollDice ():
    input("Press Enter to roll the dice.")
    die1 = rnd.randint(1,6)
    die2 = rnd.randint(1,6)
    total = die1 + die2
    if total % 2 == 0:
        total += 10
    else:
        total -= 5
    if die1 == die2:
        die3 = rnd.randint(1,6)
        print ("You rolled two ", die1,
               ". You rolled another die and got a ",die3,
               ". You got a total of ",total,".")
    else:
        print("You rolled a ", die1," and a ",
          die2,".You got a total of ",total,".")
    return(total)
def finalResults(user1,user2,total1,total2):
    print(user1," you finished with a score of ",total1,".")
    print(user2," you finished with a score of ",total2,".")
    if total1 > total2:
        print(user1," is the winner.")
        return(user1,total1)
    else:
        print(user2," is the winner.")
        return(user2,total2)
def saveData ():
    try:
        fileHandle = open('highscores.csv', 'r+')
        fileContent = fileHandle.read()
        if fileContent.strip()=='':
            fileHandle.write('Username,Score\n') 
        for item in saveScore:
            fileHandle.write('{Username},{Score}'.format(**item))
            fileHandle.write('\n')
        fileHandle.close()
    except OSError:
        print('Can\'t write to file!')
def getSortKey(item):
    return item['Score']
import os
def showHighscores ():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    scoresData = open ('highscores.csv')
    scoresInfo = (scoresData)
    scoresList = []
    heading = True
    for row in scoresInfo:
        if heading == False:
            scores = row.strip().split(",")
            heading = ['Username','Score']
            data = zip(heading,scores)
            scoresDataDict =dict (data)
            scoresList.append(scoresDataDict)
        heading = False
    scoresData.close()
    scoresList.sort(key=getSortKey,reverse=True)
    print("\n\nTop Five Scores")
    for n in range (0,5):
        player = scoresList[n]
        print(n+1, ") ",player["Score"], player['Username'])
    

#login system
print("Welcome to this die game.")
instructions = "\n\nThis game is played by two users rolling dice. Each round both users will roll two dice and they will gain points equal to the sum of the dice. If the total of the rolls is even, the an extra 10 points are added. If it's odd, 5 points are taken away. If the two dice are the same, a third dice is also rolled along with the first two. There will be 5 rounds unless the scores of both players are equal, in which case the game will go on until  there is a difference in scores."
carryOn = False
while carryOn == False:
    print ("\nDIE GAME MAIN MENU \nPlease enter the number for what you'd like to do.\n\n     1) Play Game\n     2) View Highscores\n     3) View Instructions\n     4) Make New User")
    userChoice = int(input("User Choice: "))
    if userChoice == 1:
        carryOn = True
    elif userChoice == 2:
        showHighscores()
    elif userChoice == 3:
        print(instructions)
    elif userChoice == 4:
        newUser()
user1,username1 = logIn("FALSE")
user2,username2 = logIn(username1)

#certain variables zeroed
total1 = 0
total2 = 0

#main game
for x in range (0,5):
    score = 0
    print("Round ",x+1,", ",user1)
    score = rollDice()
    total1 += score
    print ("Total score for ",user1," is ",total1,".")
    score = 0
    print("Round ",x+1,", ",user2)
    score = rollDice ()
    total2 += score
    print ("Total score for ",user2," is ",total2,".")
    total1 = total2

while total1 == total2:
    print("Both scores are equal so a tie breaker will take place.")
    total1 += rnd.randint(1,6)
    total2 += rnd.randint(1,6)
    print("The current score for ",user1," is ",total1," and the current score for ",user2," is ",total2,".")
    
#results
winner,winningScore = finalResults(user1,user2,total1,total2)

saveScore = [{'Username':winner,'Score':winningScore}]
saveData()
showHighscores()
