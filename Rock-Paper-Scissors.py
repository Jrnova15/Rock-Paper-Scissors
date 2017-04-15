
#Date: 12/8/2015
#Final Project: Make Rock - Paper - Scissors a GUI Game.


from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import time
import random
import sys

#Starts Game
def play():
    canvas.create_rectangle(50, 100, 550, 644, fill="#3d2106", outline="#3d2106")
    intro = canvas.create_text(300, 325, text="Welcome to Rock - Paper - Scissors!!!\nPlease enter your name.", font=("Comic Sans MS",25), fill=("white"))
    name()

#Ends Game
def stop():

    global playerScore
    global computerScore
    global score
    
    canvas.create_rectangle(50, 100, 550, 644, fill="#3d2106", outline="#3d2106")
    bye = canvas.create_text(300, 300, text="Thank you for playing, Good bye.", font=("Comic Sans MS",25), fill=("white"))
    playerScore = 0
    computerScore = 0
    score = 0

#Enters Name    
def name():

    
    global player
    player = 1
 
    
    while (player != 0):
        player = tkinter.simpledialog.askstring("STEP ONE", "Please enter your name: ")  
        if(len(player) == 0):
         tkinter.messagebox.showwarning("WAIT!!!", "Please enter your name again or quit: ") 
        elif(len(player) > 3):
         tkinter.messagebox.showwarning("WAIT!!!", "Name can only be 3 characters!!! ")
        elif(len(player) < 3):
         tkinter.messagebox.showwarning("WAIT!!!", "Name needs 3 characters!!! ")
 
 
        else:
         inputOpponents = canvas.create_text(190, 215, text="Opponents:", font=("Comic Sans MS",25), fill=("white"))
         canvas.create_rectangle(50, 245, 550, 644, fill="#3d2106", outline="#3d2106")
         inputName = canvas.create_text(190, 245, text=str.upper(player), font=("Comic Sans MS",25), fill=("white"))
         inputCom = canvas.create_text(190, 275, text="COM", font=("Comic Sans MS",25), fill=("white"))
         setScore()
         break

#Set Score
def setScore():
   
    global playerScore
    global computerScore
    global score
    global player
    global counter
    
    score = 1
    

    if(player == 1):
      tkinter.messagebox.showwarning("WAIT!!!", "ENTER YOUR NAME FIRST!!!")
      name()

    while(score != 0):
        score = tkinter.simpledialog.askstring("ALMOST THERE!!!", "Please enter the score total you want the game to end or quit: ") 
        if(score == "0"):
         tkinter.messagebox.showwarning("WAIT!!!", "NO ZERO!!!")

        elif(len(score) == 0):
         tkinter.messagebox.showwarning("WAIT!!!", "Can't have an empty score.")
        

        elif(score.isdigit() == True):
         canvas.create_rectangle(50, 200, 550, 333, fill="#3d2106", outline="#3d2106")
         canvas.create_rectangle(50, 290, 550, 644, fill="#3d2106", outline="#3d2106")
         
 
         canvas.create_text(400, 215, text="Score Set:", font=("Comic Sans MS",25), fill=("white"))
         canvas.create_text(400, 245, text=score, font=("Comic Sans MS",25), fill=("white"))
         canvas.create_text(300, 355, text="START PLAYING!!!", font=("Comic Sans MS",45), fill=("white"))

         inputOpponents = canvas.create_text(190, 215, text="Opponents:", font=("Comic Sans MS",25), fill=("white"))
         canvas.create_rectangle(50, 100, 550, 200, fill="#3d2106", outline="#3d2106")
         inputName = canvas.create_text(190, 245, text=str.upper(player), font=("Comic Sans MS",25), fill=("white"))
         inputCom = canvas.create_text(190, 275, text="COM", font=("Comic Sans MS",25), fill=("white"))
         playerScore = 0
         computerScore = 0
         counter = 0
         break
        

