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
        self.castle1 = pygame.image.load('backgroundImg/castle1.png').convert()
        self.castle2 = pygame.image.load('backgroundImg/castle2.png').convert()
        self.castle3 = pygame.image.load('backgroundImg/castle3.png').convert()
        self.castle4 = pygame.image.load('backgroundImg/castle4.png').convert()
        self.castle5 = pygame.image.load('backgroundImg/castle5.png').convert()
        self.castle6 = pygame.image.load('backgroundImg/castle6.png').convert()

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
        if currentBackgroundReq == 'castle1':
            currentBack = self.castle1
        if currentBackgroundReq == 'castle2':
            currentBack = self.castle2
        if currentBackgroundReq == 'castle3':
            currentBack = self.castle3
        if currentBackgroundReq == 'castle4':
            currentBack = self.castle4
        if currentBackgroundReq == 'castle5':
            currentBack = self.castle5
        if currentBackgroundReq == 'castle6':
            currentBack = self.castle6        
        screen.blit(currentBack, (0, 0))