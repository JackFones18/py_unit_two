import turtle





garden_size = input("how many feet would you like the side of your garden to be? ")
plant_size = input("how much space (in feet) should each flower occupy? ")
flowerbed_depth = input("what would you like the depth of the soil in the flowerbeds to be (in feet)? ")
fill_depth = input ("what would you like the depth of the fill to be (in feet)? ")

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
for x in range (4):
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
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
turtle.goto(220,0)
turtle.write(garden_size"feet),move=false, align="left", font=("arial",



print (garden_size)
print(plant_size)
print(flowerbed_depth)
print(fill_depth)

turtle.exitonclick()