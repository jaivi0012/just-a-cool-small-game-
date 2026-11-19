import pygame
import random
import math


class RamShower:

  def __init__(self, width, height, obj_amount=25, size=(48, 24)):
    self.width = width
    self.height = height
    self.obj_amount = obj_amount
    self.explode = pygame.mixer.Sound('Sounds/stab.wav')
    self.animspeed = 4
    self.animIndex = 0
    self.animCounter = 0
    self.explosions = []
    self.boom = [
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
    self.explodeAnim = [pygame.transform.scale(img, (100, 50)) for img in self.boom]
    self.explodeDraw = self.explodeAnim[self.animCounter]
    self.explode.set_volume(0.4)
    raw_ram = pygame.image.load("ram.png").convert_alpha()
    self.ram_img = pygame.transform.scale(raw_ram, size)
    self.ram_width = self.ram_img.get_width()
    self.ram_height = self.ram_img.get_height()

    
    self.sticks = [self._create_stick(random_y=True) for _ in range(self.obj_amount)]

  def _create_stick(self, random_y=False):
    x = random.randint(0, max(0, self.width - self.ram_width))
    y = (
        random.randint(-self.height, -self.ram_height)
        if random_y
        else random.randint(-120, -self.ram_height)
    )
    speed = random.randint(4, 11)
    return {"x": x, "y": y, "speed": speed, "trail": []}

  def update(self, player):
    for stick in self.sticks:
        stick["y"] += stick["speed"]

        
        center = (
            stick["x"] + self.ram_width / 2,
            stick["y"] + self.ram_height / 2,
        )
        stick["trail"].append(center)
        stick["trail"] = stick["trail"][-12:]

        if stick["y"] > 500:
            x = player.x + 15
            y = player.y + 15
            stick_cx = stick["x"] + self.ram_width / 2
            stick_cy = stick["y"] + self.ram_height / 2
            distance = math.hypot(x - stick_cx, y - stick_cy)
            damage = 0
            if distance < 20:
                damage = 100
            if distance < 80 and distance > 20:
                damage = 40

            player.health -= damage
            self.explode.play()
            damage = 0   
            self.anim = True

            self.explosions.append({
                "x": stick_cx - 50,  
                "y": stick_cy - 25, 
                "index": 0,
                "counter": 0,
            })
        
            respawned = self._create_stick(random_y=False)
            stick["x"] = respawned["x"]
            stick["y"] = respawned["y"]
            stick["speed"] = respawned["speed"]
            stick["trail"] = []
    for exp in self.explosions[:]:
        exp["counter"] += 1
        if exp["counter"] > self.animspeed:
            exp["counter"] = 0
            exp["index"] += 1

        if exp["index"] >= len(self.explodeAnim):
            self.explosions.remove(exp)
                            

  def draw(self, screen):
    for stick in self.sticks:
        if stick["y"] > 500:
            continue

        trail = stick["trail"]
        for i in range(len(trail) - 1):
            thickness = max(1, (i + 1) * 1)
            pygame.draw.line(
                screen, (255, 255, 255), trail[i], trail[i + 1], thickness
            )
        screen.blit(self.ram_img, (stick["x"], stick["y"]))
    for exp in self.explosions:
        screen.blit(self.explodeAnim[exp["index"]], (exp["x"], exp["y"]))