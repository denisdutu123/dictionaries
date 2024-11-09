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
    if ove:
        screen.draw.text("Game Over", center = (550,350),fontsize = 60,color = "Red" )
    elif fin:
        screen.draw.text("You Won", center = (550,350),fontsize = 60,color = "Green" )
    else:

        for item in items:
            item.draw()

def update():
    pass
    global items, cur
    if len(items) == 0:
        items = total(cur)
def over():
    global ove
    ove = True
def total(extra):
    ite = []
    k = min(extra,len(it))
    options = ["cardboard.png"] + random.sample(it,k = k)
    random.shuffle(options)
    for i in options:
        item = Actor(i)
        ite.append(item)
    siz = WIDTH/(len(ite)+1)
    for index, item in enumerate(ite):
        item.x = (index+1)*siz
        item.y = 0
        animate(item,duration = sta - cur,y=HEIGHT)
    return ite 
def on_mouse_down(pos):
    global items, cur, fin
    for item in items:
        if item.collidepoint(pos):
            if "cardboard.png" in item.image:
                if cur == lev:
                    fin = True
                else:
                    cur+=1
                    items.clear()
            else:
                over()
                
    




pgzrun.go()
