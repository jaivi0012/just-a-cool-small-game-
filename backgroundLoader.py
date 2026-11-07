import pygame
class background:
    def __init__(self, ):
        self.back1 = pygame.image.load('backgroundImg/Sprite-0001.png').convert()
        self.back2 = pygame.image.load('backgroundImg/Sprite-0002.png').convert()
        self.back3 = pygame.image.load('backgroundImg/Sprite-0003.png').convert()
        self.back4 = pygame.image.load('backgroundImg/Sprite-0004.png').convert()
        self.back5 = pygame.image.load('backgroundImg/Sprite-0005.png').convert()
        self.back6 = pygame.image.load('backgroundImg/Sprite-0006.png').convert()
        self.back7 = pygame.image.load('backgroundImg/Sprite-0007.png').convert()

    def draw(self, screen, currentBackgroundReq):
        currentBack = None
        if currentBackgroundReq == 'back1':
            currentBack = self.back1
        if currentBackgroundReq == 'back2':
            currentBack = self.back2
        if currentBackgroundReq == 'back3':
            currentBack = self.back3
        if currentBackgroundReq == 'back4':
            currentBack = self.back4
        if currentBackgroundReq == 'back5':
            currentBack = self.back5
        if currentBackgroundReq == 'back6':
            currentBack = self.back6
        if currentBackgroundReq == 'back7':
            currentBack = self.back7
        
        screen.blit(currentBack, (0, 0))