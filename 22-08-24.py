import pgzrun
import random
WIDTH= 500
HEIGHT= 500
def draw():
    rad=200
    for i in range(15):
            
            re=random.randint(0,255)
            gre=random.randint(0,255)
            blu=random.randint(0,255)
            screen.draw.circle((250,215),rad,(re,gre,blu))
            rad-=5
pgzrun.go()