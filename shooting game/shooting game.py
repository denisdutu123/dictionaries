import pgzrun
import random

WIDTH = 1000
HEIGHT = 650

shooter = Actor("shooter.png")
enemy = Actor("enemy.png")
shooter.pos = 500,575
ene = []
bul = []
ene.append(Actor("enemy.png"))
ene[-1].x = 50
ene[-1].y = -10
score = 0
def on_key_down(key):
    if key == keys.SPACE:
       bul.append(Actor("bullets.png"))
       bul[-1].y = shooter.y - 65
       bul[-1].x = shooter.x - 40
def draw():
    screen.blit("background.webp",(0,0))
    shooter.draw()
    for i in ene:
      i.draw()
    for o in bul:
      o.draw()




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
    for i in ene:
        i.y+=3
        if i.y > 650:
            i.y = -10
            i.x = random.randint (0,1000)
    for v in bul:
        v.y -= 10


















pgzrun.go()
