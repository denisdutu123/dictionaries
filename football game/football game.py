import pgzrun
import random

WIDTH = 1100
HEIGHT = 700

lev = 10
sta = 15
ove = False
cur = 1
fin = False
tea = ["barcelona.png","bayern.png","manu.png","milan.png",]
teams = []
def draw():
    screen.clear()
    screen.blit("pitch.jpg",(0,0))
    if ove:
        screen.draw.text("You Lost", center = (550,350),fontsize = 60, color = "Blue")
    elif fin:
         screen.draw.text("You Won", center = (550,350),fontsize = 60, color = "Blue")
    else:

        for team in teams:
            team.draw()

def update():
    pass
    global teams, cur
    if len(teams) == 0:
        teams = total(cur)
def over():
    global ove
    ove = True
def total(extra):
    te = []
    k = min(extra,len(tea))
    options = ["realmadrid.png"] +random.sample(tea,k = k)
    random.shuffle(options)
    for i in options:
        team = Actor(i)
        te.append(team)
    siz = WIDTH/(len(te)+1)
    for index, team in enumerate(te):
        team.x = (index+1)*siz
        team.y = 0
        animate(team,duration = sta - cur,y=HEIGHT)
    return te
def on_mouse_down(pos):
    global team,cur, fin
    for team in teams:
        if team.collidepoint(pos):
            if"realmadrid.png" in team.image:
                if cur == lev:
                    fin = True
                else:
                    cur+=1
                    teams.clear()
            else:
                over()


pgzrun.go()
    
        
        







