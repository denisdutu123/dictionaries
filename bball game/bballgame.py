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
end = 0
total = 0

#function for positioning for ball

def position():
    global sat
    for i in range(num):
        ba = Actor("ball.png")
        ba.pos = random.randint(0,1200), random.randint(0,658)
        bal.append(ba)

def draw():
    for v in bal:
        v.draw()

position()













pgzrun.go()