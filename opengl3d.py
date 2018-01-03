import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])    
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -50)
    glRotatef(0, 0, 0, 0)
    i = 0

    while True:
        glTranslatef(0,0,i)
        i += 0.00005
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:
##                    glTranslatef(0,0,1.0)
##                if event.button == 5:
##                    glTranslatef(0,0,-1.0)

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
        


    
