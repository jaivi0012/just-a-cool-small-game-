import pygame

class ramAltman:
    def __init__(self, ox, oy, health, move, width, height):

        self.ox = ox
        self.oy = oy
        self.health = health
        self.move = move
        self.accel = 0
        self.speed = 3
        self.width = width
        self.height = height
        self.orcVelocityX = 0
        self.friction = 0.9
        self.attack = False
        self.AltmanIdle = pygame.image.load('Ram_Altman.png').convert_alpha()
        # self.AltmanArmSpread = pygame.image.load('').convert_alpha
        self.AltmanScaled = pygame.transform.scale(self.AltmanIdle, (height, width))
        self.AltmanDraw = self.AltmanScaled
        self.orcRect = pygame.Rect(self.ox, self.oy, width, height)
    def move(self, targetx, targety, hostility):
        if hostility == False:
            
            self.accel = self.speed * (1 - self.friction)
            
            if self.ox + 2 > targetx:
                self.orcVelocityX -= self.accel

            if self.ox - 2 < targetx:
                self.orcVelocityX += self.accel

            if self.ox == targetx:
                pass

            self.orcVelocityX *= self.friction 
            self.ox += self.velocityX

    def smartMove(self, player, hostility):

        if hostility == True:
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

    def update(self):
        self.orcRect = pygame.Rect(self.ox, self.oy, self.height, self.width)

    def draw(self, screen):

        screen.blit(self.AltmanDraw)