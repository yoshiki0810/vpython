#from turtle import circle
#from numpy import size
from vpython import *
from time import *

floor = box(pos=vector(0,-5,0), size =vector(10,.1,10),color=color.white)
ceiling = box(pos=vector(0,5,0),size = vector(10,.1,10),color=color.white)
backwall = box(pos=vector(0,0,-5),size = vector(10,10,.1),color=color.white)
rightwall = box(pos=vector(-5,0,0),size = vector(.1,10,10),color=color.white)
leftwall = box(pos=vector(5,0,0),size = vector(.1,10,10),color=color.white)
marble = sphere(radius =.75,color=color.red)

deltaX =.1
xPos =0

while True:
    rate(100)
    xPos += deltaX
    marble.pos = vector(xPos,0,0)

    if(xPos+.75 > 5 or xPos-.75 < -5):
        deltaX = -deltaX