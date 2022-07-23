from gl2 import *

#Matriz de puntos a utilizar.
casa = [
    [0.3, -0.5, 0.3, -0.1], #Pared 1.
    [0.7, -0.5, 0.7, -0.1], #Pared 2.
    [0.3, -0.5, 0.7, -0.5], #Suelo.
    [0.3, -0.1, 0.7, -0.1], #Techito.
    [0.3, -0.1, 0.5, 0.1], #Techo formal. (Parte izquierda)
    [0.5, 0.1, 0.7, -0.1], #Techo formal. (Parte derecha)
    [-0.1, -0.2, -0.1, 0.1], #Pared de la izquierda. (Fondo)
    [-0.1, 0.1, 0.2, 0.1], #Pared de arriba. (Fondo)
    [0.3, -0.5, -0.1, -0.2], #Haciendo unión. (Pared de la izquierda)
    [0.3, -0.1, -0.1, 0.1], #Haciendo unión. (Pared de la izquierda, parte de arriba)
    [-0.1, 0.1, 0.1, 0.3] #Haciendo techo del fondo. (Parte izquierda)
]

def main():

    glCreateWindow(1024, 1024) #Creando la ventana.
    glClearColor(0, 0, 0) #Llenando el color de la pantalla.
    glClear() #Llenando el mapa de bits con el color que se le pasa.

    #Se comentó la instancia que está arriba de f.close() para debuggear el glViewPort().

    #Ancho y alto de la pantalla en donde se dibujará el punto.
    ancho = 501
    alto = 501
    
    #Sumarle uno al ancho y al alto.

    #Posición del viewport.
    posx = 250
    posy = 250

    glViewPort(posx, posy, ancho, alto) #Definiendo el área de la imagen sobre la que se va a poder dibujar.
    glColor(0.8, 0.2, 0.1) #Definiendo el color del punto.
    #glVertex(1, 1) #Definiendo el punto inicial del punto.
    #       x0,   y0,   x1,   y1
    glLine(0.3, -0.5, 0.3, -0.1) #Haciendo primera línea. (Pared izquierda)
    glLine(0.7, -0.5, 0.7, -0.1) #Haciendo segunda línea. (Pared derecha)
    glLine(0.3, -0.5, 0.7, -0.5) #Haciendo tercera línea. (Piso de abajo)
    glLine(0.3, -0.1, 0.7, -0.1) #Haciendo cuarta línea. (Techito)
    glLine(0.3, -0.1, 0.5, 0.1) #Haciendo quinta línea. (Techo)
    glLine(0.5, 0.1, 0.7, -0.1) #Haciendo sexta línea. (Techo)
    glLine(-0.1, -0.2, -0.1, 0.1) #Haciendo fondo. (Pared de la izquierda)
    #glLine(0.2, 0, 0.2, 0.1) #Haciendo fondo. (Pared de la derecha)
    glLine(-0.1, 0.1, 0.2, 0.1) #Haciendo fondo. (techo del fondo)
    glLine(0.3, -0.5, -0.1, -0.2) #Haciendo primera unión. (Pared izquierda)
    glLine(0.3, -0.1, -0.1, 0.1) #Haciendo segunda unión. (Pared izquierda, parte de arriba)
    glLine(0.7, -0.1, 0.2, 0.1) #Haciendo tercera unión. (Pared derecha, parte de arriba)
    glLine(-0.1, 0.1, 0.044, 0.3) #Haciendo el techo del fondo. (Parte izquierda)
    glLine(0.2, 0.1, 0.05, 0.3) #Haciendo el techo del fondo. (Parte derecha)
    glLine()
    glFinish() #Escribiendo la ventana.

main()