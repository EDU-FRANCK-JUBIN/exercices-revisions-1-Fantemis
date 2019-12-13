import turtle
turtle.left(90)
turtle.speed(25)
def dessin_triangle (angle_triangle, couleur, angle, taille, x, y):
    turtle.color(couleur)
    turtle.up()
    turtle.goto(x, y)
    turtle.left(angle_triangle)
    turtle.down()
    turtle.forward(taille)  # draw base

    turtle.left(angle)
    turtle.forward(taille)

    turtle.left(angle)
    turtle.forward(taille)
def dessiner_velo():
    for x in range(6):
        dessin_triangle(60, "yellow", 120, 30, 10, 10)
    for x in range(6):
        dessin_triangle(60, "yellow", 120, 30, 130, 10)

    dessin_triangle(30, "orange", 120, 60, 130, 10)
    dessin_triangle(60, "orange", 120, 60, 70, 10)

    turtle.left(180)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)

    turtle.color("red")
    turtle.left(180)
    turtle.forward(60)
    turtle.right(35)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(155)
    turtle.forward(60)
    turtle.left(35)
    turtle.forward(30)
    turtle.left(150)
    turtle.forward(25)


dessiner_velo()
