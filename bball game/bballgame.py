import pgzrun
import random
import time

WIDTH = 1200
HEIGHT = 658

# variables
bal = []
lin = []
num = 10
sat = 0
nball = 0
end = 0
total = 0

#function for positioning for ball

def position():
    global sat
    for i in range(num):
        ba = Actor("ball.png")
        ba.pos = random.randint(0,900), random.randint(0,500)
        bal.append(ba)
    sat = time.time()

def draw():
    screen.blit("court.jpg",(0,0))
    coun = 1
    for v in bal:
        v.draw()
        screen.draw.text(str(coun),(v.pos[0],v.pos[1]+25))
        coun+=1
    
    if nball < num:
        total = time.time() - sat
        screen.draw.text(str(round(total,1)),(850,25),fontsize = 25)
    else:
         screen.draw.text(str(total),(850,25),fontsize = 25)

def update():
    pass
def on_mouse_down(pos):
    global nball, lin
    if nball < num:
        if bal[nball].collidepoint(pos):
            if nball:
                lin.apend((bal[nball-1].pos, bal[nball].pos))
            nball = nball + 1
position()














pgzrun.go()
