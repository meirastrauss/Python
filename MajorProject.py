#Major Project
#Meira Strauss
import random
import time
start=time.time()

NUM_SQUARES=20
def new_board():
    #create new game board
    board = []
    position=0
    for temp1 in range(4):
        for temp in range(5):
            board.append(chr(random.randrange(65,91)))
            position+=1
    return board
def display_board(board):
    #display game board on screen
    print("\n\t",board[0],"|",board[1],"|",board[2],"|",board[3],"|",board[4])
    print("\t -----------------")
    print("\t",board[5],"|",board[6],"|",board[7],"|",board[8],"|",board[9])
    print("\t -----------------")
    print("\t",board[10],"|",board[11],"|",board[12],"|",board[13],"|",board[14])
    print("\t -----------------")
    print("\t",board[15],"|",board[16],"|",board[17],"|",board[18],"|",board[19],"\n")

def addHighScore(name, score):
    scoreFile=open("scoreFile.txt","r")
    counter=0
    scoreArray=[]
    for line in  scoreFile:
        scoreArray.append(int(line))
    for s in scoreArray:
        if score>s:
            scoreArray.insert(counter, score)
            break
        counter+=1
    if counter== len(scoreArray):
        scoreArray.append(score)
    scoreFile.close()
    nameFile=open("nameFile.txt", "r")
    temp=0
    nameArray=[]
    for nameHS in nameFile:
        nameArray.append(nameHS.strip())
        temp+=1
    
    nameFile.close()
    nameFile=open("nameFile.txt", "w")
    scoreFile=open("scoreFile.txt","w")
    if counter==len(nameArray):
        nameArray.append(name)
    else:
        nameArray.insert(counter, name)
    if(len(nameArray)>10):
        nameArray.pop(len(nameArray)-1)
        scoreArray.pop(len(scoreArray)-1)
    for obj in scoreArray:
        scoreFile.write(str(obj))
        scoreFile.write("\n")
    for obj in nameArray:
        nameFile.write(str(obj))
        nameFile.write("\n")
    scoreFile.close()
    nameFile.close()
        
            

def checkHighScore(score):
    scoreFile=open("scoreFile.txt","r")
    highScore=False
    scoreArray=[]
    for line in scoreFile:
        counter=0
        scoreArray.append(line)
        if score>int(line):
            highScore=True
    if len(scoreArray)<10:
        highScore=True
    scoreFile.close()
    return highScore
    

def printHighScore():
    print("High Scores:\n")
    scoreFile=open("scoreFile.txt","r")
    nameFile=open("nameFile.txt","r")
    scoreArray=[]
    nameArray=[]
    temp=0
    for scoreHS in scoreFile:
        scoreArray.append(scoreHS)
        temp+=1
    temp=0
    for nameHS in nameFile:
        nameArray.append(nameHS)
        temp+=1
    counter=1
    for nameHS in nameArray:
        print(counter, "\t", nameArray[counter-1].strip(),"\t",scoreArray[counter-1].strip())
        counter+=1
    scoreFile.close()
    nameFile.close()
    
def main():
    board=new_board()
    choice=""
    print("Menu")
    print("1- Play the Game")
    print("2- High Scores")
    print("3- Quit")
    print()
    choice= input("")
    while choice != "3":
        if choice=="1":
            score=0
            start=time.time()
            while time.time()-start<60:
                invalid= False
                display_board(board)
                word=input("").upper()
                #create temp board
                tempboard = []
                for option in range(NUM_SQUARES):
                    tempboard.append(board[option])
                for letter in word:
                    foundIt=False
                    counter=-1
                    for option in tempboard:
                        counter+=1
                        if option==letter and foundIt==False:
                            tempboard.remove(tempboard[counter])
                            foundIt=True
                    if foundIt==False:
                        print("Invalid Entry- Not in options")
                        invalid=True
                        break
                    else:
                        foundIt==False
                #check to see if in dictionary
                text_file=open("wordlist.txt","r")
                foundIt=False
                for diction in text_file:
                    if diction==word.lower()+"\n":
                        foundIt=True
                        break
                if foundIt==False:
                    print("Invalid Entry- Not in dictionary")
                    invalid=True
                text_file.close()

                if len(word)<3:
                    print("Invalid Entry- Less than 3 letters")
                    invalid=True
                #Replace letters
                if invalid==False:
                    for letter in word:
                        ind= board.index(letter)
                        board[ind]=(chr(random.randrange(65,91)))
                        score+=1
            print("Your score is", score)
            isHighScore=False
            isHighScore=checkHighScore(score)
            if isHighScore==True:
                print("You got a high score!!!!")
                name=input("What is your name? ")
                addHighScore(name, score)
            elif isHighScore==False:
                print("This is not a high score")
            printHighScore()
            board=new_board()
            print("Menu")
            print("1- Play the Game")
            print("2- High Scores")
            print("3- Quit")
            print()
            choice= input("")
        elif choice=="2":
            printHighScore()
            print("Menu")
            print("1- Play the Game")
            print("2- High Scores")
            print("3- Quit")
            print()
            choice= input("")
    print("Thanks for playing!")



main()
