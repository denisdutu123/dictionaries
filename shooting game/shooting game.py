import pgzrun
import random

WIDTH = 1000
HEIGHT = 650

shooter = Actor("shooter.png")
enemy = Actor("enemy.png")
shooter.pos = 500,575
def draw():
    screen.blit("background.webp",(0,0))
    shooter.draw()
    enemy.draw()



def update():
    pass
    #key movements
    if keyboard.left:
        shooter.x-=5
        if shooter.x<0:
            shooter.x = 0
    if keyboard.right:
        shooter.x+=5
        if shooter.x>1000:
            shooter.x = 1000  


















pgzrun.go()