import pygame 
import random 
from rock import Rock
from rocket import Rocket
from listOfRocks import ListOfRocks
  
pygame.init()  
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))  

done = False

# Playing the music
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# initialzing the list of rocks

listOfRocks = ListOfRocks()

# initialising the rocket

rocket = Rocket()

while not done:

    # Checking if we closed the game to exit
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    # Checking if the rocket touched a rock
    listOfRocks.Collision(screen,rocket)

    # update the stat of the rocket
    rocket.update(screen,fpsClock.get_time())

    # update the state of rocks
    listOfRocks.update(fpsClock.get_time(), rocket.score)
    
    # make the screen black
    screen.fill((0,0,0))
       
    # Draw the rocks
    listOfRocks.draw(screen)
   
    # Draw the rocket
    rocket.draw(screen)

    # Draw the score and the PB
    rocket.drawScore(screen)

    pygame.display.flip()  
    fpsClock.tick(30)
