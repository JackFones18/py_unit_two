import turtle
turtle.speed(0)
turtle.hideturtle()

import math

pi=math.pi

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


def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def semicircle():
    turtle.begin_fill()
    turtle.circle(100,180)
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
turtle.write((garden_size,'feet'),move=False, align="left", font=("arial", 10, "bold"))


turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.begin_fill()
turtle.color("light blue")
turtle.circle(100)
turtle.end_fill()

move(100,-100)
semicircle()

move(-100,100)
semicircle()

move(100,100)
turtle.left(90)
semicircle()

move(-100,-100)
semicircle()
move(-100,100)


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

move(0,120)


diameter=(float(garden_size)/2)
turtle.write((diameter,"feet"),move=False,align="center",font=("arial",10,"bold"))

radius=(float(garden_size)/4)

circle_area=(pi*(radius**2))

total_flower_area=circle_area*3

circle_volume=round((float(circle_area)*float(flowerbed_depth)),2)
semicircle_volume=round((float(circle_volume)/2),2)
total_flowerbed_volume=(float(circle_volume)*3)

fill_area=((float(garden_size)**2)-float(total_flower_area))
fill_volume=round((float(fill_area)*float(fill_depth)),2)

circle_flowers=round((float(circle_area)/float(plant_size)))
semicircle_flowers=round((float(circle_area)/2)/float(plant_size))
total_amount_flowers=round((float(circle_flowers)*3))


print(".")
print(".")
print(".")
print(".")
print(".")

print("you will be able to fit", semicircle_flowers, "flowers in each semicircle.")
print("you will be able to fit",circle_flowers,"flowers in the center circle.")
print("you will be able to fit",total_amount_flowers,"flowers in the garden.")
print("the amount of soil required for each semicircle is:",semicircle_volume,"feet cubed")
print("the amount of soil required for the center circle is:",circle_volume,"feet cubed")
print("the total amount of fill needed is:", fill_volume,"feet cubed")

'''
print("the aera of the center circle is:",circle_area,"feet squared")
print("the total area occupied by the flowers is:",total_flower_area,"feet squared")
print("the amount of soil required for the center circle is:",circle_volume,"feet cubed")
print("the amount of soil required for each semicircle is:",semicircle_volume,"feet cubed")
print("the total amount of soil needed is:",total_flowerbed_volume,"feet cubed")
print("the area of the fill is:", fill_area,"feet squared")
print("the total volume of fill needed is:", fill_volume,"feet cubed")
print("you will be able to fit",circle_flowers,"in the center circle.")
print("you will be able to fit", semicircle_flowers, "in each semicircle.")
'''
turtle.exitonclick()