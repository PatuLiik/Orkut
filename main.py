import pygame
import sys
import character
import level

pygame.init()

player1 = character.CharObject(150, 100, 1)

screen = pygame.display.set_mode([480, 270])

game_start = False

taust = pygame.image.load("taust2.jpg")

while True: #---MAIN LOOP---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#QUIT
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:#JUMP1
                game_start = True
                player1.jump(-25)
            if event.key == pygame.K_0:#LEVEL1
                game_start = True
                level.level_create(0, screen, screen, screen, player1)
            
    keys = pygame.key.get_pressed()#MOVE1
    if keys[pygame.K_RIGHT]:
        player1.move(2)
    if keys[pygame.K_LEFT]:
        player1.move(-2)
        
    #screen.fill([255, 160, 0])
    screen.blit(taust, [0,0])
    #SEE PANEB TAUSTA, AGA TUNDUB ET SEE TEEB SELLE NATUKE AEGLASEMAKS(VÕIB KATSETADA)

    if game_start: #---GAMEPLAY---#

        player1.update() #lisab hõõrde ja gravitatsiooni

        level.level_create(0, screen, screen, screen, player1) #teeb leveli ja vaatab collisionit

        player1.final_loc() #paneb lõppkoordinaadid
    
        player1.draw(screen) #joonistab playeri

        
                                 
    pygame.display.flip()

    pygame.time.wait(35)
                                
