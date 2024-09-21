import pgzrun
import random

WIDTH = 1000
HEIGHT = 600
rick = Actor("rick grimes.png")
hitler = Actor("hitler.png")
rick.pos = 400,400
hitler.pos = 550,350
gov=False
scor = 0
def draw():
    screen.blit("prison.jpg",(0,0))
    rick.draw()
    hitler.draw()
    if gov:
        screen.fill("Red")
        screen.draw.text("Time Up,score:"+str(scor),center = (500,300),fontsize = 70)
def position():
    hitler.pos = random.randint(0,1000), random.randint(0,600)
def tim():
    global gov
    gov = True
def update():
    pass
    global scor
    if keyboard.left:
        rick.x-=6
    if keyboard.right:
        rick.x+=6
    if keyboard.up:
        rick.y-=6
    if keyboard.down:
        rick.y+=6
    if rick.colliderect(hitler):
        position()
        scor+=1
        

clock.schedule(tim,10)




pgzrun.go()
