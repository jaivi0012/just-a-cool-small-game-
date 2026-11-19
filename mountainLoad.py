import pygame
import sys, os

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
import playerLogic
import weapons
import orcSpawn
import pumpkinBoss
import backgroundLoader
import orcBoss
import rain
import ramShower

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(100000)
screen = pygame.display.set_mode((800, 600))
rain_sound = pygame.mixer.Sound("Sounds/rain.ogg")
clock = pygame.time.Clock()
bg = backgroundLoader.background()
backgroundDraw = None
player = playerLogic.Player(0, 500)  
ram_Shower = ramShower.RamShower(800, 600, obj_amount=30, size=(50, 60)) 
Weapons = weapons.Weapons(player)
rain = rain.RainSystem(800, 600)
message1 = [
    'orcKing :- thanks for helping me defeat larry',
    'orcKing :- it was indeed unexpected to see larry',
    'orcKing :- i wonder what he was doing out here',
    'orcKing :- but larry is not the main focus',
    'orcKing :- he just showed up unepectedly',
    'orcKing :- you may be wondering why u cant see me',
    'orcKing :- thats because im getting weaker',
    'orcKing :- let me explain',
    'orcKing :- there is a person called',
    'orcKing :- Ram Altman',
    'orcKing :- he has created a pendemic type situation',
    'orcKing :- called RAMageddon',
    'orcKing :- basically we orcs need ',
    'orcKing :- ram to survive',
    'orcKing :- its food for us',
    'orcKing :- but Ram Altman is hoarding all the RAM',
    'orcKing :- without ram we orcs grow weaker ',
    'orcKing :- his power level is unknown',
    'orcKing :- he lives on the peak of a mountain',
    'orcKing :- i can teleport you to that mountain',
    'orcKing :- be careful he is rumored to be strong',
    'orcKing :- little one ',
    'orcKing :- be careful ',
    'YOU ARE GETTING TELEORTED',
    'YOU HAVE BEEN TELEPORTED'
]

message2 = [
    'orcKing :- now that you are at the base of the mountain',
    'orcKing :- you will have to climb it ',
    'orcKing :- be careful this mountain is cursed',
    'orcKing :- when climbing you will have dificulty jumping',
    'orcKing :- once at the top you should be fine',
    'orcKing :- i will not be able to communicate',
    'orcKing :- because im low on energy ',
    'orcKing :- if u get some ram',
    'orcKing :- you have to give it to me as a offering',
    'orcKing :- and then eat it yourself',
    'orcKing :- then ill be able to appear',
    'orcKing :- and be careful of Ram Altman',
    'orcKing :- goodluck',
    'orcKing :- little one...'
]


messageIndex = 0
currentMessage = message1[messageIndex]
rainSound = True
Running = True
stabby = False
Rain = False
orc_List = []
Dead = False
lunge = True
attack = False
ramRain = True
lungeCounter = 0
change = False
dialogue = True
orbital = True
downwardLunge = True
stab = True
stabbyCounter = 0
movement = True
bgChange = True
backgroundState = 'back6'
gameFont = pygame.font.Font(None, 36)
currentSection = 'Mountain1'
text = None
maceCounter = 0
dialogueBox = pygame.image.load('dialogueBox.png').convert_alpha()
castleMusic = False
while Running:
    events = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and dialogue == True:
                messageIndex += 1
                if currentSection == 'Mountain1' and messageIndex > 24:
                    messageIndex = 0
                    currentSection = 'Mountain2' 
                    dialogue = False
                    backgroundState = 'Mountain1'
                    movement = True
                    player.x = 520
                if currentSection == 'Mountain2' and messageIndex > 13:
                    messageIndex = 0
                    currentSection = 'Mountain3'
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

                if event.key == pygame.K_e and downwardLunge == True and player.y < 500:
                    Weapons.downwardLunge(player)
                    downwardLunge = False
                    
    screen.fill((0, 0, 0))
    print(player.x, player.y)
    print(clock)
    if currentSection == 'Mountain1' and dialogue == True:
        currentMessage = message1[messageIndex]
    if currentSection == 'Mountain2' and dialogue == True:
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
    if Weapons.orbitalStarted == False:
        bgChange = True

    if Rain == True and rainSound == True:
        rain_sound.set_volume(0.4)
        rain_sound.play(loops=-1)
        rainSound = False
    if Rain == False and rainSound == False:
        rain_sound.stop()
        rainSound = True

    if backgroundState == 'Mountain1':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            if bgChange == True:
                backgroundState = 'Mountain2'
                player.x = 750
                player.y = 500
            else:
                player.x = 0
        if currentSection == 'Mountain2':
            dialogue = True
    if backgroundState == 'Mountain2':
        if player.x > 750:
            if bgChange == True:
                backgroundState = 'Mountain1'
                player.x = 0
                player.y = 210
            else:
                player.x = 750
        if player.x < 0:
            if bgChange == True:
                backgroundState = 'Mountain3'
                player.x = 750
                player.y = 500
            else:
                player.x = 0
    if backgroundState == 'Mountain3':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain2'
                    player.x = 0
                    player.y = 260
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain4'
                    player.x = 750
                    player.y = 500
                else:
                    player.x = 0
    if backgroundState == 'Mountain4':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain3'
                    player.x = 0
                    Rain = False
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain5'
                    player.x = 750
                    player.y = 500
                    Rain = True
                else:
                    player.x = 0
    if backgroundState == 'Mountain5':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain4'
                    player.x = 0
                    Rain = False
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain6'
                    player.x = 750
                    player.y = 500
                    Rain = True
                else:
                    player.x = 0
    if backgroundState == 'Mountain6':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain5'
                    player.x = 0
                    Rain = True
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain7'
                    player.x = 750
                    player.y = 500
                    Rain = True
                else:
                    player.x = 0
    if backgroundState == 'Mountain7':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain6'
                    player.x = 0
                    Rain = True
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain8'
                    player.x = 750
                    player.y = 500
                    Rain = True
                else:
                    player.x = 0
    if backgroundState == 'Mountain8':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain7'
                    player.x = 0
                    Rain = True
                else:
                    player.x = 750
            if player.x < 0:
                if bgChange == True:
                    backgroundState = 'Mountain9'
                    player.x = 750
                    Rain = True
                else:
                    player.x = 0
    if backgroundState == 'Mountain9':
            if player.x > 750:
                if bgChange == True:
                    backgroundState = 'Mountain8'
                    player.x = 0
                    Rain = True
                else:
                    player.x = 750
            if player.x < 0:
                player.x = 0

    print(backgroundState)
    bg.collision(backgroundState, player)
    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    if Rain == True: 
        rain.update(screen)

    if ramRain == True:
        ram_Shower.update(player)
        ram_Shower.draw(screen)

    if dialogue == True:
            screen.blit(dialogueBox, (50, 510))
            textSurface = gameFont.render(currentMessage, True, (255, 255, 255))
            screen.blit(textSurface, (80, 535))
    if currentSection == 'goodbye':
        Running = False
    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60)