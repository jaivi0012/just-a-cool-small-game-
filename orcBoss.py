import pygame

class orcBoss:
    def __init__(self, ox, oy, health, height, width):
        self.ox = ox 
        self.oy = oy
        self.health = health # 6000
        self.height = height # 150
        self.width = width # 150
        self.speed = 2
        self.orcVelocityX = 0
        self.friction = 0.9
        self.orcRect = pygame.Rect(self.ox + 35, self.oy + 25, 80, 100)
        self.boss = pygame.image.load('OrcWalk/Orc1.png').convert_alpha()
        self.scaled = pygame.transform.scale(self.boss, (self.height, self.width))
        self.dra = self.scaled
        self.damage = 6
        self.orcDirection = 'Right'
    def update(self):
        self.orcRect = pygame.Rect(self.ox + 35, self.oy + 25, 80, 100)
        if self.orcDirection == 'Right':
            self.dra = self.scaled
        if self.orcDirection == 'Left':
            self.dra = pygame.transform.flip(self.scaled, True, False)
    def track(self, player, enemy, hostility):
        if hostility == True:
            if player.x > self.ox:
                self.ox += self.speed
                self.orcDirection = 'Right'
            if player.x < self.ox:
                self.ox -= self.speed
                self.orcDirection = 'Left'
        if hostility == False:
            if enemy.ox > self.ox:
                self.ox += self.speed
                self.orcDirection = 'Right'
            if enemy.ox < self.ox:
                self.ox -= self.speed
                self.orcDirection = 'Left'

    def attack(self, player, enemy, hostility):
        if hostility == True:
            if self.orcRect.colliderect(player.playerRect):
                player.health -= self.damage
        if hostility == False:
            if self.orcRect.colliderect(enemy.orcRect):
                enemy.health -= self.damage

    def draw(self, screen):
        screen.blit(self.scaled, (self.ox, self.oy))
       # pygame.draw.rect(screen, (0, 255, 0), self.orcRect, 2)