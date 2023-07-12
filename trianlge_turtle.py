# import turtle
#
# t = turtle.Turtle()
# s = turtle.Screen()
#
# s.bgcolor("black")
#
# t.width(2)
# t.speed(20)
#
# col = ('white', 'pink', 'cyan')
#
# for i in range(300):
#     t.pencolor(col[i % 3])
#     t.forward(i*4)
#     t.right(121)

### moving circle ###

# import turtle
#
# # Create a turtle screen
# screen = turtle.Screen()
# screen.bgcolor("black")
#
# # Create a turtle object
# circle = turtle.Turtle()
# circle.shape("circle")
# circle.color("red")
# circle.speed(2)
#
# # Set the initial position of the circle
# circle.penup()
# circle.goto(0, -100)
# circle.pendown()
#
# # Define the circle's movement
# angle = 0
# speed = 2
#
# # Move the circle in a circular path
# while True:
#     circle.clear()
#     x = 100 * (speed * angle) / 360  # Adjust the radius and speed of the circle
#     y = 100 * (speed * angle) / 360
#     circle.goto(x, y)
#     angle += 1
#
#     # Reset the angle to keep it within 360 degrees
#     if angle >= 360:
#         angle = 0
#
# # Exit on click
# turtle.exitonclick()


import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
diamond = turtle.Turtle()
diamond.shape("turtle")
diamond.color("blue")
diamond.speed(2)

# Define the diamond's side length
side_length = 100

# Move the turtle to the starting position
diamond.penup()
diamond.goto(-side_length/2, side_length/2)
diamond.pendown()

# Define the diamond's rotation
angle = 0
rotation_speed = 2

# Rotate the diamond
while True:
    diamond.clear()
    diamond.setheading(angle)
    for _ in range(4):
        diamond.forward(side_length)
        diamond.right(90)
    angle += rotation_speed

    # Reset the angle to keep it within 360 degrees
    if angle >= 360:
        angle = 0

# Exit on click
turtle.exitonclick()
