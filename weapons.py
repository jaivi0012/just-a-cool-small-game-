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
        self.stabnuke = True
        self.stabStarted = True
        self.stabCounter = 0
        self.stabCycle = 0
        self.explodeY = 0
        self.stabActive = False
        self.stabIndex = 0
        self.stabTimer = 0
        self.stabPoints = []
        self.stabDistance = 120
        self.stabSpacing = 90
        self.stabDamage = 70
        self.stabRange = 500
        maceImg = pygame.image.load('mace.png').convert_alpha()
        spearImg = pygame.image.load('Diamond_Spear.png').convert_alpha()
        rodImg = pygame.image.load('Fishing_Rod.png').convert_alpha()
        self.maceSfx = pygame.mixer.Sound('Sounds/mace.wav')
        self.damageSfx = pygame.mixer.Sound('Sounds/damage.wav')
        self.lungeSfx = pygame.mixer.Sound('Sounds/spear.wav')
        self.tntSfx = pygame.mixer.Sound('Sounds/tntExplode.wav')
        self.stabSfx = pygame.mixer.Sound('Sounds/stab.wav')
       
        self.mace_right = pygame.transform.scale(maceImg, (30, 30))
        self.mace_left = pygame.transform.flip(self.mace_right, True, False)
        
        self.spear_right = pygame.transform.scale(spearImg, (30, 30))
        self.spear_left = pygame.transform.flip(self.spear_right, True, False)
        
        self.rod_right = pygame.transform.scale(rodImg, (30, 30))
        self.rod_left = pygame.transform.flip(self.rod_right, True, False)

        self.maceRect = pygame.Rect(player.x + 25,player.y + 46,20,80)
        self.maceDamage = None
        self.facing_direction = player.Direction
        self.tntAnimD = False
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
        self.tntExplode = [
            pygame.image.load('tntExplode/tnt1.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt2.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt3.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt4.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt5.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt6.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt7.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt8.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt9.png').convert_alpha(),
            pygame.image.load('tntExplode/tnt10.png').convert_alpha()
        ]
        self.tntExplodeSpeed = 4
        self.tntIndex = 0
        self.tntCounter = 0
        self.tntAnim = [pygame.transform.scale(img, (200, 100)) for img in self.tntExplode]
        self.tntDraw = None
        self.scaledTnt = [pygame.transform.scale(img, (30, 30)) for img in self.tnt]
    
        self.tntX = [0, 90, 180, 270, 360, 450, 540, 630, 720]
        self.tntY = 0

        self.currentImg = self.mace_right
        self.maceU = False
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
                self.tntAnimD = True
                self.explodeY = self.tntY       
                self.tntIndex = 0
                self.tntCounter = 0
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

        if self.tntAnimD == True:
            self.tntDraw = self.tntAnim[self.tntIndex]
            self.tntCounter += 1
            if self.tntCounter >= self.tntExplodeSpeed:
                self.tntIndex += 1
                self.tntCounter = 0
            if self.tntIndex > 9:
                self.tntAnimD = False
                self.tntIndex = 0

        if self.stabActive == True:
            self.stabTimer += 1
            if self.stabTimer >= self.tntExplodeSpeed:
                self.stabTimer = 0
                self.stabIndex += 1
                if self.stabIndex >= len(self.tntAnim):
                    self.stabActive = False
                    self.stabIndex = 0

            
    def mace(self, orc_List, player):
        self.currentWeapon = 'mace'
        fallspeed = max(player.y_velocity, 0)      
        bounced = False

        for orc in orc_List:
            if orc.health <= 0:                   
                continue
            if self.maceRect.colliderect(orc.orcRect):
                maceDamage = 0
                self.maceU = False
                if fallspeed > 0:
                    maceDamage = 10 + fallspeed * 4
                    if bounced == False:          
                        player.y_velocity = self.maceJump
                        self.maceSfx.play()
                        bounced = True

                if fallspeed == 0 and player.y >= 490:
                    maceDamage = 20
                    self.damageSfx.play()

                orc.health -= maceDamage

                if player.Direction == 'Left':
                    orc.orcVelocityX -= self.Knockback 
                if player.Direction == 'Right':
                    orc.orcVelocityX += self.Knockback 

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
        self.tntSfx.play()

    def stabShot(self, orc_List, player):

        self.currentWeapon = 'rod'

       
        target = None
        bestDistance = self.stabRange
        for orc in orc_List:
            if orc.health <= 0 or orc.ox < 0 or orc.ox > 750:
                continue
            distance = abs((orc.ox + 35) - (player.x + 35))
            if distance < bestDistance:
                bestDistance = distance
                target = orc

        if target != None:
            centreX = target.ox + 35          
            y = target.oy + 35                 
        else:                                
            if player.Direction == 'Right':
                centreX = player.x + 35 + self.stabDistance
            else:
                centreX = player.x + 35 - self.stabDistance
            y = 545

        self.stabPoints = []
        while y > -40:                        
            self.stabPoints.append((centreX, y))
            y -= self.stabSpacing

        self.stabActive = True                 
        self.stabIndex = 0
        self.stabTimer = 0
        self.stabSfx.play()

        for orc in orc_List:                  
            for (px, py) in self.stabPoints:
                if math.sqrt((orc.ox + 35 - px) ** 2 + (orc.oy + 35 - py) ** 2) < 65:
                    orc.health -= self.stabDamage + 200
                    break
    
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

        # orbital explosion (the horizontal row)
        if self.tntAnimD == True and self.tntDraw != None:
            for x in self.tntX:
                px = x + 15 - self.tntDraw.get_width() // 2
                py = self.explodeY + 15 - self.tntDraw.get_height() // 2
                screen.blit(self.tntDraw, (px, py))

      
        if self.stabActive == True:
            frame = self.tntAnim[self.stabIndex]
            for (px, py) in self.stabPoints:
                screen.blit(frame, (px - frame.get_width() // 2, py - frame.get_height() // 2))

        if player.Direction == 'Right':
            screen.blit(self.currentImg, (player.x + 51, player.y + 16))
        if player.Direction == 'Left':
            screen.blit(self.currentImg, (player.x - 13, player.y + 16))

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
        