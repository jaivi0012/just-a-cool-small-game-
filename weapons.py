import pygame


class Weapons:
    def __init__(self, player):
        self.currentWeapon = 'mace'
        self.maceJump = -25
        self.maceCounter = 0
        self.Knockback = 20
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

        self.currentImg = self.mace_right

    def update(self, player):
        self.maceRect = pygame.Rect(player.x + 25,player.y + 45,20,80)

    def mace(self, orc, player):
        maceDamage = 0
        self.currentWeapon = 'mace'
        fallspeed = max(player.y_velocity, 0)
        if self.maceRect.colliderect(orc.orcRect):
            if fallspeed > 0:
                maceDamage = 10 + fallspeed * 3
                player.y_velocity = self.maceJump
                self.maceSfx.play()

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
        pygame.draw.rect(screen, (0, 255, 0), self.maceRect, 2)