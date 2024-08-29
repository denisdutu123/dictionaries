import pgzrun
import random
WIDTH=500
HEIGHT=400
TITLE="Shoot Homelander"
mess="Welcome to Homelander shooter"
home=Actor("homelander.png")
def draw():
    screen.fill("Red")
    home.draw()
    screen.draw.text(mess,center=(250,40),fontsize=25)
def posi():
    home.x=random.randint(0,500)
    home.y=random.randint(0,400)
def on_mouse_down(pos):
    global mess
    if home.collidepoint(pos):
        posi()
        mess="Good aim"
    else:
        mess="Bad aim"

clock.schedule_interval(posi,1.5)












pgzrun.go()
