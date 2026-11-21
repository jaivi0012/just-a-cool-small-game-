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
appended = False
RamThief = RamAltman.ramAltman(20, 400, move, 65, 175)
backgroundDraw = None
player = playerLogic.Player(0, 500)  
ram_Shower = ramShower.RamShower(800, 600, obj_amount=30, size=(50, 60)) 
Weapons = weapons.Weapons(player)
rain = rain.RainSystem(800, 600)
hostility = True
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

message3 = [
    'RamAltman :- So you are the one',
    'RamAltman :- who came to take my ram ',
    'RamAltman :- ive been waiting for you',
    'RamAltman :- my a bots wouldve been enough',
    'RamAltman :- to defeat you',
    'RamAltman :- but its raining so they cant fight',
    'RamAltman :- but i alone should be enough',
    'RamAltman :- be prepeared to face my wrath'
]

message4 = [
    'he has disappeared ',
    'he didnt seem to die',
    'almost as he was teleported',
    'before he died',
    'he has dropped a stick of ram',
    'eat it later',
    'go destroy his data centre',
    'move left to find his data center',
    'destroy it with your orbital strike cannon'
]

messageIndex = 0
currentMessage = message1[messageIndex]

RamAttack = False
AltmanAttack = False

ai1 = AiEnemy.AiEnemy(50, 500, 30, 40, 400, 2.5)
ai2 = AiEnemy.AiEnemy(500, 500, 30, 40, 400, 2.7)
ai3 = AiEnemy.AiEnemy(30, 500, 30, 40, 400, 2.2)
ai4 = AiEnemy.AiEnemy(300, 500, 30, 40, 400, 3.5)
ai5 = AiEnemy.AiEnemy(400, 500, 30, 40, 400, 1.5)
ai6 = AiEnemy.AiEnemy(100, 500, 30, 40, 400, 2.4)
ai7 = AiEnemy.AiEnemy(507, 500, 30, 40, 400, 2.3)
ai8 = AiEnemy.AiEnemy(150, 500, 30, 40, 400, 1.1)
ai9 = AiEnemy.AiEnemy(600, 500, 30, 40, 400, 2.1)
ai10 = AiEnemy.AiEnemy(700, 500, 30, 40, 400, 2.9)
ai11 = AiEnemy.AiEnemy(750, 500, 30, 40, 400, 1.9)
ai12 = AiEnemy.AiEnemy(244, 500, 30, 40, 400, 3.5)
ai13 = AiEnemy.AiEnemy(124, 500, 30, 40, 400, 3.4)
ai14 = AiEnemy.AiEnemy(470, 500, 30, 40, 400, 3.1)
ai15 = AiEnemy.AiEnemy(290, 500, 30, 40, 400, 2.0)
ai16 = AiEnemy.AiEnemy(550, 500, 30, 40, 400, 1.8)
ai17 = AiEnemy.AiEnemy(215, 500, 30, 40, 400, 1.6)
ai18 = AiEnemy.AiEnemy(703, 500, 30, 40, 400, 2.4)
ai19 = AiEnemy.AiEnemy(740, 500, 30, 40, 400, 1.4)
ai20 = AiEnemy.AiEnemy(660, 500, 30, 40, 400, 4.0)

ai1Spawn = False
ai2Spawn = False
ai3Spawn = False
ai4Spawn = False
ai5Spawn = False
ai6Spawn = False
ai7Spawn = False
ai8Spawn = False
ai9Spawn = False
ai10Spawn = False
ai11Spawn = False
ai12Spawn = False
ai13Spawn = False
ai14Spawn = False
ai15Spawn = False
ai16Spawn = False
ai17Spawn = False
ai18Spawn = False
ai19Spawn = False
ai20Spawn = False

