""" Culminating project - race game """
""" Chaza Elfizy """
""" 2023/05/03 """
# In this program, two people can race against each other all while avoiding projectiles

# importing graphics, time, and random libraries
from graphics import *
from random import *
import time;

# variables to keep scores
plyr1pnts = 0;
plyr2pnts = 0; 

# function to reset the game whenever a character reaches the finishline
def reset():
    resetText = Text(Point(500, 140), "Press X to play again.  Press Q to exit game.")
    resetText.draw(win);
    keyWin = win.getKey();

    # while loop to wait for a key from the user to reset or exit game
    while keyWin == "x" or keyWin == "q":

        # if to reset the characters
        if keyWin == "x":
            rtrnX2 = (verifyX2 - 100)
            rtrnY2 = (verifyY2 - 315)
            for part in plyr2:
                part.move(-rtrnX2, -rtrnY2);

            rtrnX =(verifyX - 100 )
            rtrnY = (verifyY - 90)
            for part in plyr1:
                part.move(-rtrnX, -rtrnY);

            resetText.undraw()
            keyWin = "e"
        # else to exit the game    
        elif keyWin == "q":
            win.close()

    
# creating the window and grass
win = GraphWin("Game Arena", 1000, 685);
win.setBackground("#64865F");
grass = Image(Point(500, 342.5), "lawn.png");
grass.draw(win);

# drawing the finish line
finishLine = Image(Point(900, 343), "finishLine.png");
finishLine.draw(win);

# title page
titlePage = Rectangle(Point(0,0), Point(1000, 685));
titlePage.setFill("#23411E");
titleText = Text(Point(500, 343), "Dodge The Tumbleweed!");
titleText.setFace("helvetica");
titleText.setSize(35);
titleText.setTextColor("black")
                      
titleText2 = Text(Point(505, 343), "Dodge The Tumbleweed!");
titleText2.setFace("helvetica");
titleText2.setSize(35);
titleText2.setTextColor("white")

titlepage = [titleText, titleText2]
titlePage.draw(win);

# drawing the page
for part in titlepage:
    part.draw(win);
time.sleep(3)

# moving the text off the screen
for movement in range (0, 1000):
    for part in titlepage:
        part.move(2, 0)

# instructions page
instrucText = Text(Point(-100, 300), "Use WSD for player one and IKL for player two");
instrucText.setFace("helvetica");
instrucText.setSize(28)
instrucText.setTextColor("black");

instrucText2 = Text(Point(-100, 360), "Dodge the tumbleweed and reach the finishline before your friend!")
instrucText2.setFace("helvetica");
instrucText.setSize(28)
instrucText.setTextColor("black");

instructions = [instrucText, instrucText2]

# drawing the page
for part in instructions:
    part.draw(win);

# moving the instructions onto the screen
for movement in range (0, 300):
    for part in instructions:
        part.move(2, 0)
time.sleep(5)

# moving the text off the screen
for movement in range (0, 500):
    for part in instructions:
        part.move(2, 0)
titlePage.undraw();
       
# first player
x = 100
y = 90
plyr1Head = Circle(Point(x,y), 20);
plyr1Head.setFill("#C8CBE6");
verifyPoint = Point(x, y);
plyr1Body = Line(Point(x, y+20), Point(x, y+60));
plyr1Arms = Line(Point(x-20, y+40), Point(x+20, y+40));
plyr1Leg1 = Line(Point(x, y+60), Point(x+10, y+75));
plyr1Leg2 = Line(Point(x, y+60), Point(x-10, y+75));
plyr1 = [verifyPoint, plyr1Head, plyr1Body, plyr1Arms, plyr1Leg1, plyr1Leg2];

# second player
x2 = 100
y2 = 315
plyr2Head = Circle(Point(x2,y2), 20);
plyr2Head.setFill("#E6C8DD");
verifyPoint2 = Point(x2, y2);
plyr2Body = Line(Point(x2, y2+20), Point(x2, y2+60));
plyr2Arms = Line(Point(x2-20, y2+40), Point(x2+20, y2+40));
plyr2Leg1 = Line(Point(x2, y2+60), Point(x2+10, y2+75));
plyr2Leg2 = Line(Point(x2, y2+60), Point(x2-10, y2+75));
plyr2 = [verifyPoint2, plyr2Head, plyr2Body, plyr2Arms, plyr2Leg1, plyr2Leg2];

