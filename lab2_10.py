import turtle as t
t.shape('turtle')
x=50
t.lt(90)
for i in range (10):
    t.circle(x)
    t.circle(-x)
    x+=10
t.exitonclick()
