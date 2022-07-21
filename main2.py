from gl2 import *


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
    #x0, y0, x1, y1 = 0, 0, 1, 1
    glLine(0.2, 0.1, 0.7, 0.8) #Dibujando la línea.
    #glLine(0.1, 0.7, 0.2, 0.8) #Dibujando la línea.
    glFinish() #Escribiendo la ventana.

main()