import pygame

class Rocket:

    def __init__(self, x = 295, y = 420 ,player = 1,score = 0,PB = 0,DEFAULT_IMAGE_POSITION = (0,0),DEFAULT_IMAGE_SIZE = (40, 40)):
        self.x = x
        self.y = y
        self.score = score
        self.PB = PB
        self.player = player
        self.DEFAULT_IMAGE_POSITION = DEFAULT_IMAGE_POSITION =(self.x,self.y)
        self.DEFAULT_IMAGE_SIZE = DEFAULT_IMAGE_SIZE 
        

    def draw(self,screen):
        rocket = pygame.image.load("images/rocket.png")
        rocket = pygame.transform.scale(rocket, self.DEFAULT_IMAGE_SIZE)
        screen.blit(rocket, (self.x,self.y))
        rocketrect = rocket.get_rect()


    def drawScore(self,screen,c1):
        font = pygame.font.SysFont('freesansbold.ttc', 40)
        scoreText = font.render(f'Score : {self.score} ', True, (255,255,255))
        screen.blit(scoreText, (c1,5))
        PBText = font.render(f'PB : {self.PB} ', True, (0,255,0))
        screen.blit(PBText, (c1,450))

    # Delta-time is the amount of time that passed since the last frame

    def update(self,screen,deltatime,velocity=100):
        effect = pygame.mixer.Sound('sounds/score.wav')
        pressed = pygame.key.get_pressed()  
        if self.player == 1:
            if pressed[ord('w')]  : 
                self.y -= velocity*deltatime/1000
            if pressed[ord('s')]  and self.y<430: 
                self.y += velocity*deltatime/1000
            if pressed[ord('a')]  and self.x>0: 
                self.x -= velocity*deltatime/1000
            if pressed[ord('d')]  and self.x<590: 
                self.x += velocity*deltatime/1000

        elif self.player == 2:
            if pressed[pygame.K_UP]  : 
                self.y -= velocity*deltatime/1000
            if pressed[pygame.K_DOWN]   and self.y<430: 
                self.y += velocity*deltatime/1000
            if pressed[pygame.K_LEFT]   and self.x>0: 
                self.x -= velocity*deltatime/1000
            if pressed[pygame.K_RIGHT]  and self.x<590: 
                self.x += velocity*deltatime/1000

        if self.y<-50:
            self.score+=1
            (self.x,self.y)=self.DEFAULT_IMAGE_POSITION
            effect.play()
        
