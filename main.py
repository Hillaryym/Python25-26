from myFunctions import *

turtle.tracer(0)
turtle.colormode(255)
bob.pensize(3)
turtle.bgcolor("black")

#flower

#petals1
for times in range( 256 ):
  c = ( 255, times, 255 - times )
  bob.color("black", c)
  polygon(3, 120, c )
  bob.forward(times)
  bob.left(320)

bob.home()

#petals on top
for times in range( 256 ):
  c = ( times, 255, 255 - times )
  polygon(3, 120, c )
  bob.forward(times)
  bob.left(300)
