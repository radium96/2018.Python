import turtle

t = turtle.Turtle()
t.width(3)
t.shape("turtle")
t.shapesize(3.3)

while False:
    command = input("명령을 입력하시오 : ")
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
