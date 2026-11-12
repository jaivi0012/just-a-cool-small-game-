import pygame
import sys, os

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
import playerLogic
import weapons
import orcSpawn
import backgroundLoader


pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = backgroundLoader.background()
backgroundDraw = None
player = playerLogic.Player(0, 500)   
Weapons = weapons.Weapons(player)
Running = True
stabby = False
orc_List = []
Dead = False
lunge = True
attack = False
lungeCounter = 0
change = False
dialogue = False
currentMessage = None
orbital = True
stab = True
stabbyCounter = 0
movement = True
backgroundState = 'back7'
gameFont = pygame.font.Font(None, 36)
messageIndex = 0
currentSection = 'Castle'
text = None
maceCounter = 0
dialogueBox = pygame.image.load('dialogueBox.png').convert_alpha()

while Running:
    events = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and dialogue == True:
                messageIndex += 1

            if movement == True:                  
                if event.key == pygame.K_SPACE:
                    player.jump()  
                if event.key == pygame.K_a:
                    lunge = True
                    attack = True
                if event.key == pygame.K_d and maceCounter == 0:
                    Weapons.maceU = True
                if stab == True:
                    if event.key == pygame.K_w and stabby == False:
                        Weapons.stabShot(orc_List, player)
                        stabby = True
    screen.fill((0, 0, 0))
    if stabby == True:
        stabbyCounter += 1
        if stabbyCounter > 25:
            stabby = False
            stabbyCounter = 0
    if Weapons.maceU == True:
    
        Weapons.mace(orc_List, player)
        maceCounter += 1
        if maceCounter >= 13 or Weapons.maceU == False: 
            Weapons.maceU = False
            maceCounter = 0
    
    
    key = pygame.key.get_pressed()
    text = gameFont.render(f"Health: {player.health}", True, (255, 255, 255))

    backgroundDraw = bg.draw(screen, backgroundState)

    if movement == True:
        player.move(key, backgroundState)
        player.playerDirection(key)

    if player.health <= 0:
        Dead = True


    Weapons.update(player, orc_List)
    if dialogue == True:
            movement = False
        
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
    if backgroundState in ('back1', 'back2') and player.x < 0:
        player.x = 0
    player.playerUpdate()
    if movement == True:
        if orbital == True:
            if key[pygame.K_s]:
                Weapons.rod()

    player.playerDisplay(screen)
    Weapons.draw(screen, player)

    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60) 
        