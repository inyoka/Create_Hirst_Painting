import colorgram
from turtle import Turtle, Screen, colormode
from random import shuffle


def print_colours(colors):
  for color in colors:
    rgb = color.rgb
    hsl = color.hsl
    proportion = color.proportion
    print(rgb, hsl, proportion)


if __name__ == '__main__':
  colormode(255)
  SIZE = 20
  SPACE = 40
  colors = colorgram.extract('hirst.jpg', SIZE)

  tim = Turtle()
  tim.width(15)
  lines = range(SIZE)
  tim.speed(10)
  current_line = SPACE
  
  for line in lines:
    shuffle(colors)
    for color in colors:
      rgb = color.rgb
      print(rgb)
      tim.down()
      tim.color(rgb)
      tim.forward(1)
      tim.up()
      tim.forward(SPACE)
    tim.sety(current_line)
    current_line += SPACE
    tim.setx(0)


  screen = Screen()
  screen.exitonclick()
