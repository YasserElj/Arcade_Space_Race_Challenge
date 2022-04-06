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

centerRect = pygame.Rect(320, 100, 2, 380)


# initialzing the list of rocks

listOfRocks = ListOfRocks()

# initialising the rocket

rocket1 = Rocket(135, 420, 1)

rocket2 = Rocket(455,420, 2)

while not done:

    # Checking if we closed the game to exit
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    # Checking if the rocket touched a rock
    listOfRocks.Collision(screen,rocket1)
    listOfRocks.Collision(screen,rocket2)

    # update the stat of the rocket
    rocket1.update(screen,fpsClock.get_time())
    rocket2.update(screen,fpsClock.get_time())

    # update the state of rocks1
    listOfRocks.update(fpsClock.get_time(), rocket1.score)
    
    # make the screen black
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), centerRect)
    # Draw the rocks
    listOfRocks.draw(screen)
   
    # Draw the rocket
    rocket1.draw(screen)

    rocket2.draw(screen)

    # Draw the score and the PB
    rocket1.drawScore(screen,5)

    rocket2.drawScore(screen,500)

    pygame.display.flip()  
    fpsClock.tick(30)
