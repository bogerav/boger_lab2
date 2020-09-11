import turtle as t
t.shape('turtle')

def paint(n, radius):
    for i in range (n):
        t.rt(360/n)
        t.fd(radius)

paint(100, 10)
t.exitonclick()
