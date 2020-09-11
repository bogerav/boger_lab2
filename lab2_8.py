import turtle as t
import math as m
t.shape('turtle')

loops = 0              
n = 3                 
r = 15

def paint(n,L):
    a = (n - 2) * 180 / n 
    for i in range(n):
        t.right(180 - a)
        t.forward(L)
while loops < 10:
    L = 2 * r * m.sin(m.pi / n)   
    ang = ((n - 2) * 180/n) / 2 
    t.right(ang)                       
    paint(n, L)           
    t.left(ang)                     
    t.penup()
    t.forward(15)           
    t.pendown()
    r += 15             
    n += 1                    
    loops += 1    
t.exitonclick()
