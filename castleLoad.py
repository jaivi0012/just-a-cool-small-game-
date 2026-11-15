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

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(100000)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = backgroundLoader.background()
backgroundDraw = None
player = playerLogic.Player(0, 500)   
Weapons = weapons.Weapons(player)
Running = True
stabby = False
larry = pumpkinBoss.Boss(0, 425, 80000, 150, 150)
larryStarted = False
orc_List = []
Dead = False
lunge = True
attack = False
lungeCounter = 0
change = False
dialogue = True
orcy = 500
orcB = orcBoss.orcBoss(450, 425, 6000, 150, 150)
orc1 = orcSpawn.OrcSpawn(0, orcy, 600, 1.1, True)
orc2 = orcSpawn.OrcSpawn(30, orcy, 600, 0.9, True)
orc3 = orcSpawn.OrcSpawn(90, orcy, 600, 2.2, True)
orc4 = orcSpawn.OrcSpawn(750, orcy, 600, 0.6, True)
orc5 = orcSpawn.OrcSpawn(220, orcy, 600, 1.1, True)
orc6 = orcSpawn.OrcSpawn(110, orcy, 600, 2.1, True)
orc7 = orcSpawn.OrcSpawn(654, orcy, 600, 1.6, True)
orc8 = orcSpawn.OrcSpawn(555, orcy, 600, 1.8, True)
orc9 = orcSpawn.OrcSpawn(221, orcy, 600, 1.2, True)
orc10 = orcSpawn.OrcSpawn(112, orcy, 600, 1.9, True)

orc_List = [orc1, orc2, orc3, orc4, orc5, orc6, orc7, orc8, orc9, orc10]

messangerOrc = orcSpawn.OrcSpawn(50, orcy, 250, 2.2, True)
larryMusic = False
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
larrySpawn = False
orcBossSpawn = False
messangerorcSpawn = False
orcBossFight = False

allDead = False
spawnAll = False

stage1Spawned = False
stage2Spawned = False
stage3Spawned = False
stage4Spawned = False
stage5Spawned = False
stage6Spawned = False
stage7Spawned = False

wavesPerRoom = {'Castle1': 5, 'Castle2': 6, 'Castle4': 7, 'Castle5': 11}
spawnedRooms = []
waveCounter = 0

message1 = [
    'Larry is About to transform into his final form',
    'he has transformed',
    'he used a teleportation trick to send u to his castle',
    'you have been teleported to is castle'
]

message2 = [
    'you have entered his castle',
    'this castle is full of orc souls',
    'the souls are trapped in here as well',
    'the orcs are mind controlled ',
    'if orcs die they respawn again and again',
    'the orc souls are trapped beause of a crystal',
    'find that crystal and destroy it ',
    'and free the orcs from this misery',
    'the orcs will have a health buff'
    
]

message3 = [
    'there is the crystal',
    'to destroy it you have to kill orcs',
    'alot of orcs',
    'killing that many orcs will',
    'overload the ressurection crystal ',
    'which will destroy it ',
    'if the crystal gets destroyed ',
    'you will also be able to escape'
]

message4 = [
    'the crystal has been destroyed',
    'without the crystal',
    'this castle is collapsing',
    'the dimention is destroyed',
    'you have been teleported back to orc dimntion',

]

message5 = [
    'you haven now returned from his castle',
    'you should go back to the barn'
]

message6 = [
    'orc king is here',
    'you should go talk to him',
    'orcKing :- heyyy how u doin little one ',
    'orcKing :- you shouldve come to the castle ',
    'orcKing :- what are u doin in a little barn',
    'orcKing :- and the farmerOrc in here told me',
    'orcKing :- that a monster was around here',
    'orcKing :- and you were fighting it ',
    'orcKing :- wait why can i smell the scent of....',
    'orcKing :- WAITTT!! DID YOU FIGHT LARRY??',
    'orcKing :- HOW ARE YOU EVEN ALIVE',
    'orcKing :- LARRY HAS A MONSTEROUS HEALTH',
    'orcKing :- AND YOU DEFEATED HIM ????'  

]

message7 = [
    'orcSoldier :- sir the castle is destroyed  ',
    'orcSoldier :- the one belonging to larry',
    'orcSoldier :- the castle had many large holes',
    'orcSoldier :- and explosion traces',
    'orcKing :- WHATT',
    'orcKing :- HEY LITTLE ONE ',
    'orcKing :- WAS IT YOU WHO DESTROYED IT ?',
    'orcKing :- that castle had souls trapped',
    'orcKing :- orc Souls',
    'orcKing :- those poor orcs were suffering',
    'orcKing :- im greatful you helped them',
    'BOOM!!! '
]

