import pygame 
import random 
from Game.rock import Rock
from Game.rocket import Rocket
from Game.listOfRocks import ListOfRocks
  
pygame.init()  
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))  

done = False

pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# initialzing 
listOfRocks = ListOfRocks()

# test rocket
rocket = Rocket()

while not done:
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    listOfRocks.Collision(screen,rocket)
    # update

    rocket.update(screen)
    listOfRocks.update(fpsClock.get_time()/1000, rocket.score)
    

    # draw
    
    screen.fill((0,0,0))
    
    
    listOfRocks.draw(screen)

    
   
    rocket.draw(screen)


    rocket.drawScore(screen)




    
    pygame.display.flip()  
    fpsClock.tick(30)
