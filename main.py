###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t

#timmy = t.Turtle()
import random
t.colormode(255)
#
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_colors.append((r,g,b))
#
print(rgb_colors)

def make_dots():
    for i in range (0,10):
        t.dot(10,rgb_colors[random.randint(0,29)])
        t.penup()
        t.forward(20)


for i in range (0,200,20):
    t.goto(0, i)
    t.pendown()
    make_dots()


t.exitonclick()



