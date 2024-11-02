import pgzrun
import random


WIDTH=1100
HEIGHT=700

#game variables
lev = 10
sta = 15
ove = False
cur = 1
fin = False
it = ["bag.png","bottle.png","controller.png","tin.png"]
items = []
def draw():
    screen.clear()
    screen.blit("park.jpg",(0,0))

def update():
    pass
def over():
    global ove
    ove = True
def total(extra):
    ite = []
    options = ["cardboard.png"] + random.choice(it,k = extra)
    random.shuffle(options)
    for i in options:
        item = Actor(i)
        ite.append(item)
    siz = WIDTH/(len(ite)+1)






pgzrun.go()