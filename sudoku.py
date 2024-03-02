
import pygame as pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(size=(65*10,65*10))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
running = True


def setGameBoard():

    screen.fill("gray")
    for x in range(0,9):
        top = 32.5+65*x
        for y in range(0,9):
            left = 32.5+65*y
            rect_obj = pygame.draw.rect(screen, ("white"),(top,left,60,60))

        #Border
    pygame.draw.line(screen,("black"),[31,31],[31,65*9+31],5) #Vertical 0
    pygame.draw.line(screen,("black"),[65*3+29.5,31],[65*3+29.5,65*9+31],5) #Vertical #1
    pygame.draw.line(screen,("black"),[65*6+29.5,31],[65*6+29.5,65*9+31],5) #Vertical #2
    pygame.draw.line(screen,("black"),[65*9+29.5,31],[65*9+29.5,65*9+31],5) #Vertical #3

    pygame.draw.line(screen,("black"),[29,31],[65*9+31,31],5) #Horizontal 0
    pygame.draw.line(screen,("black"),[31,65*3+29.5],[65*9+31,65*3+29.5],5) #Horizontal #1
    pygame.draw.line(screen,("black"),[31,65*6+29.5],[65*9+31,65*6+29.5],5) #Horizontal #2
    pygame.draw.line(screen,("black"),[31,65*9+29.5],[65*9+31,65*9+29.5],5) #Horizontal #3


def setText(screen):
    font = pygame.font.SysFont(None, 60) #Sets the font of the text
    text_surface = font.render("2", True, "black") #Renders the text in a box
    screen.blit(text_surface, (65, 65)) #Sets said box into the screen surface


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for event click mouse1:
            #make selected box blue-ish (change collor)
            #Make diagonal and horizontal lines blue-ish but less than the selected one
            #Get coordinates so u can setText
            #check if theres already a number inside
            #Check which number is pressed so u can set the number inside

    # for event keyboard arrows, switch between boxes with them
    #Maybe select other numbers that are the same (so if 2 selected all 2s on the board will light up)

    setGameBoard()
    setText(screen)    

    pygame.display.flip()
pygame.quit()
