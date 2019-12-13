import turtle
def dessin_carre(couleur, taille_carre,x,y):
    turtle.color(couleur)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.forward(taille_carre)
    turtle.left(90)
    turtle.forward(taille_carre)
    turtle.left(90)
    turtle.forward(taille_carre)
    turtle.left(90)
    turtle.forward(taille_carre)
    turtle.left(90)

def dessin_triangle(couleur, angle, taille, x, y):
    turtle.color(couleur)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(taille)  # draw base

    turtle.left(angle * 2)
    turtle.forward(taille)

    turtle.left(angle * 2)
    turtle.forward(taille)

    turtle.done()

dessin_carre("black", 80,0,0)
dessin_carre("red", 40,20,0)
dessin_triangle("green", 60, 80, 0, 80)