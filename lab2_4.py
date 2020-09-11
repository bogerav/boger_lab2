import turtle as t
t.shape('turtle')

size = 0
while  10:
    size = size +1
    if size > 10:
        break
    t.fd(60 + size*20)
    t.left(90)
    t.fd(60 + size*20)
    t.left(90)
    t.fd(60 + size*20)
    t.lt(90)
    t.fd(60 + size*20)
    t.lt(90)
    t.penup()
    t.goto(-size*10,-size*10)
    t.pendown()
t.exitonclick()