message8 = [
    'orcKing :- larry has arrived once again',
    'orcKing :- little one you may have defeated him once',
    'orcKing :- but right now he is in his final form',
    'orcKing :- be careful we must defeat him togather',
    'orcKing :- grant me temporary resistance to your Nukes',
    'orcKing :- Thanks Now lets Defeat larry',
    'orcKing :- i will also increse your health ',
    'OBJECTIVE DEFEAT LARRY '
]

message9 = [
    'LARRY HAS BEEN DEFEATED AND HAS DIED',
    'TO BE CONTINUED ......'
]
messageIndex = 0
currentMessage = message1[messageIndex]
orbital = True
downwardLunge = True
stab = True
stabbyCounter = 0
movement = True
backgroundState = 'back7'
gameFont = pygame.font.Font(None, 36)
currentSection = 'Castle1'
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
                if currentSection == 'Castle1' and messageIndex > 3:
                    currentSection = 'Castle2'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    backgroundState = 'Castle'
                    player.x = 400
                    player.y = 500
                if currentSection == 'Castle2' and messageIndex > 8:
                    currentSection = 'Castle3'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    backgroundState = 'Castle1'
                if currentSection == 'Castle3' and messageIndex > 7:
                    currentSection = 'Castle4'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    backgroundState = 'Castle0'
                if currentSection == 'Castle4' and messageIndex > 4:
                    currentSection = 'Barn1'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                    backgroundState = 'back7'
                if currentSection == 'Barn1' and messageIndex > 1:
                    currentSection = 'Barn2'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                if currentSection == 'Barn2' and messageIndex > 12:
                    currentSection = 'Barn3'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                if currentSection == 'Barn3' and messageIndex > 11:
                    currentSection = 'Barn4'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                if currentSection == 'Barn4' and messageIndex > 7:
                    currentSection = 'Barn5'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                if currentSection == 'Barn5' and messageIndex > 1:
                    currentSection = 'goodbye'
                    messageIndex = 0
                    dialogue = False
                    movement = True
                if backgroundState == 'Castle':
                    dialogue = True

            if backgroundState == 'Castle0' and dialogue == False:
                backgroundState = 'Castle5'

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
    if backgroundState.startswith('Castle') and castleMusic == False:
        pygame.mixer.music.load('Sounds/DECISIVE_BATTLE.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        castleMusic = True

    if currentSection == 'Barn4' and larryMusic == False:
        pygame.mixer.music.load('Sounds/DEADLOCK.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        larryMusic = True

    if backgroundState.startswith('Castle') == False and castleMusic == True:
        pygame.mixer.music.fadeout(1000)
        castleMusic = False
    if downwardLunge == False and player.y >= 500:
        downwardLunge = True

    if backgroundState in wavesPerRoom and backgroundState not in spawnedRooms:
        spawnAll = True
        allDead = False
        waveCounter = 1
        spawnedRooms.append(backgroundState)

    if backgroundState in wavesPerRoom and waveCounter > 0 and waveCounter < wavesPerRoom[backgroundState] and allDead == True:
        spawnAll = True
        allDead = False
        waveCounter += 1        

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
        for orc in orc_List:
            orc.reset()
        spawnAll = False

    if orcspawn1 == False and orcspawn2 == False and orcspawn3 == False and orcspawn4 == False and orcspawn5 == False and orcspawn6 == False and orcspawn7 == False and orcspawn8 == False and orcspawn9 == False and orcspawn10 == False:
        allDead = True

    if orcspawn1 == True or orcspawn2 == True or orcspawn3 == True or orcspawn4 == True or orcspawn5 == True or orcspawn6 == True or orcspawn7 == True or orcspawn8 == True or orcspawn9 == True or orcspawn10 == True:
        allDead = False

    roomClear = allDead == True and waveCounter >= wavesPerRoom.get(backgroundState, 0)


    if currentSection == 'Castle1':
        currentMessage = message1[messageIndex]
    if currentSection == 'Castle2':
        currentMessage = message2[messageIndex]
    if currentSection == 'Castle3':
        currentMessage = message3[messageIndex]
    if currentSection == 'Castle4':
        currentMessage = message4[messageIndex]
    if currentSection == 'Barn1':
        currentMessage = message5[messageIndex]
    if currentSection == 'Barn2':
        currentMessage = message6[messageIndex]
    if currentSection == 'Barn3':
        currentMessage = message7[messageIndex]
    if currentSection == 'Barn4':
        currentMessage = message8[messageIndex]
    if currentSection == 'Barn5':
        currentMessage = message9[messageIndex]

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

        deathText = gameFont.render('YOU DIED', True, (255, 0, 0))
        screen.blit(deathText, (340, 280))
        pygame.display.flip()
        pygame.time.delay(1000)
        pygame.event.clear()
        pygame.mixer.music.stop()

        player.x = 0
        player.y = 500
        player.y_velocity = 0
        player.health = 3000
        player.Direction = 'Right'

        Weapons.maceU = False
        Weapons.orbitalStarted = False
        Weapons.orbital = False
        Weapons.nuke = False
        Weapons.tntAnimD = False
        Weapons.stabActive = False
        Weapons.tntY = 0
        Weapons.tntVelocity = 0
        Weapons.orbitalCounter = 0
        Weapons.orbitalCycle = 3
        Weapons.currentWeapon = 'mace'

        lunge = True
        attack = False
        lungeCounter = 0
        stabby = False
        stabbyCounter = 0
        maceCounter = 0
        downwardLunge = True

        if larry in orc_List:
            orc_List.remove(larry)        
        for orc in orc_List:
            orc.reset()
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
        waveCounter = 0
        spawnedRooms = []

        larry = pumpkinBoss.Boss(0, 425, 80000, 150, 150)
        orcB = orcBoss.orcBoss(450, 425, 6000, 150, 150)
        messangerOrc.reset()
        larryStarted = False
        larrySpawn = False
        orcBossSpawn = False
        orcBossFight = False
        messangerorcSpawn = False

   
        messageIndex = 0
        currentSection = 'Castle1'
        backgroundState = 'back7'
        dialogue = True
        movement = False
        castleMusic = False
        larryMusic = False

        Dead = False

    if backgroundState == 'back1':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0
    if backgroundState == 'Castle1':
        if player.x > 750:
            player.x = 750
        if roomClear == True:
            if player.x < 0:
                player.x = 750
                backgroundState = 'Castle2'
        if roomClear == False:
            if player.x < 0:
                player.x = 0
    if backgroundState == 'Castle2':
        if roomClear == True:
            if player.x > 750:
                player.x = 0
                backgroundState = 'Castle1'
            if player.x < 0:
                player.x = 750
                backgroundState = 'Castle3'
        if roomClear == False:
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

    if backgroundState == 'back7':
        if currentSection == 'Barn1':
            dialogue = True
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            backgroundState = 'back6'
            player.x = 750

    if backgroundState == 'back6':
        if currentSection == 'Barn2':
            dialogue = True
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0


    if player.y >= 680 and backgroundState == 'Castle3':
        player.y = 0
        player.x = 750
        backgroundState = 'Castle4'

    if backgroundState == 'Castle4':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            if roomClear == True:
                backgroundState = 'Castle0'
                dialogue = True
                player.x = 750
            else:
                player.x = 0
    if backgroundState == 'Castle5' or backgroundState == 'Castle6':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0
        if roomClear == True:
            backgroundState = 'Castle6'
            dialogue = True

    if backgroundState == 'Castle6':
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
            if key[pygame.K_s] and Weapons.orbitalStarted != True:
                Weapons.rod()
            if key[pygame.K_q]:
                Weapons.stabShot(orc_List, player)


    player.playerDisplay(screen)
    Weapons.draw(screen, player)

    if currentSection == 'Barn3':
        messangerorcSpawn = True
   # print(messangerOrc.ox)
    if messangerOrc.ox >= 395 and messangerOrc.ox <= 405 and currentSection == 'Barn3':
        dialogue = True

    if messangerorcSpawn == True and dialogue == False and currentSection == 'Barn3':
        messangerOrc.orcMove(400, False)
    if messangerorcSpawn == True and currentSection == 'Barn5':
        messangerOrc.orcMove(-100, False)
        if messangerOrc.ox < -75:
            messangerorcSpawn = False
    if messangerorcSpawn == True:
        messangerOrc.draw(screen)

    if currentSection == 'Barn4':
        larry.update()
        larry.Draw(screen)
        dialogue = True

    if backgroundState == 'back6' and orcBossSpawn == False:
        orcBossSpawn = True

    if currentSection == 'Barn5' and larryStarted == False:
        larryStarted = True
        larrySpawn = True
        player.health = 7000
        orc_List.append(larry)     

    if larrySpawn == True:
        larry.smartHunt(player)
        larry.update()
        larry.attack(player)
        larry.Draw(screen)
        if orcBossFight == False:
            orcBossFight = True
        if larry.ox < 0:
            larry.ox = 0
        if larry.ox > 650:
            larry.ox = 650
        if larry.health <= 0:
            larrySpawn = False
            orc_List.remove(larry)
            dialogue = True
            orcBossFight = False

    if orcBossSpawn == True and backgroundState == 'back6':
        orcB.update()
        orcB.draw(screen)
        if orcBossFight == True:
            orcB.track(player, larry, False)
            orcB.attack(player, larry, False)

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


    if dialogue == True:
        screen.blit(dialogueBox, (50, 510))
        textSurface = gameFont.render(currentMessage, True, (255, 255, 255))
        screen.blit(textSurface, (80, 535))
    if currentSection == 'goodbye':
        Running = False
    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60)