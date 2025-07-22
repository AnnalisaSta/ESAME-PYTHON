#
# File: ESERCIZIO_1.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 1
#
#COMPLETO

import turtle

def make_window(bkg_color, title):
    """Crea una finestra con background e titolo e ritorna la nuova finestra"""
    new_window = turtle.Screen()
    new_window.bgcolor(bkg_color)
    return new_window

def make_turtle(pen_color, pen_size):
    """Crea una nuova tartaruga dato un colore e dimensione del tratto e ritorna la nuova tartaruga"""
    new_turtle = turtle.Turtle()
    new_turtle.color(pen_color)
    new_turtle.pensize(pen_size)
    return new_turtle

#richiesta 1: funzione per disengare due triangoli
def draw_triangle3(tartaruga, width):
    """ ' tartaruga' disegna tre triangoli"""
    for i in range(2):
      for i in range(3):
          tartaruga.forward(width)
          tartaruga.left(120)
      tartaruga.penup()
      tartaruga.goto(width, 0)
      tartaruga.pendown()

#funzione per disegnare un solo triangolo
def draw_triangle(tartaruga, width):
  """ ' tartaruga' disegna un triangolo"""
  for i in range(3):
        tartaruga.forward(width)
        tartaruga.left(120)

#funzione per disegnare un rettangolo
def draw_rectangle(tartaruga, width, height):
  """ 'tartaruga' disegna un rettangolo di lato 'width' e altezza 'height' """ 
  for i in range(2):     # disegna 2 lati 2 volte
        tartaruga.forward(width)
        tartaruga.left(90)
        tartaruga.forward(height)
        tartaruga.left(90)


#richiesta 1: funzione per disegnare due quadrati
def draw_square2(tartaruga, side):
    """Specializzo 'draw_rectangle' per disegnare il quadrato"""
    for i in range(2):
        draw_rectangle(tartaruga, side, side)
    tartaruga.penup()
    tartaruga.goto(side, 0)
    tartaruga.pendown()


#funzione per disegnare un solo quadrato
def draw_square(my_turtle, side):
    """Specializzo 'draw_rectangle' per disegnare il quadrato"""
    draw_rectangle(my_turtle, side, side)


#richiesta 2: funzione per disegnare una croce
def draw_cross(tartaruga, width):
    for i in range(4):
        tartaruga.forward(width)
        tartaruga.left(90)
        tartaruga.forward(width)
        tartaruga.right(90)
        tartaruga.forward(width)
        tartaruga.left(90)


# programma principale (main) 
window = make_window("lightgreen", "tartaruga")

tartaruga = make_turtle("black", 3)


#richiesta 3: si chiede all'utente di scegliere cosa disegnare
#aggiungere un ciclo while
print('Scegli una tra queste figure:\ntriangolo\nrettangolo\nquadrato\ncroce')
a = input() 
if a == 'triangolo':
  draw_triangle(tartaruga, 50)
elif a == 'rettangolo':
  draw_rectangle(tartaruga, 20, 50)
elif a == 'quadrato':  
  draw_square(tartaruga, 50)
elif a == 'croce':
  draw_cross(tartaruga, 50)
else:
  print('scelta non valida')


#richiesta 4: tartaruga disegna 5 quadrati concentrici
def draw_square(tartaruga, width):
  """la funzione disegna 5 quadrati di lato, ciascuno icrementato di 9 passi rispetto al precedente"""
  for i in range(5):
    tartaruga.penup()
    tartaruga.goto(-width/2, -width/2)
    tartaruga.pendown()
    draw_rectangle(tartaruga, width, width)
    width = width + 9 #risolvere il problema del saltino

#richiesta 5: tartaruga disegna tre triangoli equidistanti 
x = 0
for i in range(3):
    print('Scegli una terna composta dai colori: rosso, blu, giallo')
    b = input()
    if b == 'rosso':
        tartaruga = make_turtle("red", 3)
        tartaruga.penup()
        tartaruga.goto(x, 0)
        tartaruga.pendown()
        draw_triangle(tartaruga, 50)
    elif b == 'blu':
        tartaruga = make_turtle("blue", 3)
        tartaruga.penup()
        tartaruga.goto(x, 0)
        tartaruga.pendown()
        draw_triangle(tartaruga, 50)
    elif b == 'giallo':
        tartaruga = make_turtle("yellow", 3)
        tartaruga.penup()
        tartaruga.goto(x, 0)
        tartaruga.pendown()
        draw_triangle(tartaruga, 50)
    else:
            print('scegli un colore tra quelli dati')

    x += 100


#richiesta 6: disegnare la figura
print('Scelgi il numero di lati')
c = input() #viene chiesto all'utente di inserire il numero di lati
print('Scegli la dimensione di partenza')
d = input() #viene chiesto all'utente la dimensione di partenza

x = 0 #posizione iniziale
y = 0 #posizione iniziale
dimensione = int(d) #la funzione converte la dimensione di partenza da una stringa ad un intero
for i in range(int(c)): #ciclo per disegnare il numero di figure indicato
    spaziatura = dimensione*1.5 #calcola quanto è la distanza con la figura successiva
    ruotata = i % 4 #determina la direzione della rotazione 


    # Triangolo
    t1 = make_turtle("green", 1) #crea un oggetto chiamato tartaruga che serve per disegnare il triangolo
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    if ruotata == 1: #gira verso l'alto
        t1.left(90)
        y += spaziatura
    elif ruotata == 2: #gira verso sinistra
        t1.left(180)
        x -= spaziatura
    elif ruotata == 3: #gira verso il basso
        t1.left(270)
        y -= spaziatura  
    else:
        x += spaziatura
    draw_triangle(t1, dimensione) #altrimenti disegna il triangolo con la dimensione corrente


    # Quadrato
    t2 = make_turtle("pink", 1) #crea una tartaruga per disegnare il quadrato
    t2.penup()
    t2.goto(x, y)
    t2.pendown()
    if ruotata == 1: #se gira verso l'alto 
        t2.left(90)
        y += spaziatura + dimensione / 3 #dimensione/3 serve ad evitare sovvraposizione tra figure
    elif ruotata == 2: #se gira verso sinistra 
        t2.left(180)
        x -= spaziatura + dimensione / 3
    elif ruotata == 3: #se gira verso il basso
        t2.left(270)
        y -= spaziatura + dimensione / 3
    else:
        x += spaziatura + dimensione / 3
    draw_square(t2, dimensione)

    # Croce
    t3 = make_turtle("blue", 1) #si crea un oggetto t3 che serve a disegnare la croce
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    if ruotata == 1: #se gira verso l'alto
        t3.left(90)
        y += 2 * (dimensione / 3)
        x -= 4 * (dimensione / 3)
    elif ruotata == 2: #se gira verso sinistra
        t3.left(180)
        y -= 4 * (dimensione / 3)
        x -= 2 * (dimensione / 3)
    elif ruotata == 3: #se gira verso il basso 
        t3.left(270)
        x += 4 * (dimensione / 3)
        y -= 2 * (dimensione / 3)
    else:
        x += 2 * (dimensione / 3)
        y = spaziatura
    draw_cross(t3, dimensione / 3)

    dimensione = dimensione*1.40 #la dimensione delle figure cresce ad ogni ciclo

    
#draw_triangle3(tartaruga, 50)

#draw_triangle(tartaruga, 50)

#draw_rectangle(tartaruga, 20, 50)

#draw_square2(tartaruga, 50)

#draw_square(tartaruga, 50)

#draw_cross(tartaruga, 50/3)


window.mainloop()