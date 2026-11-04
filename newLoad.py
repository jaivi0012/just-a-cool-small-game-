import pygame
import sys, os

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
import playerLogic
import weapons
import orcSpawn


pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
player = playerLogic.Player(0, 500)   
Weapons = weapons.Weapons(player)
Running = True
orc1 = orcSpawn.OrcSpawn(700, 500, 250)
orc1spawn = True
lunge = False
attack = False
lungeCounter = 0

while Running:
    events = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()  
            if event.key == pygame.K_a:
                lunge = True
                attack = True
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    player.move(key)
    player.playerDirection(key)
    Weapons.update(player)
    if key[pygame.K_d]:
        Weapons.mace(orc1, player)
    
    if lunge == True and attack == True:
        lunge = False
        lungeCounter = 0
        Weapons.spear(player)  

    
    if lunge == False:
        lungeCounter += 1
        Power = 20  
        
        if player.Direction == 'Right':
            player.x += Power
        if player.Direction == 'Left':
            player.x -= Power

    if lungeCounter >= 4:
        lunge = True
        lungeCounter = 0
        attack = False
   
    if key[pygame.K_s]:
        Weapons.rod()
    if orc1spawn == True:
        orc1.orcAi(player, True)
    if orc1.health <= 0:
        orc1spawn = False

    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    if orc1spawn == True:
        orc1.draw(screen)
    pygame.display.flip()  
    clock.tick(60) 
    