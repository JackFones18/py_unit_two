# Jack Fones
# 9-30-23
# This code does a few things. the first is calculating the amount of flowers, soil, and fill needed to create a
# flowerbed. The next is taking all of this information and outputting it to a turtle window where it makes it easy to
# read and visualize.

# The first step is importing both turtle and math, so we can draw and use the pi command.
import turtle
import math

# This line makes it easier to call pi later when we do calculations, so I can just type pi and not math.pi.
pi = math.pi


# This line makes it easier to move the pen. that way I can only type one line in the future instead of 3.
def move(x_coordinate, y):
    turtle.penup()
    turtle.goto(x_coordinate, y)
    turtle.pendown()


# These lines take user input, so it knows what values and colors to use for later calculations.
print("for each input of a value, please enter your desired value to 2 decimal places. (ex.11.00, 14.75)")
garden_size = input("how many feet would you like the side of your garden to be? ")
plant_size = input("how much space (in feet) should each flower occupy? ")
flowerbed_depth = input("what would you like the depth of the soil in the flowerbeds to be (in feet)? ")
fill_depth = input("what would you like the depth of the fill to be (in feet)? ")
print("")
print("color options include, but are not limited to: yellow, gold, orange, red, maroon, violet, magenta, purple,")
print("navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white")
fill_color = input("what color would you like the fill to be? ")
flower_color = input("what color would you like the flowers to be? ")

# This is to make the turtle go very fast and hides the cursor.
turtle.speed(0)
turtle.hideturtle()

# Moves the turtle.
move(-200, -200)

# This line takes the user input from earlier and makes a square filled with the user's chosen color.
turtle.color(fill_color)
turtle.begin_fill()
for x in range(4):
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()


# This makes it much easier to create semicircles in the future
def semicircle():
    turtle.begin_fill()
    turtle.circle(100, 180)
    turtle.end_fill()


move(200, -200)

# These lines make the black line on the side of the square that indicates the size. It also writes the size of the
# square using the users input from earlier.
turtle.color("black")
turtle.pensize(5)
turtle.forward(30)
turtle.back(15)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(15)
turtle.left(180)
turtle.forward(30)
turtle.penup()
turtle.goto(220, 0)
turtle.write((garden_size, 'feet'), move=False, align="left", font=("arial", 10, "bold"))

move(0, -100)

# This line makes the center circle in the user's chosen color.
turtle.begin_fill()
turtle.color(flower_color)
turtle.circle(100)
turtle.end_fill()

# Moves and creates the first semicircle
move(100, -100)
semicircle()

# Moves and creates the second semicircle
move(-100, 100)
semicircle()

# Moves and creates the third semicircle
move(100, 100)
turtle.left(90)
semicircle()

# Moves and creates the fourth semicircle
move(-100, -100)
semicircle()
move(-100, 100)

# These lines create the other line that indicates the diameter of all the circles.
turtle.color("black")
turtle.pensize(5)
turtle.forward(20)
turtle.left(180)
turtle.forward(10)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(10)
turtle.left(180)
turtle.forward(20)

# Moves and writes the size of the diameter. it finds this by taking the size of the garden and dividing it by 2.
move(0, 85)
diameter = (float(garden_size) / 2)
turtle.write((diameter, "feet"), move=False, align="center", font=("arial", 10, "bold"))

# The next 10 lines all do math to find the thing indicated by the name of the function (ex. radius)
radius = (float(garden_size) / 4)
circle_area = (pi * (radius ** 2))
total_flower_area = circle_area * 3
circle_volume = round((float(circle_area) * float(flowerbed_depth)), 2)
semicircle_volume = round((float(circle_volume) / 2), 2)
total_flowerbed_volume = (float(circle_volume) * 3)
fill_area = ((float(garden_size) ** 2) - float(total_flower_area))
fill_volume = round((float(fill_area) * float(fill_depth)), 2)
circle_flowers = round((float(circle_area) // float(plant_size)))
semicircle_flowers = round((float(circle_area) / 2) // float(plant_size))
total_amount_flowers = round((float(circle_flowers) * 3))

# Writes the amount of flowers that will fit in the center
move(0, 0)
turtle.write((circle_flowers, "flowers will fit here"), move=False, align="center", font=("arial", 10, "bold"))

# Writes the amount of flowers that will fit in the top and bottom semicircles. I wanted to write it on the sides but
# you cant write sideways text in turtle.
move(0, -140)
turtle.write((semicircle_flowers, "flowers will fit here"), move=False, align="center", font=("arial", 10, "bold"))
move(0, 145)
turtle.write((semicircle_flowers, "flowers will fit here"), move=False, align="center", font=("arial", 10, "bold"))

# Prints a bunch of blank lines, so it's easier to read what the code is outputting
print("")
print("")
print("")

# Prints all the requirements that were found through the math functions
print("REQUIREMENTS")
print("")
print("you will be able to fit", semicircle_flowers, "flowers in each semicircle.")
print("")
print("you will be able to fit", circle_flowers, "flowers in the center circle.")
print("")
print("you will be able to fit", total_amount_flowers, "flowers in the garden.")
print("")
print("the amount of soil required for each semicircle is:", semicircle_volume, "feet cubed")
print("")
print("the amount of soil required for the center circle is:", circle_volume, "feet cubed")
print("")
print("the total amount of soil required for the garden is:", total_flowerbed_volume, "feet cubed")
print("")
print("the total amount of fill needed is:", fill_volume, "feet cubed")

# All of these lines make the same thing that was printed to the console get printed to the turtle window.
move(-200, -215)
turtle.write("REQUIREMENTS:", move=False, align="left", font=("arial", 10, "bold"))
move(-200, -230)
turtle.write(("you will be able to fit", semicircle_flowers, "flowers in each semicircle."), move=False, align="left",
             font=("arial", 10, "bold"))
move(-200, -245)
turtle.write(("you will be able to fit", circle_flowers, "flowers in the center circle."), move=False, align="left",
             font=("arial", 10, "bold"))
move(-200, -260)
turtle.write(("you will be able to fit", total_amount_flowers, "flowers in the garden."), move=False, align="left",
             font=("arial", 10, "bold"))
move(-200, -275)
turtle.write(("the amount of soil required for each semicircle is:", semicircle_volume, "feet cubed"), move=False,
             align="left", font=("arial", 10, "bold"))
move(-200, -290)
turtle.write(("the amount of soil required for the center circle is:", circle_volume, "feet cubed"), move=False,
             align="left", font=("arial", 10, "bold"))
move(-200, -305)
turtle.write(("the total amount of soil required for the garden is:", total_flowerbed_volume, "feet cubed"), move=False,
             align="left", font=("arial", 10, "bold"))
move(-200, -320)
turtle.write(("the total amount of fill needed is:", fill_volume, "feet cubed"), move=False, align="left",
             font=("arial", 10, "bold"))

turtle.exitonclick()
