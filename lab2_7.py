import turtle as t
t.shape('turtle')
x=50
for i in range (10):
    for i in range (4):
        x+=10
        t.fd(x)
        t.lt(90)
t.exitonclick()
