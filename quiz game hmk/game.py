import pgzrun

WIDTH = 900
HEIGHT = 700

TITLE = "5 for 5"
ti = 10
sc = 0
qu = "text.txt"
ove = False
counter = 0
question_i = 0
questions = []
marq = ""
mbox = Rect(0,0,900,100)
ques = Rect(0,100,700,150)
ans1 = Rect(20,250,300,200)
ans2 = Rect(375,250,300,200)
ans3 = Rect(20,500,300,200)
ans4 = Rect(375,500,300,200)
tim = Rect(700,100,200,150)
ski = Rect(700,250,225,450)
answe = [ans1, ans2, ans3, ans4]
def draw():
    screen.draw.filled_rect(mbox,"Blue")
    screen.draw.filled_rect(ques,"Red")
    screen.draw.filled_rect(tim,"Orange")
    screen.draw.filled_rect(ski,"Green")
    ind = 1
    for i in answe:
        screen.draw.filled_rect(i,"yellow")
    marq = "Welcome to 5 for 5"
    screen.draw.textbox(marq, mbox, color = "White")
    screen.draw.textbox(str (ti), tim, color = "Purple")
    screen.draw.textbox("SKIP", ski, color = "Red", angle = -90)
    screen.draw.textbox(question[0].strip(), ques, color = "Black")
    for i in answe:
        screen.draw.textbox(question[ind].strip(), i, color = "White")
        ind+=1


def marqee():
    mbox.x-=5
    if mbox.right < 0:
        mbox.left = 900
def update():
    pass
   
    marqee()
def read():
    global counter, questions
    tex = open(qu, "r")
    for i in tex:
        questions.append(i)
        counter+=1
    tex.close()
def next():
    global question_i
    question_i+=1
    return questions.pop(0).split(",")
def ov():
    global  question, ti, sc, ove
    marq = f"Gamer Over\n Your score is:{sc}"
    question = [marq, "-", "-", "-","-","-",5]
    ti = 0
    ove = True
def timi():
    global ti
    if ti > 0:
        ti-=1
    else:
        ov()
def answ():
    global sc, ti, question, questions
    sc+=1
    if questions:
        question = next()
        ti = 10
    else:
        ov()
def sk():
    global question, questions, ti
    if questions and not ove:
        question = next()
        ti = 10
    else:
        ov()
def on_mouse_down(pos):
    coun = 1
    for i in answe:
        if i.collidepoint(pos):
            if coun == int(question[5]):
                answ()
            else:
                ov()
        coun+=1
    if ski.collidepoint(pos):
        sk()







read()
question = next()
clock.schedule_interval(timi, 1)




pgzrun.go()
