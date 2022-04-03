import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((640,480))  
done = False  
color = (0, 125, 255)
x=295
y=420
speed=(5,5)
score=0
ball = pygame.image.load("rocket.png")

font2 = pygame.font.SysFont('freesansbold.ttc', 40)
DEFAULT_IMAGE_SIZE = (50, 50)

DEFAULT_IMAGE_POSITION = (x,y)

effect = pygame.mixer.Sound('score.wav')


ball = pygame.transform.scale(ball, DEFAULT_IMAGE_SIZE)

ballrect = ball.get_rect()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
while not done:

    img2 = font2.render(f'Score : {score} ', True, (255,255,255))
    pressed = pygame.key.get_pressed()   
    for event in pygame.event.get():  
        
        if event.type == pygame.QUIT:  
            done = True  
        
    if pressed[pygame.K_UP]: 
        y -= 1/10
    if pressed[pygame.K_DOWN] and y<430: 
        y += 1 /10
    if pressed[pygame.K_LEFT] and x>0: 
        x -= 1 /10
    if pressed[pygame.K_RIGHT] and x<590: 
        x += 1/10
    screen.fill((0,0,0))
    screen.blit(ball, (x,y))
    screen.blit(img2, (5,5))

    if y<-50:
        score+=1
        (x,y)=DEFAULT_IMAGE_POSITION
        effect.play()

        
        
  
    pygame.display.flip()  
