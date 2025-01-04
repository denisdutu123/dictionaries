import pgzrun

WIDTH = 900
HEIGHT = 700

TITLE = "5 for 5"

mbox = Rect(0,0,900,100)
ques = Rect(0,100,700,150)
ans1 = Rect(0,0,300,100)
ans2 = Rect(0,0,300,100)
ans3 = Rect(0,0,300,100)
ans4 = Rect(0,0,300,100)
tim = Rect(700,100,200,150)
ski = Rect(700,250,225,450)
answe = [ans1, ans2, ans3, ans4]
def draw():
    screen.draw.filled_rect(mbox,"Blue")
    screen.draw.filled_rect(ques,"Red")
    screen.draw.filled_rect(tim,"Orange")
    screen.draw.filled_rect(ski,"Green")


def update():
    pass






pgzrun.go()