#Adds Points     
def addScore():

    global computerScore
    global playerScore
    global player
    
    
    #Track of Score    
    canvas.create_text(210, 530, text="Score:", font=("Comic Sans MS",25), fill=("white"))
 

    canvas.create_text(310, 530, text=str.upper(player), font=("Comic Sans MS",25), fill=("white"))
    canvas.create_text(310, 560, text=playerScore, font=("Comic Sans MS",25), fill=("white"))

    canvas.create_text(400, 530, text="COM", font=("Comic Sans MS",25), fill=("white"))
    canvas.create_text(400, 560, text=computerScore, font=("Comic Sans MS",25), fill=("white"))

    
    #To decide winner and alert user for a rematch
    if(float(computerScore) == float(score)):
        canvas.create_rectangle(50, 100, 550, 300, fill="#3d2106", outline="#3d2106")
        canvas.create_text(300, 125, text="Computer Wins Game!!!", font=("Comic Sans MS",45), fill=("white"))
        canvas.create_text(300, 610, text="♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦", font=("Comic Sans MS",45), fill=("white"))
        app.skull = tkinter.PhotoImage(file="skull.gif")
        app.skullRun = canvas.create_image(375, 160, anchor = NE, image=app.skull)
        

 
       
    elif(float(playerScore) == float(score)):
        canvas.create_rectangle(50, 100, 550, 300, fill="#3d2106", outline="#3d2106")
        canvas.create_text(300, 125, text=str.upper(player) + "'s The CHAMP!!!", font=("Comic Sans MS",45), fill=("white"))
        canvas.create_text(300, 610, text="★★★★★★★★★★", font=("Comic Sans MS",45), fill=("white"))
        app.trophy = tkinter.PhotoImage(file="trophy.gif")
        app.trophyRun = canvas.create_image(375, 160, anchor = NE, image=app.trophy)
       
        

    if(float(computerScore) > float(score)):
        canvas.create_rectangle(50, 100, 550, 644, fill="#3d2106", outline="#3d2106")
        canvas.create_text(300, 150, text=str.upper(player) +", HIT THE REMATCH BUTTON\nTO PLAY AGAIN!!!", font=("Comic Sans MS",25), fill=("white"))
        canvas.create_text(300, 600, text=str.upper(player) +", HIT THE REMATCH BUTTON\nTO PLAY AGAIN!!!", font=("Comic Sans MS",25), fill=("white"))
        app.stop = tkinter.PhotoImage(file="stop.gif")
        app.stopRun = canvas.create_image(450, 200, anchor = NE, image=app.stop)

        
       
    elif(float(playerScore) > float(score)):
        canvas.create_rectangle(50, 100, 550, 644, fill="#3d2106", outline="#3d2106")
        canvas.create_text(300, 150, text=str.upper(player) + ", HIT THE REMATCH BUTTON\nTO PLAY AGAIN!!!", font=("Comic Sans MS",25), fill=("white"))
        canvas.create_text(300, 600, text=str.upper(player) + ", HIT THE REMATCH BUTTON\nTO PLAY AGAIN!!!", font=("Comic Sans MS",25), fill=("white"))
        app.stop = tkinter.PhotoImage(file="stop.gif")
        app.stopRun = canvas.create_image(450, 200, anchor = NE, image=app.stop)



