import pygame
class background:
    def __init__(self, ):
        self.back1 = pygame.image.load('backgroundImg/Sprite-0001.png')

    def draw(self, screen, currentBackgroundReq):
        currentBack = None
        if currentBackgroundReq == 'back1':
            currentBack = self.back1

        screen.blit(currentBack, (0, 0))