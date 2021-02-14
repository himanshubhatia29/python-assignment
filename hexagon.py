# import the turtle modules
import turtle

# Start a work Screen
ws = turtle.Screen()

# Define a Turtle Instance
geekyTurtle = turtle.Turtle()
# executing loop 6 times for 6 sides
geekyTurtle.circle(-25)
turtle.forward(50)
turtle.left(-90)
turtle.forward(50)
turtle.left(-90)
turtle.forward(50)
turtle.left(-90)
turtle.forward(50)
turtle.left(-60)
for i in range(6):

	# Move forward by 90 units
	geekyTurtle.forward(90)
	# Turn left the turtle by 300 degrees
	geekyTurtle.left(300)
   
    
