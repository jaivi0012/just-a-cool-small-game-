import pygame
import sys, os

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
import playerLogic
import weapons
import backgroundLoader
import rain
import ramShower
import RamAltman
import AiEnemy

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(100000)
screen = pygame.display.set_mode((800, 600))
rain_sound = pygame.mixer.Sound("Sounds/rain.ogg")
clock = pygame.time.Clock()
bg = backgroundLoader.background()
move = False
ramThiefSpawn = False
ramThiefHasSpawned = False
RamThief = RamAltman.ramAltman(20, 400, move, 65, 175)
backgroundDraw = None
player = playerLogic.Player(0, 500)  
ram_Shower = ramShower.RamShower(800, 600, obj_amount=30, size=(50, 60)) 
Weapons = weapons.Weapons(player)
rain = rain.RainSystem(800, 600)
portalRect = pygame.Rect(350, 425, 100, 150)
hostility = True
messageIndex = 0
RamAttack = False
AltmanAttack = False
AltmanHasSpawned = False
rainSound = True
Running = True
stabby = False
Rain = False
orc_List = []
Dead = False
lunge = True
attack = False
ramRain = False
lungeCounter = 0
change = False
dialogue = True
orbital = True
downwardLunge = True
stab = True
stabbyCounter = 0
movement = True
bgChange = True
aiRestriction = False
backgroundState = 'Mountain10'
gameFont = pygame.font.Font(None, 36)
currentSection = 'Message1'
text = None
maceCounter = 0
dialogueBox = pygame.image.load('dialogueBox.png').convert_alpha()
castleMusic = False
allDead = False
portalAppear = False

message1 = [
    'The Data centre has been destroyed',
    'and it has disappeared',
    'a portal has appeared in its place',
    'ENTER THE PORTAL'
]

message2 = [
    'That portl led u bac down the mountain',
    'u should go back',
    'but there is no one to give u directions',
    'lets just move right',
    'cant be that bad',
    'Right?',
    'Righttt....????'
]

currentMessage = message1[messageIndex]

while Running:
    events = None
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and dialogue == True:
                messageIndex += 1
                if currentSection == 'Message1' and messageIndex > 3:
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    portalAppear = True
                    currentSection = 'Message2'
                   # print(messageIndex)
                if currentSection == 'Message2' and messageIndex > 6:
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    currentSection = 'Message3'
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
                if event.key == pygame.K_e and downwardLunge == True and player.y < 500:
                    Weapons.downwardLunge(player)
                    downwardLunge = False
    screen.fill((0, 0, 0))    
    if dialogue == True and currentSection == 'Message1':
        currentMessage = message1[messageIndex]  
    if dialogue == True and currentSection == 'Message2':
        currentMessage = message2[messageIndex]
    if stabby == True:
        stabbyCounter += 1  
        if stabbyCounter > 25:
            stabby = False
            stabbyCounter = 0
    if Weapons.maceU == True:
    
        Weapons.mace(orc_List, player)
        maceCounter += 1
        downwardLunge = True
        if maceCounter >= 13 or Weapons.maceU == False: 
            Weapons.maceU = False
            maceCounter = 0
    
    key = pygame.key.get_pressed()
    text = gameFont.render(f"Health: {player.health}", True, (255, 255, 255))

    backgroundDraw = bg.draw(screen, backgroundState)

    if portalAppear == True:
        if player.playerRect.colliderect(portalRect):
            player.x = 750
            backgroundState = 'Mountain1'
            portalAppear = False
            dialogue = True

    if movement == True:
        player.move(key, backgroundState)
        player.playerDirection(key)

    if player.health <= 0:
        Dead = True
    if Dead == True:
        pass
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

    player.playerUpdate()
    if movement == True:
        if orbital == True:
            if key[pygame.K_s] and Weapons.orbitalStarted != True:
                Weapons.rod()
            if key[pygame.K_q]:
                Weapons.stabShot(orc_List, player)
    
    if Weapons.orbitalStarted == True:
        bgChange = False
    if Weapons.orbitalStarted == False and ramThiefSpawn == False:
        bgChange = True
    
    if portalAppear == True:
        pygame.draw.rect(screen, (0, 255, 0), portalRect, 2)
    
    bg.collision(backgroundState, player)
    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    

    if dialogue == True:
            screen.blit(dialogueBox, (50, 510))
            textSurface = gameFont.render(currentMessage, True, (255, 255, 255))
            screen.blit(textSurface, (80, 535))

    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60)