#Rock Button
def pickRock():

    
    global playerScore
    global computerScore
    global score
    global counter

    
    
    if(score == 0):
         tkinter.messagebox.showwarning("WAIT!!!", "SET NAME AND SCORE!!!")
         play()

    canvas.create_rectangle(50, 300, 550, 644, fill="#3d2106", outline="#3d2106")
    canvas.create_text(300, 340, text="You picked Rock", font=("Comic Sans MS",25), fill=("white"))
    app.rock = tkinter.PhotoImage(file="Player_rock.gif")
    app.rockRun = canvas.create_image(210, 415, anchor = NE, image=app.rock)



    computerChoices = [rockButton, paperButton, scissorButton]
    computerPicks = random.choice(computerChoices)



    if (computerPicks == paperButton ):
        canvas.create_text(300, 470, text="Winner ►", font=("Comic Sans MS",25), fill=("white"))
        computerScore += 1
        addScore()
            
    elif(computerPicks != paperButton and computerPicks != rockButton ):
        canvas.create_text(300, 470, text="◄ Winner", font=("Comic Sans MS",25), fill=("white"))
        playerScore += 1
        addScore()
        
        

    if (computerPicks == rockButton):
        canvas.create_text(300, 400, text="Computer picked Rock", font=("Comic Sans MS",25), fill=("white"))
        canvas.create_text(300, 470, text="Draw", font=("Comic Sans MS",25), fill=("white"))
        app.comRock = tkinter.PhotoImage(file="Computer_rock.gif")
        app.comRockRun = canvas.create_image(545, 415, anchor = NE, image=app.comRock)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()

    elif (computerPicks == paperButton):
        canvas.create_text(300, 400, text="Computer picked Paper", font=("Comic Sans MS",25), fill=("white"))
        app.comPaper = tkinter.PhotoImage(file="Computer_paper.gif")
        app.comPaperRun = canvas.create_image(545, 425, anchor = NE, image=app.comPaper)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()

    elif (computerPicks == scissorButton):
        canvas.create_text(300, 400, text="Computer picked Scissors", font=("Comic Sans MS",25), fill=("white"))
        app.comScissor = tkinter.PhotoImage(file="Computer_scissor.gif")
        app.comScissorRun = canvas.create_image(545, 435, anchor = NE, image=app.comScissor)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()


#Paper Button           
def pickPaper():

    global playerScore
    global computerScore
    global score
    global counter
      
    
    if(score == 0):
         tkinter.messagebox.showwarning("WAIT!!!", "SET NAME AND SCORE!!!")
         play()
    
    canvas.create_rectangle(50, 300, 550, 644, fill="#3d2106", outline="#3d2106")
    canvas.create_text(300, 340, text="You picked Paper", font=("Comic Sans MS",25), fill=("white"))
    app.paper = tkinter.PhotoImage(file="Player_paper.gif")
    app.paperRun = canvas.create_image(210, 425, anchor = NE, image=app.paper)


    computerChoices = [rockButton, paperButton, scissorButton]
    computerPicks = random.choice(computerChoices)

    
    if (computerPicks == rockButton):
        canvas.create_text(300, 470, text="◄ Winner", font=("Comic Sans MS",25), fill=("white"))
        playerScore += 1
        addScore()
            
    elif(computerPicks != rockButton and computerPicks != paperButton):
       canvas.create_text(300, 470, text="Winner ►", font=("Comic Sans MS",25), fill=("white"))
       computerScore += 1
       addScore()



    if (computerPicks == paperButton):
        canvas.create_text(300, 400, text="Computer picked Paper", font=("Comic Sans MS",25), fill=("white"))
        canvas.create_text(300, 470, text="Draw", font=("Comic Sans MS",25), fill=("white"))
        app.comPaper = tkinter.PhotoImage(file="Computer_paper.gif")
        app.comPaperRun = canvas.create_image(545, 425, anchor = NE, image=app.comPaper)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()
        
    elif (computerPicks == rockButton):
        canvas.create_text(300, 400, text="Computer picked Rock", font=("Comic Sans MS",25), fill=("white"))
        app.comRock = tkinter.PhotoImage(file="Computer_rock.gif")
        app.comRockRun = canvas.create_image(545, 415, anchor = NE, image=app.comRock)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()

    elif (computerPicks == scissorButton):
        canvas.create_text(300, 400, text="Computer picked Scissors", font=("Comic Sans MS",25), fill=("white"))
        app.comScissor = tkinter.PhotoImage(file="Computer_scissor.gif")
        app.comScissorRun = canvas.create_image(545, 435, anchor = NE, image=app.comScissor)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()



