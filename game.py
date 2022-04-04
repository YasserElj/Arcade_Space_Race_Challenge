import pygame 
import random 
  
pygame.init()  
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))  
done = False  
color = (0, 125, 255)
x=295
y=420
speed=(5,5)
score=0

vel = 4
ball = pygame.image.load("rocket.png")
S=[0,2,4,6]
L=[random.randrange(60,480) for i in range(10)]


xx = 0

def rock(x):
    for i in L:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(xx, i, 6, 2))



font2 = pygame.font.SysFont('freesansbold.ttc', 40)
DEFAULT_IMAGE_SIZE = (40, 40)

DEFAULT_IMAGE_POSITION = (x,y)

effect = pygame.mixer.Sound('score.wav')


ball = pygame.transform.scale(ball, DEFAULT_IMAGE_SIZE)

ballrect = ball.get_rect()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

while not done:

    img2 = font2.render(f'Score : {score} ', True, (255,255,255))
    pressed = pygame.key.get_pressed()   
    for event in pygame.event.get():  
        
        if event.type == pygame.QUIT:  
            done = True  
        
    if pressed[pygame.K_UP]: 
        y -= vel
    if pressed[pygame.K_DOWN] and y<430: 
        y += vel
    if pressed[pygame.K_LEFT] and x>0: 
        x -= vel 
    if pressed[pygame.K_RIGHT] and x<590: 
        x += vel
    screen.fill((0,0,0))
    screen.blit(ball, (x,y))
    screen.blit(img2, (5,5))
    for i in S:
        rock(i)

        i+=random.randrange(1,10)

    if y<-50:
        score+=1
        (x,y)=DEFAULT_IMAGE_POSITION
        effect.play()

    
    xx+=3
    pygame.display.flip()  
    fpsClock.tick(30)
