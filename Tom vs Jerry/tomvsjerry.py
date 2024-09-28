import pgzrun
import random

WIDTH = 1000
HEIGHT = 650
tom = Actor("tom.png")
jerry = Actor("jerry.png")
tom.pos = 500,325
jerry.pos = 600,275
scor = 0

def draw():
    screen.blit("ground.jpg",(0,0))
    tom.draw()
    jerry.draw()


def position():
        jerry.pos = random.randint(0,1000), random.randint(0,600)


def update():
      global scor
      if keyboard.left:
          tom.x-=7
      if keyboard.right:
          tom.x+=7
      if keyboard.up:
          tom.y-=7
      if keyboard.down:
          tom.y+=7
      if tom.colliderect(jerry):
           position()
      



pgzrun.go()