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
        self.speed = 5
        self.friction = 0.9
        self.orcVelocityX = 0
        self.velocityY = 0
        self.orcRect = pygame.Rect(self.ox + 200, self.oy + 200, width, height)
        self.boss = pygame.image.load('Boss/pumpkin1.png').convert_alpha()
        self.bossDraw = pygame.transform.scale(self.boss, (height, width))
        self.jumped = False
        self.damage = 10
        self.gameFont = pygame.font.Font(None, 36)
        self.maceD = False

        self.bossAttack = pygame.image.load('Boss/pumpkinAttack.png').convert_alpha()
        self.text = self.gameFont.render(f"larry the Pumpkin Health: {self.health}", True, (255, 255, 255))

    
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

    def smartHunt(self, player):
        accel = self.speed * (1 - self.friction)
        playerCentre = player.x + 35
        bossCentre = self.ox + self.width / 2
        distance = playerCentre - bossCentre        

        playerInAir = player.y < 480
        playerAbove = playerInAir and abs(distance) < 140

        if playerAbove:
           
            if distance > 0:
                direction = -1
            else:
                direction = 1
          
            if self.ox <= 10 and direction == -1:
                direction = 1
            if self.ox >= 800 - self.width - 10 and direction == 1:
                direction = -1
            self.orcVelocityX += direction * accel * 2
        else:
           
            boost = 1
            if abs(distance) < 250 and playerInAir == False:
                boost = 1.5
            if distance < -10:
                self.orcVelocityX -= accel * boost
            if distance > 10:
                self.orcVelocityX += accel * boost

        self.orcVelocityX *= self.friction
        self.ox += self.orcVelocityX

        if self.ox < 0:
            self.ox = 0
            self.orcVelocityX = 0
        if self.ox > 800 - self.width:
            self.ox = 800 - self.width
            self.orcVelocityX = 0

    def attack(self, player):
        if self.orcRect.colliderect(player.playerRect):
            player.health -= self.damage

    def Draw(self, screen):
        screen.blit(self.bossDraw, (self.ox, self.oy))
       # pygame.draw.rect(screen, (0, 255, 0), self.orcRect, 2)
        screen.blit(self.text, (350, 20))