import copy
import pygame as pygame
import math
from random import randrange
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
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],  # Middle Lane Row: 14
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
print(spriteOffset)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
game_over = False  # Biến đánh dấu sự kiện kết thúc game 


curPoint  = copy.deepcopy(originalGameBoard)

print(len(gameBoard[0]))
print(len(gameBoard))
for i in range(len(gameBoard) ) :
    for j in range(len(gameBoard[0]) ) :
        if gameBoard[i][j] != 2 :
            curPoint[i][j] = 0

for i in range(len(gameBoard) ) :
    for j in range(len(gameBoard[0]) ) :
        print(f'{curPoint[i][j] }', end='')
    print('')        


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

def canMove(row, col):
# if col == -1 or col == len(gameBoard[0]):
#     return True
    if gameBoard[int(row)][int(col)] != 3:
        return True
    return False


class MovableObj : # include pacman, ghost
    def __init__(self, row, col, imagePath, isPacMan, startingRow, startingCol ):
        self.imgPath = imagePath
        self.row = row
        self.col = col
        self.speed = 1 / 4 
        self.dir = 0  # 0: North, 1: East, 2: South, 3: West 0 là đi lên. 1 là sang phải 2 là xuống dưới 3 là sang trái
        self.newDir = 0
        self.isPacMan = isPacMan

    def startDraw() :
        p = pygame.image.load(src + imgPacClose)
        p = pygame.transform.scale(p, (square, square))
        screen.blit(p, (startingRow * square, startingCol * square, square, square))

    def update(self) :
        if self.newDir == 0:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
                self.dir = self.newDir
                # print(0)
                if self.isPacMan == 1 :
                    curPoint[ math.ceil(self.row) ][ int(self.col) ] = 0
                return
        elif self.newDir == 1:  # 26 , 13,5
            if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
                self.dir = self.newDir
                # print(1)
                if self.isPacMan == 1 :
                    curPoint[ int(self.row) ][ math.ceil(self.col) ] = 0
                return
        elif self.newDir == 2:
            if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
                self.dir = self.newDir
                # print(2)
                if self.isPacMan ==1 :
                    curPoint[ math.floor(self.row) ][int(self.col)] = 0
                return
        elif self.newDir == 3:
            if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed
                self.dir = self.newDir
                # print(3)
                if self.isPacMan ==1 :
                    curPoint[int(self.row)][ math.floor(self.col) ] = 0
                return
        #

        print("does it can happen ?") 

        if self.dir == 0:
            if canMove(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
                if self.isPacMan ==1 :
                    curPoint[ math.ceil(self.row) ][ int(self.col) ] = 0
            # print(0)
        
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
                if self.isPacMan ==1 :
                    curPoint[ int(self.row) ][ math.ceil(self.col) ] = 0
            # print(1)
        
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
                if self.isPacMan ==1 :
                    curPoint[ math.floor(self.row) ][int(self.col)] = 0
            # print(2)
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed
                if self.isPacMan ==1 :
                    curPoint[int(self.row)][ math.floor(self.col) ] = 0
            # print(3)

    def drawBlackRectangle(self, row, col) :  # draw image
        pygame.draw.rect(screen, (0, 0, 0) , (col * square, row * square, square, square))

    def drawBlackBoxAndDot(self, row, col) :
        print(row)
        print(col)
        if curPoint[row][col] == 2 :
            self.drawBlackRectangle(row, col)
            pygame.draw.circle(screen, pelletColor, (col * square + square // 2, row * square + square // 2),
                                square // 4)
        else :
            self.drawBlackRectangle(row, col)
            print("yes i'm printting black box")
            print(row,col)
    
    def clearCurObjImage(self):

        # only row or col can be float . other is not
        print(self.row)
        print(self.col)
        print(isInt( self.row ))

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
    def __init__(self, row, col,impPac,isPacMan,startingRow,startingCol) :
        MovableObj.__init__(self,row,col,imgPacClose,isPacMan, startingRow,startingCol ) 
    

class Blinky(MovableObj):
    def __init(self,row,col,blinky,isPacMan,startingRow,startingCol):
        MovableObj.__init__(self,row,col,blinky,isPacMan, startingRow,startingCol ) 


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

P = Pacman(26, 14,imgPacClose,1,14,26)

S1 = Blinky(16,14,blinky,0,14,16)

S2 = Blinky(18,14,cyanghost,0,14,18)



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

while not game_over:
    for event in pygame.event.get():
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

    S1.clearCurObjImage()
    S1.update()
    S1.drawCurObjImage()
    S2.clearCurObjImage()
    S2.update()
    S2.drawCurObjImage()

    P.clearCurObjImage()
    P.update()
    P.drawCurObjImage()  # draw Pacman

    if step % 15 == 0 :
      doGhostMovRand()

    pygame.display.update()
    fpsClock.tick(fps)
    step += 1
