import turtle as t
t.shape('turtle')
n=5
k=11
def stars(n):
    t.rt(180 - (180 / n))
    t.fd(100)
for i in range (n):
    stars(n)
t.up()
t.goto(200, 0)
t.down()
for i in range (k):
    stars(k)
t.exitonclick()
