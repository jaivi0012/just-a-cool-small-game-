import pygame

class AiEnemy:
    def __init__(self, x, y, width, height, health, speed):
        self.ox = x
        self.oy = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed
        self.orcVelcityX = 0
        self.accel = 0
        self.friction = 0.9
        self.attackDamage = 100
        
        self.image = pygame.image.load('ai.png').convert_alpha()
        self.Scaledimage = pygame.transform.scale(self.image, (width, height))
        self.orcRect = pygame.Rect(x, y, width, height)
        self.hasAttacked = False
        self.AttackCounter = 0
    def move(self, targetx, hostility):
        if hostility == True:
            self.accel = self.speed * (1 - self.friction)

            if targetx + 2 > self.ox:
                self.orcVelcityX -= self.accel
            if targetx -2 < self.ox:
                self.orcVelcityX += self.accel

            self.orcVelcityX *= self.friction
            self.ox += self.orcVelcityX

    def approach(self, player, hostility):
        if hostility == True:
            self.accel = self.speed * (1 - self.friction)

            if player.x > self.ox:
                self.orcVelcityX -= self.accel
            if player.x < self.ox:
                self.orcVelcityX += self.accel

            self.orcVelcityX *= self.friction
            self.ox += self.orcVelcityX

    def attack(self, player, hostility):
        if hostility == True:
            if self.hasAttacked == False:
                if self.orcRect.colliderect(player.playerRect):
                    player.health -= self.attackDamage
                    self.hasAttacked = True
            if self.hasAttacked == True:
                self.AttackCounter += 1
                if self.AttackCounter > 60:
                    self.hasAttacked = False
                    self.AttackCounter = 0

    def update(self):
        self.orcRect = pygame.Rect(self.ox, self.oy, self.width, self.height)

    def Draw(self, screen):
        screen.blit(self.Scaledimage)