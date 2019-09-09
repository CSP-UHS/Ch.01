'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
bb8=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
bb8.speed(15)
bb8.pensize(1.5)
bb8.color('white')
bb8.penup()
bb8.setpos(0,-150)
bb8.pendown()
bb8.begin_fill()
bb8.circle(100)
bb8.end_fill()
bb8.penup()
bb8.setpos(100,50)
bb8.pendown()
bb8.begin_fill()
bb8.left(90)
bb8.circle(100,180)
bb8.left(90)
bb8.forward(200)
bb8.end_fill()
bb8.color('gray')
bb8.begin_fill()
bb8.right(135)
bb8.forward(30)
bb8.right(45)
bb8.penup()
bb8.setpos(-100,50)
bb8.left(135)
bb8.pendown()
bb8.forward(30)
bb8.left(45)
bb8.forward(160)
bb8.penup()
bb8.setpos(-100,50)
bb8.pendown()
bb8.forward(200)
bb8.end_fill()
bb8.color('black')
bb8.backward(200)
bb8.penup()
bb8.setpos(5,90)
bb8.left(20)
bb8.begin_fill()
bb8.pendown()
bb8.circle(20)
bb8.end_fill()
bb8.penup()
bb8.setpos(0,63)
bb8.pendown()
bb8.circle(6)
bb8.penup()
bb8.setpos(1,59)
bb8.pendown()
bb8.circle(10)
bb8.penup()
bb8.setpos(50,70)
bb8.pendown()
bb8.begin_fill()
bb8.circle(10)
bb8.end_fill()
bb8.penup()
bb8.color('gray')
bb8.setpos(5,150)
bb8.left(70)
bb8.pendown()
bb8.forward(40)
bb8.penup()
bb8.setpos(-5,150)
bb8.pendown()
bb8.forward(30)
bb8.penup()
bb8.color('orange')
bb8.setpos(-90,50)
bb8.pendown()
bb8.begin_fill()
bb8.forward(10)
bb8.right(90)
bb8.forward(50)
bb8.right(90)
bb8.forward(10)
bb8.right(90)
bb8.forward(50)
bb8.end_fill()
bb8.penup()
bb8.setpos(90,50)
bb8.pendown()
bb8.begin_fill()
bb8.forward(20)
bb8.right(90)
bb8.forward(10)
bb8.right(90)
bb8.forward(20)
bb8.right(90)
bb8.forward(10)
bb8.end_fill()
bb8.penup()
bb8.setpos(-50,-20)
bb8.pendown()
bb8.right(30)
bb8.circle(60)
bb8.penup()
bb8.setpos(150,-150)
bb8.pendown()
bb8.write('Cal Watson',font=("Arial", 12, "normal"))

turtle.exitonclick() #Keeps pycharm window open
