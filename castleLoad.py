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
dialogue = True
orcy = 500
orc1 = orcSpawn.OrcSpawn(0, orcy, 250, 1.1, True)
orc2 = orcSpawn.OrcSpawn(30, orcy, 250, 0.9, True)
orc3 = orcSpawn.OrcSpawn(90, orcy, 250, 2.2, True)
orc4 = orcSpawn.OrcSpawn(750, orcy, 250, 0.6, True)
orc5 = orcSpawn.OrcSpawn(200, orcy, 250, 1.1, True)
orc6 = orcSpawn.OrcSpawn(11, orcy, 250, 2.1, True)
orc7 = orcSpawn.OrcSpawn(650, orcy, 250, 1.6, True)
orc8 = orcSpawn.OrcSpawn(550, orcy, 250, 1.8, True)
orc9 = orcSpawn.OrcSpawn(221, orcy, 250, 1.2, True)
orc10 = orcSpawn.OrcSpawn(112, orcy, 250, 1.9, True)

orc_List = [orc1, orc2, orc3, orc4, orc5, orc6, orc7, orc8, orc9, orc10]

orcspawn1 = False
orcspawn2 = False
orcspawn3 = False
orcspawn4 = False
orcspawn5 = False
orcspawn6 = False
orcspawn7 = False
orcspawn8 = False
orcspawn9 = False
orcspawn10 = False

allDead = False
spawnAll = False

stage1Spawned = False
stage2Spawned = False
stage3Spawned = False
stage4Spawned = False
stage5Spawned = False
stage6Spawned = False
stage7Spawned = False


message1 = [
    'Larry is About to transform into his final form',
    'he has transformed',
    'he used a teleportation trick to send u to his castle',
    'you have been teleported to is castle'
]

message2 = [
    'you have entered his castle',
    'this castle if full of orc souls',
    'the souls are trapped in here as well',
    'the orcs are mind controlled ',
    'if orcs die they respawn again and again',
    'the orc souls are trapped beause of a crystal',
    'find that crystal and destroy it ',
    'and free the orcs from this misery'
    
]

