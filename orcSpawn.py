import pygame


class OrcSpawn:
    def __init__(self, ox, oy, health, speed, restriction):
        self.ox = ox
        self.oy = oy
        self.health = health
        self.restricton = restriction
        self.orcsoldier = [
            pygame.image.load('OrcWalk/Orc1.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc2.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc3.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc4.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc5.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc6.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc7.png').convert_alpha(),
           # pygame.image.load('OrcWalk/Orc8.png').convert_alpha()
        ]

        self.checkpointReached = False

        self.orcRect = pygame.Rect(ox + 13, oy + 25, 30, 35)

        self.orcsoldier_right = [pygame.transform.scale(img, (70, 70)) for img in self.orcsoldier]
        self.orcsoldier_left = [pygame.transform.flip(img, True, False) for img in self.orcsoldier_right]
        self.orcMain = self.orcsoldier_right[0]

        self.orcAnimationIndex = 0 
        self.orcAnimationSpeed = 2
        self.orcAnimationCounter = 0
        self.orcDirection = 'Right'
        self.orcVelocityX = 0
        self.orcAccel = 0
        self.orcSpeed = speed
        self.friction = 0.9
    def AnimationOrc(self):
        self.orcAnimationCounter += 1
        if self.orcAnimationCounter >= self.orcAnimationSpeed:
            self.orcAnimationCounter = 0
            self.orcAnimationIndex += 1
            if self.orcAnimationIndex >= len(self.orcsoldier_right):
                self.orcAnimationIndex = 0

        if self.orcDirection == 'Right':
            self.orcMain = self.orcsoldier_right[self.orcAnimationIndex]
        if  self.orcDirection == 'Left':
            self.orcMain = self.orcsoldier_left[self.orcAnimationIndex] 

    def orcAi(self, player, hostility):
        if hostility == True:
            self.orcAccel = self.orcSpeed * (1 - self.friction)
            if player.x < self.ox:
                self.orcDirection = 'Left'
                self.orcVelocityX -= self.orcAccel
                
            if player.x > self.ox:
                self.orcDirection = 'Right'
                self.orcVelocityX += self.orcAccel

            self.orcRect = pygame.Rect(self.ox + 13, self.oy + 25, 30, 35)

            self.orcVelocityX *= self.friction
            self.ox += self.orcVelocityX


        if self.restriction == True:
            if self.ox > 750:
                self.ox = 750
            if self.ox < 0:
                self.ox = 0

    def orcMove(self, targetX, hostility):
        if hostility == False:
            
            self.orcAccel = self.orcSpeed * (1 - self.friction)
            if self.checkpointReached == False:
                if targetX > self.ox:
                    self.orcDirection = 'Right'
                    self.orcVelocityX += self.orcAccel
                if targetX < self.ox:
                    self.orcDirection = 'Left'
                    self.orcVelocityX -= self.orcAccel
                    
                self.orcVelocityX *= self.friction
                self.ox += self.orcVelocityX

            
            if targetX == self.ox:
                self.checkpointReached = True
            if targetX != self.ox:
                self.checkpointReached = False
        

    def attack(self, player, hostility):
        if hostility == True:
            if self.orcRect.colliderect(player.playerRect):
                player.health -= 2

    def draw(self, screen):
        screen.blit(self.orcMain, (self.ox, self.oy))
       # pygame.draw.rect(screen, (0, 255, 0), self.orcRect, 2) 