import copy
import pygame as pygame
import math
from random import randrange
from tkinter import *  
from tkinter import messagebox  
#shiet


pygame.init()

originalGameBoard = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 6, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 6, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3],  # Middle Lane Row: 14
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
    [3, 6, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 6, 3],
    [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
    [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
    [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
    [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
    [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]




gameBoard = copy.deepcopy(originalGameBoard)
spriteRatio = 3 / 2
square = 15  # Size of each unit square
spriteOffset = square * (1 - spriteRatio) * (1 / 2)
(width, height) = (len(gameBoard[0]) * square, len(gameBoard) * square)  # Game screen
#print(spriteOffset)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
game_over = False  # Biến đánh dấu sự kiện kết thúc game 

SPEED = 1/4

curPoint  = copy.deepcopy(originalGameBoard)

#print(len(gameBoard[0]))
#print(len(gameBoard))

global numOfPoint
numOfPoint=0

for i in range(len(gameBoard) ) :
    for j in range(len(gameBoard[0]) ) :
        if gameBoard[i][j] == 2:
            numOfPoint+=1
            
print(numOfPoint)
for i in range(len(gameBoard) ) :
    for j in range(len(gameBoard[0]) ) :
        if gameBoard[i][j] != 2 :
            curPoint[i][j] = 0       


pos = [13, 26]
pelletColor = (222, 161, 133)
# print(len(gameBoard[0]))  # horizontal
# print(len(gameBoard))  # vertical
clock = pygame.time.Clock()
src = "src/"
imgPacClose = "yellow2.jpg"  # hình tròn vàng
y = "image1.jpg"  # tường màu xanh
blinky = "blinky.png"
cyanghost = "cyan.jpg"

def isInt( x ) :
    if x == int(x) : 
        return True
    return False


def insideOfGameBoard( y , x ) :
    return x >= 0 and x < len(gameBoard[0]) and y >= 0 and y < len(gameBoard)


def reachCel( row , col, direct ) :
    if direct == 0 :
        return  ( math.floor(row - SPEED) , int( col ) )
    if direct == 1 :
        return  ( int( row ) , math.ceil(col + SPEED) )
    if direct == 2 :
        return  ( math.ceil(row + SPEED) , int(col) ) 
    if direct == 3 :
        return  ( int(row) , math.floor(col - SPEED) )
    return True

def canMove(row, col, direct) :

    (y,x) = reachCel(row,col,direct)

    if not insideOfGameBoard( y , x ) :
        return False

    if direct == 0 :
        return  gameBoard[ y ][ x] != 3 and isInt(col) 
    if direct == 1 :
        return  gameBoard[ y ][ x ] != 3 and isInt(row) 
    if direct == 2 :
        return  gameBoard[ y ][ x ] != 3 and isInt(col) 
    if direct == 3 :
        return  gameBoard[ y ][ x ] != 3 and isInt(row) 
    return True


#tinh' diem?
score = 0
font = pygame.font.Font('freesansbold.ttf',20)

def showScore(x,y):
    pygame.draw.rect(screen, (0, 0, 0) , (x-3 , y-3, square*8, square*2))
    strScore = font.render("Score: " + str(score),True,(255,255,255))
    screen.blit(strScore,(x,y))


class MovableObj : # include pacman, ghost
    def __init__(self, row, col, imagePath, isPacMan ):
        self.imgPath = imagePath
        self.row = row
        self.col = col
        self.speed = SPEED
        self.dir = 0  # 0: North, 1: East, 2: South, 3: West 0 là đi lên. 1 là sang phải 2 là xuống dưới 3 là sang trái
        self.newDir = 0
        self.isPacMan = isPacMan

    def startDraw(self) :
        p = pygame.image.load(src + imgPacClose)
        p = pygame.transform.scale(p, (square, square))
        screen.blit(p, (self.row * square, self.col * square, square, square))
    
    
    def update(self) :
        global score
        if self.newDir == 0:
            if canMove(self.row,self.col, self.newDir ) == True :
                self.row -= self.speed
                self.dir = self.newDir
                # print(0)
                (y,x) = reachCel(self.row,self.col,self.newDir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
                return
        elif self.newDir == 1:  # 26 , 13,5
            if canMove(self.row,self.col,1):
                self.col += self.speed
                self.dir = self.newDir
                # print(1)
                (y,x) = reachCel(self.row,self.col,self.newDir)
                if self.isPacMan == 1 :
                    if ( curPoint[y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
                return
        elif self.newDir == 2:
            if canMove(self.row,self.col,2):
                self.row += self.speed
                self.dir = self.newDir
                # print(2)
                (y,x) = reachCel(self.row,self.col,self.newDir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
                return
        elif self.newDir == 3:
            if canMove(self.row,self.col,3):
                self.col -= self.speed
                self.dir = self.newDir
                # print(3)
                (y,x) = reachCel(self.row,self.col,self.newDir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
                return
        #

        #print("does it can happen ?") 

        if self.dir == 0:
            if canMove(self.row,self.col,0):
                self.row -= self.speed
                (y,x) = reachCel(self.row,self.col,self.dir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
            # print(0)
        
        elif self.dir == 1:
            if canMove(self.row,self.col,1):
                self.col += self.speed
                (y,x) = reachCel(self.row,self.col,self.dir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
            # print(1)
        
        elif self.dir == 2:
            if canMove(self.row,self.col,2):
                self.row += self.speed
                (y,x) = reachCel(self.row,self.col,self.dir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
            # print(2)
        elif self.dir == 3:
            if canMove(self.row,self.col,3):
                self.col -= self.speed
                (y,x) = reachCel(self.row,self.col,self.dir)
                if self.isPacMan == 1 :
                    if ( curPoint[ y][ x] == 2 ) :
                        score+=1
                        showScore(5,5)
                        curPoint[ y ][ x ] = 0
            # print(3)

    def drawBlackRectangle(self, row, col) :  # draw image
        pygame.draw.rect(screen, (0, 0, 0) , (col * square, row * square, square, square))

    def drawBlackBoxAndDot(self, row, col) :
        #print(row)
        #print(col)
        if curPoint[row][col] == 2 :
            self.drawBlackRectangle(row, col)
            pygame.draw.circle(screen, pelletColor, (col * square + square // 2, row * square + square // 2),
                                square // 4)
        else :
            self.drawBlackRectangle(row, col)
           # print("yes i'm printting black box")
           # print(row,col)
    
    def clearCurObjImage(self):

        # only row or col can be float . other is not
        #print(self.row)
        #print(self.col)
        #print(isInt( self.row ))

        if isInt( self.row ) :
            self.drawBlackBoxAndDot(int(self.row), math.floor(self.col))
            self.drawBlackBoxAndDot(int(self.row), math.ceil(self.col))
        else :
            self.drawBlackBoxAndDot(math.floor(self.row), int(self.col) )
            self.drawBlackBoxAndDot(math.ceil(self.row), int(self.col) )

    # Draws pacman based on his current state

    def drawCurObjImage(self):  # draw image
        p = pygame.image.load(src + self.imgPath)
        p = pygame.transform.scale(p, (square, square))
        screen.blit(p, (self.col * square, self.row * square, square, square))


    def pause(time) :
        cur = 0
        while not cur == time:
            cur += 1


class Pacman (MovableObj):
    def __init__(self, row, col,impPac,isPacMan) :
        MovableObj.__init__(self,row,col,imgPacClose,isPacMan ) 
    

class Blinky(MovableObj):
    def __init(self,row,col,blinky,isPacMan):
        MovableObj.__init__(self,row,col,blinky,isPacMan ) 


def drawMap():
    screen.fill((0, 0, 0))  # fill background màu black
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 3:
                tileImage = pygame.image.load(src + y)
                tileImage = pygame.transform.scale(tileImage, (square, square))
                screen.blit(tileImage, (j * square, i * square, square, square))
            elif gameBoard[i][j] == 2:  # Draw Tic-Tak
                pygame.draw.circle(screen, pelletColor, (j * square + square // 2, i * square + square // 2),
                                square // 4)


drawMap()
fps = 30
fpsClock = pygame.time.Clock()

#create and create character

P = Pacman(26, 14,imgPacClose,1)

S1 = Blinky(16,14,blinky,0)

S2 = Blinky(18,14,cyanghost,0)

P.startDraw
S1.startDraw
S2.startDraw
pygame.display.update()



def doGhostMovRand():
    while True :
        new = randrange(4)
        if new != S1.dir: 
            S1.newDir = new
            break
        new = randrange(4)
        if new != S2.dir: 
            S2.newDir = new
            break
step = 0 


### MINIMAXXXXXXX

mnmCurPoint  = copy.deepcopy(curPoint)

class Node:
    def __init__(self,PacmanPosition,pG1,pG2):
        self.PP = PacmanPosition
        self.G1 = pG1
        self.G2 = pG2
    

def isTouch(a , b) :
    if  a[0] == b[0] and abs( a[1]  - b[1] ) < 1.0 :
        return True 
    if  a[1] == b[1] and abs( a[0]  - b[0] ) < 1.0 :
        return True 
    return False

def pacIsBlocked( node ):
    return False

#some contance
global NUM_MAP_DOT
NUM_MAP_DOT=0

for i in range(len(gameBoard) ) :
    for j in range(len(gameBoard[0]) ) :
        if gameBoard[i][j] == 2:
            NUM_MAP_DOT+=1

MAXIMUMSCORE = 10000 * 10000
INF = 100000 * 100000

remDot = numOfPoint
print(f'Rem dot : {remDot}')

def isPacWin(curDot):
    return curDot >= NUM_MAP_DOT

def randomD():
    l1 = randrange(1000000000)
    m1 = randrange(1000000000)
    x1 = l1 % m1
    print(x1)
    l1 = randrange(1000000000)
    m1 = randrange(1000000000)
    print(x1)
    x1 = x1 +  l1 % m1
    return x1 % 4


# return ( score , list of point ) alway is G1 , G2
# *** ( row , col )
# 0 - up, 1 - right, 2 - down, 3 - left
SPEEDP = 1/4
d4val = [ (-SPEEDP,0), (0,SPEEDP), (SPEEDP,0), (0,-SPEEDP)  ]
SPEEDG = 2/4
d4valG = [ (-SPEEDG,0), (0,SPEEDG), (SPEEDG,0), (0,-SPEEDG)  ]


def inside( a , b1, b2 ) :
    if b1[0] == b2[0] and a[0] == b1[0] :
        l = min( b1[1] , b2[1] )
        r = max( b1[1] , b2[1] )
        return l <= a[1] and a[1] <= r
    if b1[1] == b2[1] and a[1] == b1[1] :
        l = min( b1[0] , b2[0] )
        r = max( b1[0] , b2[0] )
        return l <= a[0] and a[0] <= r

    return False
        
    

def isPacLose( node , d1 , d2 ):
    #check pacman is touched by ghost
        return inside( node.PP , ( node.G1[0] - d4valG[d1][0] , node.G1[1] - d4valG[d1][1] ) , node.G1 ) or inside( node.PP , ( node.G2[0] - d4valG[d2][0] , node.G2[1] - d4valG[d2][1] ) , node.G2 )
    #check pacman is touched by ghost


def minimax(node, isMax, depth, curScore, alpha, beta, curDot, dir1, dir2) :
    currentScore = curScore
    #print()
    #print(f'CurScore {currentScore} of {cnt}')
    #CHECK FOR TERMINAL NODE / LEAF
    #case when over the MAXDEPTH
    
    #pacwin 
    if isPacWin(curDot) :
        #print("PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !PACMAN WIN !VVV")
        return ( INF + score , [ 0,0 ] ) 
    #paclose
    if dir1 != -1 and isPacLose( node , dir1, dir2 ) :
        #print("PACMAN LOSE !")
        return ( -INF + score , [ 0,0 ] )

    if depth > MAXDEPTH :
        #print("REACH MAX DEPTH !")
        return ( currentScore , [ 0,0 ]   )
    

    if isMax :
        #pacman turn
        #print("MAXNODE - PACMAN TURN")
        #score , list position
        bestChoice = ( -1 , [ 0,0 ] )
        isEqual = True
        firstPic = 0

        startd = randrange(1000000)

        for sd in range(4) :

            d = (sd + startd)%4

            newPacPos = ( node.PP[0] + d4val[d][0] , node.PP[1] + d4val[d][1] ) 

            if( canMove( node.PP[0] , node.PP[1] , d ) ) :
                # print("pac canmove somw")

                (dotY,dotX) = reachCel( node.PP[0] , node.PP[1] , d )
                #print(f'Child of{cnt}')
                #print(f'Pacpos{node.PP}')
                #print(f'newPacpos{newPacPos}')
                # print(f'dot pos : {dotY} {dotX}')
                # print(mnmCurPoint[dotY][dotX])
                
                takenDot = 0

                if mnmCurPoint[dotY][dotX] == 2 :
                    #print("take!")
                    mnmCurPoint[dotY][dotX] = 0
                    takenDot = 1
                    curDot+=1

                
               
                newNode = Node(newPacPos,node.G1,node.G2 )

                optChoice = minimax(newNode, False,depth+1, currentScore + takenDot , alpha, beta , curDot , dir1,dir2)
                if d == 0 :
                    firstPic = optChoice[0]
                if d > 0 and optChoice[0] != firstPic :
                    isEqual = False

                if takenDot != 0 :
                    #print("recover!")
                    mnmCurPoint[dotY][dotX] = 2
                    curDot+=1


                if( bestChoice[0] == -1 or optChoice[0] > bestChoice[0]) : 
                    #bestChoice = ( optChoice[0], [newPacPos] )
                    bestChoice =( optChoice[0], [d])
                    alpha = max( alpha , bestChoice[0] )
                    if beta <= alpha :
                        #print("Prunning Alphabeta !!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        break
                
            
        
        
        #print(f"PAC best choice score {bestChoice[0]} of {cnt}")
        if isEqual :
            return ( bestChoice[0] , [-2,-2] )
        return bestChoice
                    

    else :
        #print("MIN NODE - GHOST TURN")

        bestChoice = ( INF , [-1,-1] )
        isEqual = True
        firstPic = 0
        startd = randrange(100000)
        for sig1 in range(4) :
            for sig2 in range(4) :
                ig1 = (startd + sig1)%4
                ig2 = (startd + sig2)%4
                newPosG1 = ( node.G1[0] + d4valG[ig1][0] , node.G1[1] + d4valG[ig1][1] )
                newPosG2 = ( node.G2[0] + d4valG[ig2][0] , node.G2[1] + d4valG[ig2][1] )
                if( canMove( node.G1[0] , node.G1[1] , ig1)  and canMove( node.G2[0]  , node.G2[1]  ,ig2) ) :

                    # print("ghost canmove somw")
                    # print(f'Ghost 1 Pos : {node.G1}')
                    # print(f'Ghost new 1 Pos : {newPosG1}')
                    # print(f'Ghost 2 Pos : {node.G2}')
                    # print(f'Ghost new 2 Pos : {newPosG2}')

                    newNode = Node( node.PP , newPosG1 , newPosG2 )
                    optChoice = minimax(newNode, True, depth+1, currentScore, alpha, beta , curDot , ig1 , ig2 )
                    if ig1 == 0 and ig2 == 0 :
                        firstPic = optChoice[0]
                    if ig1 != 0 or ig2 != 0 :
                       if  optChoice[0] != firstPic :
                           isEqual = False
                    if( optChoice[0] < bestChoice[0] ) : 
                        bestChoice = ( optChoice[0], [ig1,ig2] )
                        beta = min( beta , bestChoice[0] )
                        if beta <= alpha :
                            #print("Prunning Alphabeta !!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            break
        #print(f"ghost best choice score {bestChoice[0]} of {cnt}")
        if isEqual :
            # print("equal")
            # print(bestChoice[0])
            return ( bestChoice[0] , [-2,-2] )
        return bestChoice


    

MAXDEPTH = 6

def doGhostMoveByMiniMax(pacPos, G1 , G2):

    curNode = Node( pacPos , G1 , G2 )
    minchoice = minimax(curNode,False,0,0,-INF,INF,0,-1,-1)
    
    S1.newDir = minchoice[1][0]
    S2.newDir = minchoice[1][1]

    if minchoice[1][0] == -2  :
        print("is random move !")
        if step%15 == 0 :
            tmp = randomD()
            while(tmp == S1.newDir):
                tmp = randomD()
            S1.newDir = tmp
            tmp = randomD()
            while(tmp == S2.newDir):
                tmp = randomD()
            S2.newDir = tmp
    else :
        S1.newDir = minchoice[1][0]
        S2.newDir = minchoice[1][1]
        #print(minchoice[1][0])
        #print(minchoice[1][1])
        #print()


    # print(f'mnm: {S1.newDir} {S2.newDir} ')



step = 0 

def isTouch( a , b ) :
    if  a[0] == b[0] and abs( a[1]  - b[1] ) < 1.0 :
        return True 
    if  a[1] == b[1] and abs( a[0]  - b[0] ) < 1.0 :
        return True 
    return False

while not game_over:
    if numOfPoint == score:
        # show win announce
        messagebox.showinfo("WIN ANNOUNCEMENT","Ban. da~ thang'") 
        game_over = True
    else:
     for event in pygame.event.get():
        #print(f'{P.row} {P.col}')
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                P.newDir = 0
            elif event.key == pygame.K_d:
                P.newDir = 1
            elif event.key == pygame.K_s:
                P.newDir = 2
            elif event.key == pygame.K_a:
                P.newDir = 3
    

    if S1.row == P.row:
        if float(abs(P.col-S1.col))<1.0:
            messagebox.showinfo("LOSE ANNOUNCEMENT","Game Over!") 
            game_over = True
            continue
    if S2.row == P.row:
         if float(abs(P.col-S2.col))<1.0:
            messagebox.showinfo("LOSE ANNOUNCEMENT","Game Over!") 
            game_over = True
            continue
    if S2.col == P.col:
         if float(abs(P.row-S2.row))<1.0:
            messagebox.showinfo("LOSE ANNOUNCEMENT","Game Over!") 
            game_over = True
            continue
 
    if S1.col == P.col:
         if float(abs(P.row-S1.row))<1.0:
            messagebox.showinfo("LOSE ANNOUNCEMENT","Game Over!") 
            game_over = True
            continue
    showScore(5,5)

    S1.clearCurObjImage()
    S1.update()
    S1.drawCurObjImage()

    S2.clearCurObjImage()
    S2.update()
    S2.drawCurObjImage()

    P.clearCurObjImage()
    P.update()
    P.drawCurObjImage()  # draw Pacman
    
    # if step % 15 == 0 :
    #   doGhostMovRand()
    if isInt(P.row) and isInt(P.col) and isInt(S1.row) and isInt(S1.col) and isInt(S2.col) and isInt(S2.row) :
        print(f' {P.row} {P.col} {S1.row} {S1.col} {S2.row} {S1.col}')
        doGhostMoveByMiniMax( (P.row,P.col) , (S1.row,S1.col), (S2.row,S2.col))
        print()
        print()

    pygame.display.update()
    fpsClock.tick(fps)
    step += 1

