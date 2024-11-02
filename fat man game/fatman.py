import pgzrun
import random
import time
import pygame

WIDTH = 1000
HEIGHT = 750 

man = []
lin = []
num = 10
sat = 0
nfat = 0
end = 0
total = 0


def position():
    global sat
    for i in range(num):
        fa = Actor("fat man.png")
        fa.pos = random.randint(100,900), random.randint(100,500)
        man.append(fa)
    sat = time.time()

def draw():
    global total
    screen.blit("macdonalds.png",(0,0))
    coun = 1
    for v in man:
        v.draw()
        screen.draw.text(str(coun),(v.pos[0],v.pos[1]+25))
        coun+=1
    for i in lin:
        pygame.draw.line(screen.surface,(127,206,99),i[0],i[1],5)
    
    if nfat < num:
        total = time.time() - sat
        screen.draw.text(str(round(total,1)),(850,25),fontsize = 25)
    else:
         screen.draw.text(str(round(total)),(850,25),fontsize = 25)

def update():
    pass
def on_mouse_down(pos):
    global nfat, lin
    if nfat < num:
        if man[nfat].collidepoint(pos):
            if nfat:
                lin.append((man[nfat-1].pos, man[nfat].pos))
            nfat = nfat + 1
        else:
            lin = []
            nfat = 0
position()














pgzrun.go()