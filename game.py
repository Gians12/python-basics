import pygame as pg
#init width height
width=800
height=720
fps=30
#floors
floor1=493
floor2=392
floor3=366
floor4=223
#initialize game
pg.init()
#create Clock
clock = pg.time.Clock()
#init display
gameDisplay = pg.display.set_mode((width,height))
pg.display.set_caption('Swordsman of DOOM')
pg.mouse.set_visible(False)
#bg icon
bg=pg.image.load("bg.jpg")
gameDisplay.blit(bg, (0, 0))
#init char
char=pg.image.load("ds2.png")
def chr(x,y):
    gameDisplay.blit(char,(x,y))
enemy=pg.image.load('mage.png')
def atk(key):
    if key==pg.K_1:
        char=pg.image.load('ds2.png')

#initialize gravit
gravity=10
sc=1.1
#char default placement
cx=0
cy=0
x=30
y=floor1
#bool var for Exit
Exit=False
def moveSide(keys,cx):
    if keys[pg.K_a]:
        if x<=0:
            cx=0
        else:
            cx=-6.3
    if keys[pg.K_d]:
        if x>=width-50:
            cx=0
        else:
            cx=6.3
    if event.type==pg.KEYUP :

        if event.key==pg.K_a:
            cx=0
        elif event.key==pg.K_d:
            cx=0
    return cx
#Jump method
jumpcnt=10
isJump=False
#gameloop
while not Exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Exit=True
        if event.type == pg.MOUSEBUTTONDOWN:
            print x,y

    keys=pg.key.get_pressed()
    #y=Jump(keys,y,jumpcnt)
    if keys[pg.K_1]:
        char=pg.image.load('atk.png')
    if event.type == pg.KEYUP:
        atk(event.key)
    if keys[pg.K_w] or keys[pg.K_SPACE] :
        isJump=True
    if(isJump):
        if jumpcnt>=-10:
            neq=1
            if jumpcnt<0:
                neq=-1
            y-=(jumpcnt**2)*0.5*neq
            jumpcnt-=1
        elif jumpcnt=-11:
            jumpcnt=10
            isJump=False
    #return y
    cx=moveSide(keys,cx)




    if x>=300 and x<=563:
        if y>floor4-50:#223
            gravity=0

    elif x>=48 and x<=308:
        if y<floor3-52:#366
            y+=0

    elif x>=483 and x<=733:
        if y>floor2-50:#393
            gravity=0

    if x>=-69 and x<=width:
        if y>=floor1:#493
            gravity=0


    x+=cx
    y+=gravity

    gameDisplay.blit(enemy,(x,floor1))
    gameDisplay.blit(bg,(0,0))
    chr(x,y)

    pg.display.flip()
    clock.tick(fps)

pg.quit()
quit()
