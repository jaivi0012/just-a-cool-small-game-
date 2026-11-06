import pygame
import math

class Weapons:
    def __init__(self, player):
        self.currentWeapon = 'mace'
        self.maceJump = -25
        self.maceCounter = 0
        self.Knockback = 20
        self.orbitalCounter = 0
        self.orbitalCycle = 3
        self.tntVelocity = 0
        maceImg = pygame.image.load('mace.png').convert_alpha()
        spearImg = pygame.image.load('Diamond_Spear.png').convert_alpha()
        rodImg = pygame.image.load('Fishing_Rod.png').convert_alpha()
        self.maceSfx = pygame.mixer.Sound('Sounds/mace.wav')
        self.damageSfx = pygame.mixer.Sound('Sounds/damage.wav')
        self.lungeSfx = pygame.mixer.Sound('Sounds/spear.wav')
       
        self.mace_right = pygame.transform.scale(maceImg, (30, 30))
        self.mace_left = pygame.transform.flip(self.mace_right, True, False)
        
        self.spear_right = pygame.transform.scale(spearImg, (30, 30))
        self.spear_left = pygame.transform.flip(self.spear_right, True, False)
        
        self.rod_right = pygame.transform.scale(rodImg, (30, 30))
        self.rod_left = pygame.transform.flip(self.rod_right, True, False)

        self.maceRect = pygame.Rect(player.x + 25,player.y + 45,20,80)
        self.maceDamage = None
        self.facing_direction = player.Direction

        self.nuke = False
        self.orbital = False
        self.orbitalStarted = False
        self.tnt = [
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert(),
                        pygame.image.load('tnt.jpeg').convert()
                    ]
        
        self.scaledTnt = [pygame.transform.scale(img, (30, 30)) for img in self.tnt]
    
        self.tntX = [0, 90, 180, 270, 360, 450, 540, 630, 720]
        self.tntY = 0

        self.currentImg = self.mace_right

    def update(self, player, orc_List):
        self.maceRect = pygame.Rect(player.x + 25,player.y + 45,20,80)
        nukeWasOn = self.nuke
        orbitalWasOn = self.orbital
        if self.orbitalCounter <= 85:
            self.orbitalCounter += 1 
        if self.orbitalCounter > 85:
            self.orbitalCounter = 0
        if self.orbitalCounter > 42: 
            self.orbital = True
            self.nuke = False
        if self.orbitalCounter <= 0:
            self.orbital = False
            self.nuke = True
            self.orbitalCycle += 1
            if self.tntY > 500:
                self.tntY = 500

        if self.orbitalStarted == True:
            
            self.tntVelocity += 0.9
            self.tntY += self.tntVelocity
            if self.tntY > 530:
                self.tntY = 530
        if self.orbitalCycle >= 3:
            if self.orbitalStarted == True and orbitalWasOn  == True:
                # your old "cycles >= 3" explosion: damage applied once, before the reset below
                # (later you can start the explosion animation here as well)
                for x in self.tntX:
                    ax = x + 15
                    ay = self.tntY + 15
                    for orc in orc_List:
                        bx = orc.ox + 35
                        by = orc.oy + 35
                        distance = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
                        if distance < 65:
                            orc.health -= 70

            self.nuke = False
            self.orbital = False
            self.orbitalStarted = False
            self.tntY = 0
            self.tntVelocity = 0
    def mace(self, orc_List, player):
        self.currentWeapon = 'mace'
        fallspeed = max(player.y_velocity, 0)      # read ONCE, before the bounce changes it
        bounced = False

        for orc in orc_List:
            if orc.health <= 0:                   
                continue
            if self.maceRect.colliderect(orc.orcRect):
                maceDamage = 0

                if fallspeed > 0:
                    maceDamage = 10 + fallspeed * 3
                    if bounced == False:          
                        player.y_velocity = self.maceJump
                        self.maceSfx.play()
                        bounced = True

                if fallspeed == 0 and player.y >= 490:
                    maceDamage = 20
                    self.damageSfx.play()

                orc.health -= maceDamage

                if player.Direction == 'Left':
                    orc.orcVelocityX -= self.Knockback / 2
                if player.Direction == 'Right':
                    orc.orcVelocityX += self.Knockback / 5

    def spear(self, player):      
        self.currentWeapon = 'spear'
        if player.Direction == 'Left':
            player.x += -20
        if player.Direction == 'Right':
            player.x += 20
        self.lungeSfx.play()

    def rod(self): 
        self.currentWeapon = 'rod'
        self.orbital = False
        self.nuke = True
        self.orbitalStarted = True
        self.orbitalCounter = 0
        self.orbitalCycle = 0

            
     
    
    def draw(self, screen, player):
    
        if self.currentWeapon == 'mace':
            if player.Direction == 'Left':
                self.currentImg = self.mace_right
            if player.Direction == 'Right':
                self.currentImg = self.mace_left
        if self.currentWeapon == 'spear':
            if player.Direction == 'Right':
                self.currentImg = self.spear_right
            if player.Direction == 'Left':
                self.currentImg = self.spear_left
        if self.currentWeapon == 'rod':
            if player.Direction == 'Right':
                self.currentImg = self.rod_right
            if player.Direction == 'Left':
                self.currentImg = self.rod_left

        if player.Direction == 'Right':
            screen.blit(self.currentImg, (player.x + 51, player.y + 16))
        if player.Direction == 'Left':
            screen.blit(self.currentImg, (player.x - 13, player.y + 16))
       # pygame.draw.rect(screen, (0, 255, 0), self.maceRect, 2)

        if self.nuke == True:
            for tnt_img, x_val in zip(self.scaledTnt, self.tntX):
                        screen.blit(tnt_img, (x_val, self.tntY))
                
        if self.orbital == True:
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[0], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[1], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[2], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[3], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[4], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[5], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[6], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[7], self.tntY, 30, 30))
            pygame.draw.rect(screen, (255, 255, 255), (self.tntX[8], self.tntY, 30, 30))
        