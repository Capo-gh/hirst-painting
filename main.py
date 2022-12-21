import random
import colorgram
import turtle

colors = colorgram.extract("image.jpg", 30)
turtle.colormode(255)
rgb_colors = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202), (61, 233, 241), (5, 67, 42)]

timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)







screen = turtle.Screen()
screen.exitonclick()