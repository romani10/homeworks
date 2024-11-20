from turtle import *


#we want to paint a house

#step 1:  draw a square
# shape("turtle")
speed(30)
width(5)
color("purple")
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)




#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(60)
right(90) 
forward(100)
end_fill()

#roof

penup()
goto(200, 200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window

left(30)
color("green")
penup()
forward(80)
pendown()
left(90)
forward(80)
left(90)
forward(80)
penup()
left(90)
forward(40)
left(90)
pendown()
forward(80)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(80)
penup()
right(90)
forward(40)
right(90)
forward(130)
pendown()
right(90)
forward(80)
left(90)
forward(70)
left(90)
penup()
forward(80)
left(90)
forward(30)
left(90)
pendown()
forward(80)
left(90)
forward(30)
left(90)
penup()
forward(40)
left(90)
pendown()
forward(70)












exitonclick()








