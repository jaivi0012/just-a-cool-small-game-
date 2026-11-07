import pygame

class Boss:
    def __init__(self, x, y, health, height, width):
        self.ox = x
        self.oy = y
        self.health = health
        self.height = height
        self.width = width
        self.animationSpeed = 5
        self.animationIndex = 0
        self.animationCounter = 0
        self.speed = 3
        self.friction = 0.9
        self.orcVelocityX = 0
        self.velocityY = 0
        self.orcRect = pygame.Rect(self.ox, self.oy, width, height)
        self.boss = pygame.image.load('Boss/pumpkin1.png').convert_alpha()
        self.bossDraw = pygame.transform.scale(self.boss, (height, width))
        self.jumped = False
        self.damage = 8
        self.gameFont = pygame.font.Font(None, 36)

        self.bossAttack = pygame.image.load('Boss/pumpkinAttack.png').convert_alpha()
        self.text = self.gameFont.render(f"larry the slime Health: {self.health}", True, (255, 255, 255))

    
    def update(self):
        self.orcRect = pygame.Rect(self.ox, self.oy, self.width, self.height)
        self.text = self.gameFont.render(f"larry the Pumpkin Health: {self.health}", True, (255, 255, 255))
    def hunt(self, player):
        accel = self.speed * (1 - self.friction)
        playerCentre = player.x + 35                
        bossCentre = self.ox + self.width / 2        
        if playerCentre < bossCentre - 10:           
            self.orcVelocityX -= accel
        if playerCentre > bossCentre + 10:
            self.orcVelocityX += accel
        self.orcVelocityX *= self.friction
        self.ox += self.orcVelocityX

    def attack(self, player):
        if self.orcRect.colliderect(player.playerRect):
            player.health -= self.damage

    def Draw(self, screen):
        screen.blit(self.bossDraw, (self.ox, self.oy))
        pygame.draw.rect(screen, (0, 255, 0), self.orcRect, 2)
        screen.blit(self.text, (300, 20))