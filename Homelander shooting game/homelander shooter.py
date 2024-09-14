import pgzrun
import random
WIDTH=500
HEIGHT=400
TITLE="Shoot Homelander"
mess="Welcome to Homelander shooter"
home=Actor("homelander.png")
scor=0
clicks=0
mis=0
perc=0
def draw():
    screen.fill("Red")
    home.draw()
    r=Rect((0,350),(500,60))
    screen.draw.filled_rect(r,(87,201,111))
    screen.draw.text(mess,center=(250,40),fontsize=25)
    screen.draw.text("Score-"+str(scor),topleft=(0,360),fontsize=30)
    screen.draw.text("Misses-"+str(mis),center=(150,370),fontsize=30)
    screen.draw.text("Percentage"+str(perc),topright=(300,380),fontsize=30)
def posi():
    home.x=random.randint(0,500)
    home.y=random.randint(0,400)
def on_mouse_down(pos):
    global scor,clicks,mis,perc
    clicks += 1
    global mess
    if home.collidepoint(pos):
        posi()
        mess="Good aim"
        scor += 1
        perc=(scor/clicks)*100
    else:
        mess="Bad aim"
        mis += 1


clock.schedule_interval(posi,1.5)

pgzrun.go()