yPosWeed1 = [120, 232, 344] # array to give proper y values so the tumbleweed doesn't appear at a random place
#  first tumbleweed
frstWeedYPos = randint(0, 2)
frstWeedY = yPosWeed1[frstWeedYPos]
frstWeedX = 1000
tumblwd = Image(Point(frstWeedX, frstWeedY), "tumbleweed.png");
tumblwd.draw(win)

yPosWeed2 = [465, 577] # array to give proper y values so the tumbleweed doesn't appear at a random place
# second tumbleweed
scndWeedYPos = randint(0, 1)
scndWeedY = yPosWeed2[scndWeedYPos]
scndWeedX = 1500
tumblwd2 = Image(Point(scndWeedX, scndWeedY), "tumbleweed.png");
tumblwd2.draw(win)
    
# score board
scoreText = Text(Point(500, 650), "Player One: {0}     Player Two: {1}".format(plyr1pnts, plyr2pnts))
scoreText.draw(win)

# drawing the first player
for part in plyr1:
    part.draw(win);
    
# drawing the second player
for part in plyr2:
    part.draw(win);

# while loop to keep the game running
while True:
    time.sleep(0.01)
    
# if structure if the first tumbleweed reaches the edge of the arena
    if (frstWeedX <= 10):
        tumblwd.undraw()
        frstWeedYPos = randint(0, 2)
        frstWeedY = yPosWeed1[frstWeedYPos]
        frstWeedX = 1000
        tumblwd = Image(Point(frstWeedX, frstWeedY), "tumbleweed.png");
        tumblwd.draw(win)
    else:     
        tumblwd.move(-6, 0)
        frstWeedX -= 6

# if structure if the second tumbleweed reaches the edge of the arena
    if (scndWeedX <= 10):
        tumblwd2.undraw()
        scndWeedYPos = randint(0, 1)
        scndWeedY = yPosWeed2[scndWeedYPos]
        scndWeedX = 1000
        tumblwd2 = Image(Point(scndWeedX, scndWeedY), "tumbleweed.png");
        tumblwd2.draw(win)
    else:     
        tumblwd2.move(-6, 0)
        scndWeedX -= 6
        
# checking keys and getting points that verify the positions of the players
    key = win.checkKey();
    verifyX = verifyPoint.getX()
    verifyY = verifyPoint.getY();
    verifyX2 = verifyPoint2.getX()
    verifyY2 = verifyPoint2.getY();

