import pygame
import math


class ramAltman:
    PLAYER_THRESHOLDS = [2500, 2000, 1500, 1000, 650, 300]
    BOSS_TRIGGERS = {
    'tar1': 25000,
    'tar2': 20000,
    'tar3': 15000,
    'tar4': 10000,
    'tar5': 5000,
    'tar6': 1000,
    'tar7': 500,
}

    GROUND_Y = 400
    MUSIC_DELAY_FRAMES = 1075
    GROUND_MIN_FRAMES = 120 
    GROUND_MIN_FRAMES = 120
    GROUND_MAX_FRAMES = 600            
    GROUND_DAMAGE_TO_ASCEND = 1500
    def __init__(self, ox, oy, move, width, height):
        self.ox = ox
        self.oy = oy
        self.width = width
        self.height = height
        self.move = move
        self.oldx = ox

        self.health = 30000
        self.punchDamage = 45
        self.punched = False
        self.punchCounter = 0
        self.speed = 3
        self.accel = 0
        self.friction = 0.9
        self.orcVelocityX = 0
        self.orcVelocityY = 0
        self.Direction = 'Right'
        self.attack = False
        self.dead = True

        self.state = 'ASCEND'
        self.target = 'tar1'
        self.ascended_for = set()
        self.groundFrames = 0
        self.groundFrames = 0
        self.landHealth = self.health

        self.skyfall = False
        self.ramfall = False
        self.Ascend = True
        self.otherAttack = False

        self.LineCounter = 0
        self.skyfall_music_started = False
        self.DialougeBeg = False
        self.musichasplayed = False

        self.AltmanIdle = pygame.image.load('Ram_Altman.png').convert_alpha()
        # self.AltmanArmSpread = pygame.image.load('').convert_alpha()
        self.AltmanScaled = pygame.transform.scale(self.AltmanIdle, (width, height))
        self.AltmanDraw = self.AltmanScaled
        self.orcRect = pygame.Rect(ox, oy, width, height)


    def _approach(self, pos, vel, target):
    
        f = self.friction
        accel = self.speed * (1 - f)         
        max_v = self.speed * f             
        
        desired = max(-max_v, min(max_v, (target - pos) * (1 - f) / f))
        thrust = max(-accel, min(accel, desired - vel))
        return vel + thrust

    def _steer(self, tx, ty):
        self.orcVelocityX = self._approach(self.ox, self.orcVelocityX, tx)
        self.orcVelocityY = self._approach(self.oy, self.orcVelocityY, ty)

    def _apply_velocity(self):
        
        self.orcVelocityX *= self.friction
        self.orcVelocityY *= self.friction
        self.ox += self.orcVelocityX
        self.oy += self.orcVelocityY

        if self.ox < 0:
            self.ox = 0
            self.orcVelocityX = 0
        if self.ox > 800 - self.width:
            self.ox = 800 - self.width
            self.orcVelocityX = 0

    def _player_phase(self, hp):
        return sum(1 for t in self.PLAYER_THRESHOLDS if hp <= t)


    def movement(self, targetx, hostility):
        if hostility == False:
            self.accel = self.speed * (1 - self.friction)

            if self.ox + 2 > targetx:
                self.orcVelocityX -= self.accel

            if self.ox - 2 < targetx:
                self.orcVelocityX += self.accel

            self.orcVelocityX *= self.friction
            self.ox += self.orcVelocityX

    def smartMove(self, player, hostility):

        if self.otherAttack == True and hostility == True:
            accel = self.speed * (1 - self.friction)
            playerCentre = player.x + 35
            bossCentre = self.ox + self.width / 2
            distance = playerCentre - bossCentre

            playerInAir = player.y < 480
            playerAbove = playerInAir and abs(distance) < 140

            if playerAbove:
                direction = -1 if distance > 0 else 1

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

    def SkyFall(self, targetx, targety, ramfallin, player):
       # print(self.state, self.target, int(self.health), player.health, round(self.oy), self.groundFrames)
        distance = math.hypot(targetx - self.ox, targety - self.oy)

        if not self.musichasplayed:
            if distance < 10 and not self.DialougeBeg:
                Line = pygame.mixer.Sound("Sounds/SamAltmanVoiceLine.wav")
                Line.set_volume(0.5)
                Line.play()
                self.DialougeBeg = True

        if not self.musichasplayed:
            if ramfallin and not self.skyfall_music_started:
                self.LineCounter += 1
                if self.LineCounter > self.MUSIC_DELAY_FRAMES:
                    self.LineCounter = 0
                    self.ramfall = True
                    self.skyfall_music_started = True
                    pygame.mixer.music.load("Sounds/skyfall2.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(loops=-1)
                    self.musichasplayed = True

        if player.health > 0:
            new_target = f'tar{self._player_phase(player.health) + 1}'
            if new_target != self.target:
                self.target = new_target
                self.ramfall = False
                self.skyfall = False
                if self.state in ('ASCEND', 'HOVER'):
                    self.state = 'DESCEND'

        if self.state == 'ASCEND':
            self._steer(targetx, targety)
            if distance < 20:
                self.state = 'HOVER'

        elif self.state == 'HOVER':
            self._steer(targetx, targety)
            if self.ramfall:
                self.skyfall = True

        elif self.state == 'DESCEND':
            self._steer(targetx, self.GROUND_Y)
            if math.hypot(targetx - self.ox, self.GROUND_Y - self.oy) < 30:
                self.state = 'GROUND'
                self.groundFrames = 0
                self.landHealth = self.health

        elif self.state == 'GROUND':
            self.orcVelocityY = self._approach(self.oy, self.orcVelocityY, self.GROUND_Y)
            self.groundFrames += 1

            trigger = self.BOSS_TRIGGERS.get(self.target)
            below_trigger = trigger is not None and self.health <= trigger
            hurt_enough = (self.landHealth - self.health) >= self.GROUND_DAMAGE_TO_ASCEND
            timed_out = self.groundFrames >= self.GROUND_MAX_FRAMES

            if (self.health > 0
                    and self.groundFrames >= self.GROUND_MIN_FRAMES
                    and (below_trigger or hurt_enough or timed_out)):
                self.ramfall = True
                self.skyfall = False
                self.state = 'ASCEND'


        if self.health <= 0:
            self.skyfall = False

        self.Ascend = self.state in ('ASCEND', 'HOVER')
        self.otherAttack = (self.state == 'GROUND')

        self._apply_velocity()

    def powerPunch(self, player):
        if self.otherAttack == True:
            if self.orcRect.colliderect(player.playerRect) and self.punched == False:
                player.health -= self.punchDamage
                self.punched = True
        if self.punched == True:
            self.punchCounter += 1
            if self.punchCounter > 60:
                self.punched = False
                self.punchCounter = 0


    def update(self):
        self.orcRect = pygame.Rect(self.ox, self.oy, self.width, self.height)
        self.oldx = self.ox

        if self.orcVelocityX < -0.1:
            self.Direction = 'Left'
        elif self.orcVelocityX > 0.1:
            self.Direction = 'Right'

    def restrict(self):
        if self.ox > 800 - self.width:
            self.ox = 800 - self.width
        if self.ox < 0:
            self.ox = 0

    def draw(self, screen, font):
        screen.blit(self.AltmanDraw, (self.ox, self.oy))
       # pygame.draw.rect(screen, (0, 255, 0), self.orcRect, 2)

        text = font.render(f"Ram Altman: {max(0, int(self.health))}", True, (255, 255, 255))
        screen.blit(text, (800 - text.get_width() - 20, 20))