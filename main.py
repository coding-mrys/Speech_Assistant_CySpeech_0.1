import pygame

#own imports
import objs
import CySpeech

#setup
pygame.display.set_caption("CyHome 1.1")
pygame.init()
clock= pygame.time.Clock()
screen = pygame.display.set_mode([1600,900])

#show objs
def show():
    screen.blit(objs.bg,(0,0))
    screen.blit(objs.btn,(650,300))
    
a=0 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
    mouse_x,mouse_y = pygame.mouse.get_pos()

    #speak
    if mouse_x >=650 and mouse_x<=950 and mouse_y>=300 and mouse_y<=600 and event.type == pygame.MOUSEBUTTONUP:
        a+=1
        objs.btn = pygame.image.load("graphics/btn2.png")
        if a>1:
            #start main script
            CySpeech.speech()
            a=0
    else:
        objs.btn = pygame.image.load("graphics/btn.png")

    #show
    show()
    clock.tick(60)
    pygame.display.update()