AiSpawnAll = False

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
orbital = False
downwardLunge = True
stab = False
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
                if currentSection == 'Mountain3' and messageIndex > 7:
                    messageIndex = 0
                    currentSection = 'Mountain4'
                    dialogue = False
                    movement = True
                    RamAttack = True
                if currentSection == 'Mountain4'and messageIndex > 8:
                    messageIndex = 0
                    currentSection = 'Mountain5'
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
   # print(player.x, player.y)
   # print(clock)
   # print(RamThief.target)
   # print(RamThief.health)
   # print(RamThief.Direction)
   # print(RamThief.Ascend)
   # print(RamThief.otherAttack)
    
    if currentSection == 'Mountain1' and dialogue == True:
        currentMessage = message1[messageIndex]
    if currentSection == 'Mountain2' and dialogue == True:
        currentMessage = message2[messageIndex]
    if currentSection == 'Mountain3' and dialogue == True:
        currentMessage = message3[messageIndex]
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
    if Weapons.orbitalStarted == False and ramThiefSpawn == False:
        bgChange = True

    if RamThief.skyfall == True:
        ramRain = True
    if RamThief.skyfall == False:
        ramRain = False

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

    if backgroundState == 'Mountain8' and ramThiefSpawn == True and bgChange == True:
        bgChange = False

    if AiSpawnAll == True:
        ai1Spawn = True
        ai2Spawn = True
        ai3Spawn = True
        ai4Spawn = True
        ai5Spawn = True
        ai6Spawn = True
        ai7Spawn = True
        ai8Spawn = True
        ai9Spawn = True
        ai10Spawn = True
        ai11Spawn = True
        ai12Spawn = True
        ai13Spawn = True
        ai14Spawn = True
        ai15Spawn = True
        ai16Spawn = True
        ai17Spawn = True
        ai18Spawn = True
        ai19Spawn = True
        ai20Spawn = True
        AiSpawnAll = False
    
    if ai1.health >= 0 and ai1Spawn == True:
        ai1Spawn = False
    if ai2.health >= 0 and ai2Spawn == True:
        ai2Spawn = False
    if ai3.health >= 0 and ai3Spawn == True:
        ai3Spawn = False
    if ai4.health >= 0 and ai4Spawn == True:
        ai4Spawn = False
    if ai5.health >= 0 and ai5Spawn == True:
        ai5Spawn = False
    if ai6.health >= 0 and ai6Spawn == True:
        ai6spawn = False
    if ai7.health >= 0 and ai7Spawn == True:
        ai7spawn = False
    if ai8.health >= 0 and ai8Spawn == True:
        ai8spawn = False
    if ai9.health >= 0 and ai9Spawn == True:
        ai9spawn = False
    if ai10.health >= 0 and ai10Spawn == True:
        ai10Spawn = False
    if ai11.health >= 0 and ai1Spawn == True:
        ai11Spawn = False
    if ai12.health >= 0 and ai12Spawn == True:
        ai12Spawn = False
    if ai13.health >= 0 and ai13Spawn == True:
        ai13Spawn = False
    if ai14.health >= 0 and ai14Spawn == True:
        ai14Spawn = False
    if ai15.health >= 0 and ai15Spawn == True:
        ai15Spawn = False
    if ai16.health >= 0 and ai16Spawn == True:
        ai16pawn = False
    if ai17.health >= 0 and ai17Spawn == True:
        ai17Spawn = False
    if ai18.health >= 0 and ai18Spawn == True:
        ai18Spawn = False
    if ai19.health >= 0 and ai19Spawn == True:
        ai19Spawn = False
    if ai20.health >= 0 and ai20Spawn == True:
        ai20Spawn = False

    if ramThiefHasSpawned == False and backgroundState == 'Mountain8' and ramThiefSpawn == False:
        ramThiefSpawn = True
        orbital = True
        stab = True
        dialogue = True
        ramThiefHasSpawned = True

    if RamThief.health <= 0 and ramThiefSpawn == True:
        ramThiefSpawn = False
        bgChange = True

    if ai1Spawn == True:
        ai1.approach(player, hostility)
        ai1.attack(player, hostility)
        ai1.update()
        ai1.Draw
    if ai2Spawn == True:
        ai2.approach(player, hostility)
        ai2.attack(player, hostility)
        ai2.update()
        ai2.Draw
    if ai3Spawn == True:
        ai3.approach(player, hostility)
        ai3.attack(player, hostility)
        ai3.update()
        ai3.Draw
    if ai4Spawn == True:
        ai4.approach(player, hostility)
        ai4.attack(player, hostility)
        ai4.update()
        ai4.Draw
    if ai5Spawn == True:
        ai5.approach(player, hostility)
        ai5.attack(player, hostility)
        ai5.update()
        ai5.Draw
    if ai6Spawn == True:
        ai6.approach(player, hostility)
        ai6.attack(player, hostility)
        ai6.update()
        ai6.Draw
    if ai7Spawn == True:
        ai7.approach(player, hostility)
        ai7.attack(player, hostility)
        ai7.update()
        ai7.Draw
    if ai8Spawn == True:
        ai8.approach(player, hostility)
        ai8.attack(player, hostility)
        ai8.update()
        ai8.Draw
    if ai9Spawn == True:
        ai9.approach(player, hostility)
        ai9.attack(player, hostility)
        ai9.update()
        ai9.Draw
    if ai10Spawn == True:
        ai10.approach(player, hostility)
        ai10.attack(player, hostility)
        ai10.update()
        ai10.Draw
    if ai11Spawn == True:
        ai11.approach(player, hostility)
        ai11.attack(player, hostility)
        ai11.update()
        ai11.Draw
    if ai12Spawn == True:
        ai12.approach(player, hostility)
        ai12.attack(player, hostility)
        ai12.update()
        ai12.Draw
    if ai13Spawn == True:
        ai13.approach(player, hostility)
        ai13.attack(player, hostility)
        ai13.update()
        ai13.Draw
    if ai4Spawn == True:
        ai14.approach(player, hostility)
        ai14.attack(player, hostility)
        ai14.update()
        ai14.Draw
    if ai15Spawn == True:
        ai15.approach(player, hostility)
        ai15.attack(player, hostility)
        ai15.update()
        ai15.Draw
    if ai16Spawn == True:
        ai16.approach(player, hostility)
        ai16.attack(player, hostility)
        ai16.update()
        ai16.Draw
    if ai17Spawn == True:
        ai17.approach(player, hostility)
        ai17.attack(player, hostility)
        ai17.update()
        ai17.Draw
    if ai18Spawn == True:
        ai18.approach(player, hostility)
        ai18.attack(player, hostility)
        ai18.update()
        ai18.Draw
    if ai19Spawn == True:
        ai19.approach(player, hostility)
        ai19.attack(player, hostility)
        ai19.update()
        ai19.Draw
    if ai20Spawn == True:
        ai20.approach(player, hostility)
        ai20.attack(player, hostility)
        ai20.update()
        ai20.Draw
   # print(backgroundState)
    bg.collision(backgroundState, player)
    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    if Rain == True: 
        rain.update(screen)

    if ramRain == True:
        ram_Shower.update(player)
        ram_Shower.draw(screen)
    if ramThiefSpawn == True: 
       # RamThief.movement(600, False)
        RamThief.draw(screen, gameFont)
        RamThief.update()
        if RamAttack == True:
            RamThief.SkyFall(350, 20, True, player)
            RamThief.smartMove(player, True)
            RamThief.powerPunch(player)

        if appended == False:
            orc_List.append(RamThief)
            appended = True
            
    if dialogue == True:
            screen.blit(dialogueBox, (50, 510))
            textSurface = gameFont.render(currentMessage, True, (255, 255, 255))
            screen.blit(textSurface, (80, 535))
    if currentSection == 'goodbye':
        Running = False
    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60)