import pygame

class AiEnemy:
    def __init__(self, x, y, width, height, health, speed):
        self.ox = x
        self.oy = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed
        self.orcVelocityX = 0
        self.accel = 0
        self.friction = 0.9
        self.attackDamage = 9
        self.startX = x
        self.startY = y
        self.startHealth = health
        self.hasAttacked = False
        self.AttackCounter = 0
        self.image = pygame.image.load('ai.png').convert_alpha()
        self.Scaledimage = pygame.transform.scale(self.image, (width, height))
        self.orcRect = pygame.Rect(x, y, width, height)
    def move(self, targetx, hostility):
        if hostility == True:
            self.accel = self.speed * (1 - self.friction)

            if targetx + 2 > self.ox:
                self.orcVelocityX -= self.accel
            if targetx -2 < self.ox:
                self.orcVelocityX += self.accel

            self.orcVelocityX *= self.friction
            self.ox += self.orcVelocityX

    def approach(self, player, hostility):
        if hostility == True:
            self.accel = self.speed * (1 - self.friction)

            if player.x < self.ox:
                self.orcVelocityX -= self.accel
            if player.x > self.ox:
                self.orcVelocityX += self.accel

            self.orcVelocityX *= self.friction
            self.ox += self.orcVelocityX

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

    def restriction(self, restriction):
        if restriction == True:
            if self.ox > 730:
                self.ox = 730
            if self.ox < 0:
                self.ox = 0
        if restriction == False:
            pass
        
    def update(self):
        self.orcRect = pygame.Rect(self.ox, self.oy, self.width, self.height)

    def reset(self):
        self.ox = self.startX
        self.oy = self.startY
        self.health = self.startHealth
        self.hasAttacked = False
        self.AttackCounter = 0
        self.update()

    def Draw(self, screen):
        screen.blit(self.Scaledimage, (self.ox, self.oy))