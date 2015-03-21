import turtle
import math

def DrawFlag(a):
    w = turtle.Screen()
    t = turtle.Turtle()

    A = a
    B = a * 1.9
    C = A * 7 / 13
    D = B * 2 / 5
    E = F = C / 10
    G = H = D / 12
    L = A / 13
    K = L * 4 / 5
    
    w.setworldcoordinates(0, 0, B * 2, A * 2)

    t.ht()
    t.degrees()
    t.speed(200)
    
    t.setheading(0)
    t.penup()
    t.goto(0, A)
    
    DrawRectangle(A, B, "black", t)

    t.setheading(0)
    t.penup()
    t.goto(0, A)
    t.fillcolor(0, 0, 1) #blue
    t.begin_fill()
    DrawRectangle(C, D, "black", t)
    t.end_fill()

    for i in range(7):
        t.setheading(0)
        t.penup()
        t.goto(D, A - (i * L))
        c = "red"
        if i % 2 != 0:
            c = "white"
            
        r, g, b = GetColor(c)
        t.fillcolor(r, g, b)
        t.begin_fill()
        DrawRectangle(L, B - D, "black", t)
        t.end_fill()

    for i in range(6):
        t.setheading(0)
        t.penup()
        t.goto(0, A - C - (i * L))
        c = "red"
        if i % 2 == 0:
            c = "white"

        r, g, b = GetColor(c)
        t.fillcolor(r, g, b)
        t.begin_fill()
        DrawRectangle(L, B, "black", t)
        t.end_fill()

    for i in range(9):
        if i % 2 == 0:
            t.setheading(18)
            t.penup()
            t.goto(G, A - E - (i * E))

            for j in range(6):
                t.goto(G + (j * 2 * G), A - E - (i * E))
                t.pendown()
                r, g, b = GetColor("white")
                t.fillcolor(r, g, b)
                t.pencolor(r, g, b)
                t.begin_fill()
                DrawStar(t, K /2 * 1.17)
                t.penup()
                t.end_fill()

        if i % 2 != 0:
            t.setheading(18)
            t.penup()
            t.goto(2 * G, A - (2 * E) - ((i - 1) * E))

            for j in range(5):
                t.goto((2 * G) + (j * 2 * G), A - (2 * E) - ((i - 1) * E))
                t.pendown()
                r, g, b = GetColor("white")
                t.fillcolor(r, g, b)
                t.pencolor(r, g, b)
                t.begin_fill()
                DrawStar(t, K /2 * 1.17)
                t.penup()
                t.end_fill()
'''
    t.setheading(18)
    t.penup()
    t.goto(G, A - E)
    t.fillcolor(1, 1, 1)
    t.begin_fill()
    DrawStar(t, K / 2 * 1.17)
    t.end_fill()
    '''

def DrawRectangle(h, l, c, t):
    
    r, g, b = GetColor(c)
    t.pencolor(r, g, b)
    t.pendown()
    t.forward(h)
    #print(t.position())
    t.left(90)
    t.forward(l)
    #print(t.position())
    t.left(90)
    t.forward(h)
    #print(t.position())
    t.left(90)
    t.forward(l)
    #print(t.position())
    
    return

def GetColor(c):
    if c == "black":
        return 0, 0, 0
    if c == "red":
        return 1, 0, 0
    if c == "white":
        return 1, 1, 1
    if c == "blue":
        return 0, 0, 1

def DrawStar(t, d):
    for i in range(5):
        t.forward(d)
        t.right(144)
        t.forward(d)

DrawFlag(10)
