import turtle as t
import math
t.shape('turtle')

rad=0.1
degr=rad*(180/math.pi)
for i in range (100):
    ro=rad
    t.forward(ro/5)
    t.left(degr)
    rad+=0.1
    ro+=ro
t.exitonclick()