message3 = [
    'the crystal has been destroyed',
    'without the crystal',
    'this castle is collapsing',
    'the dimention is destroyed',
    'you have been teleported back to orc dimntion',

]
messageIndex = 0
currentMessage = message1[messageIndex]
orbital = True
stab = True
stabbyCounter = 0
movement = True
backgroundState = 'back7'
gameFont = pygame.font.Font(None, 36)
currentSection = 'Castle1'
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
                if currentSection == 'Castle1' and messageIndex > 3:
                    currentSection = 'Castle2'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    backgroundState = 'Castle1'
                    player.x = 400
                    player.y = 500
                if currentSection == 'Castle2' and messageIndex > 7:
                    currentSection = 'Castle3'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    
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

    if spawnAll == True:
        orcspawn1 = True
        orcspawn2 = True
        orcspawn3 = True
        orcspawn4 = True
        orcspawn5 = True
        orcspawn6 = True
        orcspawn7 = True
        orcspawn8 = True
        orcspawn9 = True
        orcspawn10 = True
        spawnAll = False

    if backgroundState == 'Castle1' and stage1Spawned == False:
        spawnAll = True
        stage1Spawned = True
    if backgroundState == 'Castle2' and stage2Spawned == False:
        spawnAll = True
        stage1Spawned = True
    if backgroundState == 'Castle3' and stage3Spawned == False:
        spawnAll = True
        stage1Spawned = True
    if backgroundState == 'Castle4' and stage4Spawned == False:
        spawnAll = True
        stage1Spawned = True
    if backgroundState == 'Castle5' and stage5Spawned == False:
        spawnAll = True
        stage1Spawned = True

    if orcspawn1 == False and orcspawn2 == False and orcspawn3 == False and orcspawn4 == False and orcspawn5 == False and orcspawn6 == False and orcspawn7 == False and orcspawn8 == False and orcspawn9 == False and orcspawn10 == False:
        allDead = True

    if orcspawn1 == True or orcspawn2 == True or orcspawn3 == True or orcspawn4 == True or orcspawn5 == True or orcspawn6 == True or orcspawn7 == True or orcspawn8 == True or orcspawn9 == True or orcspawn10 == True:
        allDead = False

    if currentSection == 'Castle1':
        currentMessage = message1[messageIndex]
    if currentSection == 'Castle2':
        currentMessage = message2[messageIndex]
    if currentSection == 'Castl3':
        currentMessage = message3[messageIndex]
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

    print(player.x, player.y)
    
    key = pygame.key.get_pressed()
    text = gameFont.render(f"Health: {player.health}", True, (255, 255, 255))

    backgroundDraw = bg.draw(screen, backgroundState)

    if movement == True:
        player.move(key, backgroundState)
        player.playerDirection(key)

    if player.health <= 0:
        Dead = True

    if backgroundState == 'back1':
        if player.x > 750:
            player.x - 750
        if player.x < 0:
            player.x = 0
    if backgroundState == 'Castle1':
        if player.x > 750:
            player.x = 750
        if allDead == True:
            if player.x < 0:
                player.x = 750
                backgroundState = 'Castle2'
        if allDead == False:
            if player.x < 0:
                player.x = 0
    if backgroundState == 'Castle2':
        if allDead == True:
            if player.x > 750:
                player.x = 0
                backgroundState = 'Castle1'
            if player.x < 0:
                player.x = 750
                backgroundState = 'Castle3'
        if allDead == False:
            if player.x > 750:
                player.x = 750
            if player.x < 0:
                player.x = 0
    if backgroundState == 'Castle3':
        if player.x < 0:
            player.x = 0
        if player.x > 750:
            player.x = 0
            backgroundState = 'Castle2'
    if player.y >= 680 and backgroundState == 'Castle3':
        player.y = 0
        player.x = 750
        backgroundState = 'Castle4'

    if backgroundState == 'Castle4':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            backgroundState = 'Castle5'
            player.x = 750
    if backgroundState == 'Castle5' or backgroundState == 'Castle6':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0

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
            if key[pygame.K_s]:
                Weapons.rod()

    player.playerDisplay(screen)
    Weapons.draw(screen, player)

    if orcspawn1 == True:
        orc1.orcAi(player, True)
        orc1.attack(player, True)
        orc1.draw(screen)
    if orcspawn2 == True:
        orc2.orcAi(player, True)
        orc2.attack(player, True)
        orc2.draw(screen)
    if orcspawn3 == True:
        orc3.orcAi(player, True)
        orc3.attack(player, True)
        orc3.draw(screen)
    if orcspawn4 == True:
        orc4.orcAi(player, True)
        orc4.attack(player, True)
        orc4.draw(screen)
    if orcspawn5 == True:
        orc5.orcAi(player, True)
        orc5.attack(player, True)
        orc5.draw(screen)
    if orcspawn6 == True:
        orc6.orcAi(player, True)
        orc6.attack(player, True)
        orc6.draw(screen)
    if orcspawn7 == True:
        orc7.orcAi(player, True)
        orc7.attack(player, True)
        orc7.draw(screen)
    if orcspawn8 == True:
        orc8.orcAi(player, True)
        orc8.attack(player, True)
        orc8.draw(screen)
    if orcspawn9 == True:
        orc9.orcAi(player, True)
        orc9.attack(player, True)
        orc9.draw(screen)
    if orcspawn10 == True:
        orc10.orcAi(player, True)
        orc10.attack(player, True)
        orc10.draw(screen)

    if orc1.health <= 0:
        orcspawn1 = False
    if orc2.health <= 0:
        orcspawn2 = False
    if orc3.health <= 0:
        orcspawn3 = False
    if orc4.health <= 0:
        orcspawn4 = False
    if orc5.health <= 0:
        orcspawn5 = False
    if orc6.health <= 0:
        orcspawn6 = False
    if orc7.health <= 0:
        orcspawn7 = False
    if orc8.health <= 0:
        orcspawn8 = False
    if orc9.health <= 0:
        orcspawn9 = False
    if orc10.health <= 0:
        orcspawn10 = False

    print(orc1.health)

    if dialogue == True:
        screen.blit(dialogueBox, (50, 510))
        textSurface = gameFont.render(currentMessage, True, (255, 255, 255))
        screen.blit(textSurface, (80, 535))

    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60) 
        