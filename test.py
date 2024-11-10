import pygame
from pygame import locals
pygame.init()

width = 1280
height = 720

display = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

rot = 0
running = True
while running: 

    for event in pygame.event.get(): 
        match event.type:
            case pygame.QUIT:
                running = False
            case locals.KEYDOWN:
                
                match event.key:
                    case locals.K_RIGHT:
                        print("derecha")
                    case locals.K_LEFT:
                        print("Izquierda")


    display.fill((rot, 255, 255))
    
    rot = rot + 1
    if rot > 255:
        rot = 0

    player = pygame.draw.rect(display, (50, 50, 50), (width/2 - 100, height-50, 200, 50))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