#Scissors Button
def pickScissors():

   global playerScore
   global computerScore
   global score
   global counter


   if(score == 0):
         tkinter.messagebox.showwarning("WAIT!!!", "SET NAME AND SCORE!!!")
         play()
    
   canvas.create_rectangle(50, 300, 550, 644, fill="#3d2106", outline="#3d2106")
   canvas.create_text(300, 340, text="You picked Scissors", font=("Comic Sans MS",25), fill=("white"))
   app.scissor = tkinter.PhotoImage(file="Player_scissor.gif")
   app.scissorRun = canvas.create_image(210, 435, anchor = NE, image=app.scissor)


   computerChoices = [rockButton, paperButton, scissorButton]
   computerPicks = random.choice(computerChoices)

   
   if (computerPicks == rockButton):
            canvas.create_text(300, 470, text="Winner ►", font=("Comic Sans MS",25), fill=("white"))
            computerScore += 1
            addScore()
            
   elif(computerPicks != rockButton and computerPicks != scissorButton):
        canvas.create_text(300, 470, text="◄ Winner", font=("Comic Sans MS",25), fill=("white"))
        playerScore += 1
        addScore()


   if (computerPicks == scissorButton):
        canvas.create_text(300, 400, text="Computer picked Scissors", font=("Comic Sans MS",25), fill=("white"))
        canvas.create_text(300, 470, text="Draw", font=("Comic Sans MS",25), fill=("white"))
        app.comScissor = tkinter.PhotoImage(file="Computer_scissor.gif")
        app.comScissorRun = canvas.create_image(545, 435, anchor = NE, image=app.comScissor)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()
        
   elif (computerPicks == rockButton):
        canvas.create_text(300, 400, text="Computer picked Rock", font=("Comic Sans MS",25), fill=("white"))
        app.comRock = tkinter.PhotoImage(file="Computer_rock.gif")
        app.comRockRun = canvas.create_image(545, 415, anchor = NE, image=app.comRock)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()                            
    
   elif (computerPicks == paperButton):
        canvas.create_text(300, 400, text="Computer picked Paper", font=("Comic Sans MS",25), fill=("white"))
        app.comPaper = tkinter.PhotoImage(file="Computer_paper.gif")
        app.comPaperRun = canvas.create_image(545, 425, anchor = NE, image=app.comPaper)
        counter += 1
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        canvas.create_text(495, 310, text=str(counter) + " counts", font=("Comic Sans MS",20), fill=("white"))
        addScore()


 

# main program
app = Tk()
app.title("Rock - Paper - Scissors Game")


canvas = Canvas(bg="black", height=700, width=600)
canvas.pack(side = TOP)


background = PhotoImage(file="backgroundNew.gif")
backgroundRun = canvas.create_image(602, 0, anchor = NE, image=background)

playButton=Button(app)
photo=PhotoImage(file="playButton.gif")
playButton.config(image=photo,width="100",height="100", command=play)
playButton.pack(side=LEFT)

rematchButton=Button(app)
photoRematch=PhotoImage(file="rematch.gif")
rematchButton.config(image=photoRematch,width="100",height="100", command=setScore)
rematchButton.pack(side=LEFT)

rockButton=Button(app, text="rock")
photoRock=PhotoImage(file="P1_rock.gif")
rockButton.config(image=photoRock,width="100",height="100", command=pickRock)
rockButton.pack(side=LEFT)

paperButton=Button(app)
photoPaper=PhotoImage(file="P1_paper.gif")
paperButton.config(image=photoPaper,width="100",height="100", command=pickPaper)
paperButton.pack(side=LEFT)

scissorButton=Button(app)
photoScissor=PhotoImage(file="P1_scissor.gif")
scissorButton.config(image=photoScissor,width="100",height="100",command=pickScissors)
scissorButton.pack(side=LEFT)

quitButton=Button(app)
bye=PhotoImage(file="quitButton.gif")
quitButton.config(image=bye,width="100",height="100", command=stop)
quitButton.pack(side=LEFT)



#For Global Variable
player = 1
computerScore = 0
playerScore = 0
score = 0
counter = 0

mainloop( )

      
    

