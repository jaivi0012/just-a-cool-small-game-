import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.oldX = 0
        self.y_velocity = 0
        self.x_speed = 8
        self.y_jump = -15
        self.gravity = 0.9
        self.on_ground = False
        self.health = 3000
        self.jumpCounter = 0
        self.aninationIndex = 0
        self.animationSpeed = 2
        self.animationCounter = 0
        self.Direction = "Right"
        self.moving = False
        self.under = False
        screen = pygame.display.set_mode((800, 600))
        self.playerRect = pygame.Rect(x + 21, y+ 22, 30, 40)

        playerFrames = [
            pygame.image.load('SoldierWalk/Soldier_Walk1.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk2.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk3.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk4.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk5.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk6.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk7.png').convert_alpha(),
            pygame.image.load('SoldierWalk/Soldier_Walk8.png').convert_alpha()
        ]

        self.player_right = [pygame.transform.scale(img, (70, 70)) for img in playerFrames]
        self.player_left = [pygame.transform.flip(img, True, False) for img in self.player_right]
        self.playerImage = self.player_right[0]

    def playerUpdate(self):
        self.playerRect.topleft = (self.x + 21, self.y + 22)

    def move(self,key):
       
       
        if key[pygame.K_LEFT]:
            self.x -= self.x_speed
            self.Direction = 'Left'
            self.moving = True
        if key[pygame.K_RIGHT]:
            self.x += self.x_speed
            self.Direction = 'Right'
            self.moving = True
        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.moving = False


       
        self.y_velocity += self.gravity
        self.y += self.y_velocity

        if self.under == False:
            if self.y >= 500:
                self.y = 500
                self.y_velocity = 0
                self.on_ground = True
                self.jumpCounter = 0
            else:
                self.on_ground = False

        if self.y >= 500:
            self.on_ground = True
        if self.y < 500:
            self.on_ground = False
       
        if self.x > 111 and self.x < 154 and self.y >= 500:
            self.under = True
        else:
            self.under = False

        if self.y > 700:
            self.y = 700

        if self.jumpCounter > 2 and self.on_ground == True:
            self.jumpCounter = 0

    def jump(self):
        if self.jumpCounter <= 2:
            self.y_velocity = self.y_jump
        self.jumpCounter += 1

        
    def damageEnemy(self, enemyRect, enemyType):
        if self.playerRect.colliderect(enemyRect) and enemyType == "orcSoldier":
            self.health -= 2
        if self.playerRect.colliderect(enemyRect) and enemyType == "orcBoss":
            self.health -= 6
            
    def playerDirection(self, keys):
        if self.moving == True:
            self.animationCounter += 1
            if self.animationCounter > self.animationSpeed:
                self.animationIndex += 1
                self.animationCounter = 0
            if self.animationIndex >= len(self.player_right):
                self.animationIndex = 0
        if self.moving == False:
            self.animationIndex = 0  

     
        if self.Direction == "Left":
            self.playerImage = self.player_left[self.animationIndex]
        if self.Direction == 'Right':
            self.playerImage = self.player_right[self.animationIndex]



    def playerDisplay(self, screen):
        screen.blit(self.playerImage, (self.x, self.y))