# for first player
    # if structure in case they win
    if(verifyX == 880):
        finishTextPlyr1 = Text(Point(500, 100), "Player One has won. One point for Player One")
        finishTextPlyr1.draw(win)
        time.sleep(2);
        
        scoreText.undraw();
        
        plyr1pnts += 1;
        scoreText = Text(Point(500, 650), "Player One: {0}     Player Two: {1}".format(plyr1pnts, plyr2pnts))
        scoreText.draw(win)
        
        # calling on the reset function
        reset()
        finishTextPlyr1.undraw();
    # move the character when they click a specific key   
    elif (verifyX >= 20 and verifyX <= 980) and (verifyY >= 20 and verifyY <=590):
        if key == "d": 
            for movement in range (0, 1):
                for part in plyr1:
                    part.move(6, 0);
        elif key == "w":
            for movement in range (0, 1):
                for part in plyr1:
                    part.move(0, -112);
        elif key == "s":
            for movement in range (0, 1):
                for part in plyr1:
                    part.move(0, 112);
    # when the player reaches a border, and respawns at the original position                
    elif (verifyX < 0 or verifyX > 980) or (verifyY <0 or verifyY > 590): 
        text = Text(Point(500, 10), "Player One has reached the border. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX =(verifyX - 100)
        rtrnY = (verifyY - 90)
        for part in plyr1:
            part.move(-rtrnX, -rtrnY);
        text.undraw();
    # when the player gets hit by the second tumbleweed, to reset the player and the second tumbleweed's positions
    if (scndWeedX+50 >= verifyX+20 and scndWeedX-50 <= verifyX-20) and ((scndWeedY-50 <= verifyY+75 and scndWeedY+50 >= verifyY+75) or (scndWeedY-50 <= verifyY and scndWeedY+50 >= verifyY)):
        text = Text(Point(500, 100), "Player One has been hit. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX =(verifyX - 100)
        rtrnY = (verifyY - 90)
        for part in plyr1:
            part.move(-rtrnX, -rtrnY);
        text.undraw();
        tumblwd2.undraw()
         # (tumbleweed reset)
        scndWeedYPos = randint(0, 1)
        scndWeedY = yPosWeed2[scndWeedYPos]
        scndWeedX = 1500
        tumblwd2 = Image(Point(scndWeedX, scndWeedY), "tumbleweed.png");
        tumblwd2.draw(win)

    # when the player gets hit by a tumble weed, to reset the player and the first tumbleweed's positions
    if (frstWeedX+50 >= verifyX+20 and frstWeedX-50 <= verifyX-20) and ((frstWeedY-50 <= verifyY+75 and frstWeedY+50 >= verifyY+75) or (frstWeedY-50 <= verifyY and frstWeedY+50 >= verifyY)):
        text = Text(Point(500, 100), "Player One has been hit. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX =(verifyX - 100)
        rtrnY = (verifyY - 90)
        for part in plyr1:
            part.move(-rtrnX, -rtrnY);
        text.undraw();
        tumblwd.undraw();
         # (tumbleweed reset)
        frstWeedYPos = randint(0, 2)
        frstWeedY = yPosWeed1[frstWeedYPos]
        frstWeedX = 1000
        tumblwd = Image(Point(frstWeedX, frstWeedY), "tumbleweed.png");
        tumblwd.draw(win)

# for second player
    # if structure in case they win
    if (verifyX2 == 880):
        finishTextPlyr2 = Text(Point(500, 100), "Player Two has won. One point for Player Two")
        finishTextPlyr2.draw(win)
        time.sleep(2);
        
        scoreText.undraw();
        plyr2pnts += 1;
        scoreText = Text(Point(500, 650), "Player One: {0}     Player Two: {1}".format(plyr1pnts, plyr2pnts))
        scoreText.draw(win)

        # calling on the reset function
        reset();
        finishTextPlyr2.undraw();
        
    # move the character when they click a specific key   
    elif (verifyX2 >= 20 and verifyX2 <= 980) and (verifyY2 >= 20 and verifyY2 <=590):
        if key == "l": 
            for movement in range (0, 1):
                for part in plyr2:
                    part.move(6, 0);
        elif key == "i":
            for movement in range (0, 1):
                for part in plyr2:
                    part.move(0, -112);
        elif key == "k":
            for movement in range (0, 1):
                for part in plyr2:
                    part.move(0, 112);
                    
    # when the player reaches a border, and respawns at the original position                
    elif (verifyX2 < 0 or verifyX2 > 980) or (verifyY2 < 0 or verifyY2 > 590):
        text = Text(Point(500, 100), "Player Two has reached the border. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX2 = (verifyX2 - 100)
        rtrnY2 = (verifyY2 - 315)
        for part in plyr2:
            part.move(-rtrnX2, -rtrnY2);
        text.undraw();
        
    # when the player gets hit by the second tumbleweed, to reset the player and the second tumbleweed's positions
    if (scndWeedX+49 >= verifyX2+20 and scndWeedX-49 <= verifyX2-20) and ((scndWeedY-49 <= verifyY2+75 and scndWeedY+49 >= verifyY2+75) or (scndWeedY-49 <= verifyY2 and scndWeedY+49 >= verifyY2)):
        text = Text(Point(500, 100), "Player Two has been hit. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX2 = (verifyX2 - 100)
        rtrnY2 = (verifyY2 - 315)
        for part in plyr2:
            part.move(-rtrnX2, -rtrnY2);
        text.undraw();
        tumblwd2.undraw()
        
        # (tumbleweed reset)
        scndWeedYPos = randint(0, 1)
        scndWeedY = yPosWeed2[scndWeedYPos]
        scndWeedX = 1500
        tumblwd2 = Image(Point(scndWeedX, scndWeedY), "tumbleweed.png");
        tumblwd2.draw(win)
        
    # when the player gets hit by a tumble weed, to reset the player and the first tumbleweed's positions
    if (frstWeedX+49 >= verifyX2+20 and frstWeedX-49 <= verifyX2-20) and ((frstWeedY-40 <= verifyY2+75 and frstWeedY+40 >= verifyY2+75) or (frstWeedY-40 <= verifyY2 and frstWeedY+40 >= verifyY2)):
        text = Text(Point(500, 100), "Player Two has been hit. Respawn.");
        text.draw(win);
        time.sleep(2)
        rtrnX2 = (verifyX2 - 100)
        rtrnY2 = (verifyY2 - 315)
        for part in plyr2:
            part.move(-rtrnX2, -rtrnY2);
        text.undraw();
        tumblwd.undraw();
        
        # (tumbleweed reset)
        frstWeedYPos = randint(0, 2)
        frstWeedY = yPosWeed1[frstWeedYPos]
        frstWeedX = 1000
        tumblwd = Image(Point(frstWeedX, frstWeedY), "tumbleweed.png");
        tumblwd.draw(win)

        







