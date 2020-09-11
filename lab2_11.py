import turtle as t
t.shape('turtle')
x=50
t.lt(90)
for i in range (10):
    t.circle(-x, 360-180, 50)
    t.circle(-x/5, 180, 50)
t.exitonclick()
