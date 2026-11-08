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
import pumpkinBoss

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = backgroundLoader.background()
player = playerLogic.Player(0, 500)   
Weapons = weapons.Weapons(player)
Running = True
guard1 = orcSpawn.OrcSpawn(900, 500, 250, 1, False)
guard2 = orcSpawn.OrcSpawn(800, 500, 250, 1, False)
orcSoldier1 = orcSpawn.OrcSpawn(900, 500, 250, 1.5, False)
orcSoldier2 = orcSpawn.OrcSpawn(800, 500, 250, 1, False)
npc1 = orcSpawn.OrcSpawn(200, 450, 250, 1, False)
stabby = False
larryThePumpkin = pumpkinBoss.Boss(700, 450, 50000, 100, 100)
orc_List = [orcSoldier1, orcSoldier2, larryThePumpkin]
guard1spawn = True
guard2spawn = True
playerInSewer = False
Dead = False
lunge = True
attack = False
lungeCounter = 0
change = False
dialogue = True
currentMessage = None
guardMove = [500, 400]
orbital = False
hasSpawned = False
orcSoldierSpawn1 = False
orcSoldierSpawn2 = False
bossFight = False
stab = False
bossMusicStarted = False
stabbyCounter = 0
message = [
    'You Enter a New Dimention',
    'This Dimention is not Home',
    'you hear distant Talking',
    'QUICKK!! hide',
    'Jump into the Gutter',
    'do not to use your orbital Strike',
    'try not to get attention'
]
message2 = [
    'OrcSoldier1 :- Man i swear i heared something',
    'OrcSoldier2 :- u always be hearing things',
    'OrcSoldier2 :- see its nothing here',
    'OrcSoldier2 :- u Should go get your ears checked out',
    'OrcSoldier1 :- i could have sworn i heared a sound',
    'OrcSoldier1 :- from right here',
    'OrcSoldier1 :- i  should go get my ears checked',
    'OrcSoldier2 :- well get them checked later cuz now',
    'OrcSoldier2 :- we go cuz the king called us in ',
    'OrcSoldier2 :- they said they found a very fat dude',
    'OrcSoldier2 :- they also say that that guy can speak',
    'OrcSoldier2 :- although he just keeps screamin',
    'OrcSoldier2 :- he also says he is from earth',
    'OrcSoldier1 :- we better go or its gonna be bad for us'
]
message3 = [
    'you have fallen into the gutter',
    'you heared the conversation between the orcs',
    'this seems to be the home dimention of orcs',
    'go meet the orc king',
    'ask him why he didnt send you home',
    'and try not to get seen',
    'and dont use any orbitals while underground',
    'if u incounter any orc underground',
    'kill it'
]
message4 = [
    'npcOrc :- oh hey',
    'npcOrc :- didnt expect to see you here',
    'npcOrc :- the king old us to expect a visitor',
    'npcOrc :- he said you are very friendly and strong',
    'npcOrc :- shouldnt you be in the main city ?',
    'npcOrc :- how come you visit my little barn',
    'npcOrc :- my two sons also went in that travel highway',
    'npcOrc :- they are your biggest fans',
    'npcOrc :- they went to the main city',
    'npcOrc :- just to meet you',
    'npcOrc :- did you see them in there ?',
    'npcOrc :- they said that they will approach you',
    'npcOrc :- and then try to communicate with you ',
    'npcOrc :- they dont intend to harm you',
    'npcOrc :- so if you see them dont hurt them',
    'npcOrc :- maybe they had reached the city before you',
    'npcOrc :- well may i ask of a small favour from you',
    'npcOrc :- a monster has entered my barn',
    'npcOrc :- it has killed all my farm animals',
    'npcOrc :- so can you defeat it for me ? ',
    'npcOrc :- i was about to call the orc guards ',
    'npcOrc :- but you are here alredy you can handle him',
    'npcOrc :- thanks for the favour ill repay it',
    'npcOrc :- and feel free to use your full power ',
    'npcOrc :- after all its just empty fields in here',
    'npcOrc :- the monster should be in the field on the right',
    'ORBITAL STRIKE ACTIVATED',
    'STAB SHOT ACTIVATED',
    'QUEST - DEFEAT THE MONSTER'
    
]

message5 = [
    'LARRY THE PUMPKIN has been defeated',
    'BUT THIS WAS NOT HIS FInAL FORM',
    'FINAL FORM COMING SOON'
]
movement = False
backgroundState = 'back1'
gameFont = pygame.font.Font(None, 36)
messageIndex = 0
currentSection = 'Beggining'
text = None
maceCounter = 0
gameFont = pygame.font.Font(None, 36)
dialogueBox = pygame.image.load('dialogueBox.png').convert_alpha()
while Running:
    events = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and dialogue == True:
                messageIndex += 1
                if messageIndex > 6 and currentSection == 'Beggining':
                    messageIndex = 0
                    currentSection = 'Mid'
                    dialogue = False
                    movement = True
                if messageIndex > 13 and currentSection == 'Mid':
                    messageIndex = 0
                    currentSection = 'InTunnel'
                    dialogue = False
                if messageIndex > 8 and currentSection == 'InTunnel':
                    messageIndex = 0
                    currentSection = 'Barn'
                    dialogue = False
                    movement = True
                if messageIndex > 28 and currentSection == 'Barn':
                    messageIndex = 0
                    currentSection = 'end'
                    dialogue = False
                    movement = True
                if messageIndex > 3 and currentSection == 'end':
                    Running = False
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


    if bossFight == True and bossMusicStarted == False:
        pygame.mixer.music.load('Sounds/cahosConstruct.mp3')
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)
        bossMusicStarted = True
    if currentSection == 'Beggining':
        currentMessage = message[messageIndex]
    if currentSection == 'Mid':
        currentMessage = message2[messageIndex]
    if currentSection == 'InTunnel':
        currentMessage = message3[messageIndex]
    if currentSection == 'Barn':
         currentMessage = message4[messageIndex]
    if currentSection == 'end':
        currentMessage = message5[messageIndex]
    screen.fill((0, 0, 0))
    if Dead == True:
        pygame.mixer.music.stop()
        player = playerLogic.Player(0, 500)
        Weapons = weapons.Weapons(player)
        guard1 = orcSpawn.OrcSpawn(900, 500, 250, 1, False)
        guard2 = orcSpawn.OrcSpawn(800, 500, 250, 1, False)
        orcSoldier1 = orcSpawn.OrcSpawn(900, 500, 250, 1.5, False)
        orcSoldier2 = orcSpawn.OrcSpawn(800, 500, 250, 1, False)
        npc1 = orcSpawn.OrcSpawn(200, 450, 250, 1, False)
        larryThePumpkin = pumpkinBoss.Boss(700, 450, 50000, 100, 100)
        orc_List = [orcSoldier1, orcSoldier2, larryThePumpkin]
        guard1spawn = True
        guard2spawn = True
        playerInSewer = False
        lunge = True
        attack = False
        lungeCounter = 0
        change = False
        maceCounter = 0
        dialogue = True
        currentMessage = None
        guardMove = [500, 400]
        orbital = False
        hasSpawned = False
        orcSoldierSpawn1 = False
        orcSoldierSpawn2 = False
        bossFight = False
        bossMusicStarted = False
        stab = False
        stabby = False
        stabbyCounter = 0
        movement = False
        backgroundState = 'back1'
        messageIndex = 0
        currentSection = 'Beggining'
        Dead = False

    if stabby == True:
        stabbyCounter += 1
        if stabbyCounter > 25:
            stabby = False
            stabbyCounter = 0
    
    bg.draw(screen, backgroundState)
    if Weapons.maceU == True:

        Weapons.mace(orc_List, player)
        maceCounter += 1
        if maceCounter >= 13 or Weapons.maceU == False: 
            Weapons.maceU = False
            maceCounter = 0

    if backgroundState == 'back7' and bossFight == True:
        larryThePumpkin.update()
        larryThePumpkin.hunt(player)
        larryThePumpkin.attack(player)

    key = pygame.key.get_pressed()
    text = gameFont.render(f"Health: {player.health}", True, (255, 255, 255))
    if movement == True:
        player.move(key, backgroundState)
        player.playerDirection(key)

    if player.health <= 0:
        Dead = True

    if backgroundState == 'back6':
        npc1.draw(screen)

    Weapons.update(player, orc_List)
    if currentSection == 'end':
        orbital = True

    if guard2.ox < 520 and currentSection == 'Mid':
        dialogue = True

    if player.y > 650:
        movement = False
        playerInSewer = True

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

    if playerInSewer == True:

        if guard1spawn == True:
            guard1.orcMove(guardMove[0], False)
        if guard1.health <= 0:
            guard1spawn = False
        if guard2spawn == True:
                guard2.orcMove(guardMove[1], False)
        if guard2.health <= 0:
            guard2spawn = False

    if larryThePumpkin.health < 0:
        bossFight = False
        dialogue = True
        pygame.mixer.music.stop()
        bossMusicStarted = False
    
    if currentSection == 'InTunnel':
        guardMove[0] = 1000
        guardMove[1] = 1000
        if guard1.ox > 650 and change == False:
            guard1spawn = False
            guard2spawn = False
            backgroundState = 'back2'
            change = True
            movement = True
            playerInSewer = False
            player.y = 500
            dialogue = True
    if backgroundState == 'back4' and hasSpawned == False:
        orcSoldierSpawn1 = True
        orcSoldierSpawn2 = True  
        hasSpawned = True

    if orcSoldierSpawn1 == True:
        orcSoldier1.orcAi(player, True)
    if orcSoldierSpawn2 == True:
        orcSoldier2.orcAi(player, True)
    if orcSoldier1.health < 0:
         orcSoldierSpawn1 = False
    if orcSoldier2.health < 0:
         orcSoldierSpawn2 = False

    if backgroundState == 'back2' and player.x > 750:
        player.x = 0
        backgroundState = 'back3'
    if backgroundState == 'back3':
            if player.x > 750:
                player.x = 0
                backgroundState = 'back4'
            if player.x < 0:
                player.x = 750
                backgroundState = 'back2'
    if backgroundState == 'back4' and (orcSoldierSpawn1 == False and orcSoldierSpawn2 == False):
            if player.x > 750:
                player.x = 0
                backgroundState = 'back5'
            if player.x < 0:
                player.x = 750
                backgroundState = 'back3'
    if backgroundState == 'back5':
            if player.x > 750:
                player.x = 0
                backgroundState = 'back6'
            if player.x < 0:
                player.x = 750
                backgroundState = 'back4'
    if backgroundState == 'back6':
            if currentSection == 'Barn':
                dialogue = True
            if player.x > 750:
                player.x = 0
                backgroundState = 'back7'
                bossFight = True
                stab = True
    if backgroundState == 'back7':
            if player.x < 0 and bossFight == False:
                player.x = 750
                backgroundState = 'back6'

    if orcSoldierSpawn1 == True:
        orcSoldier1.draw(screen)
    if orcSoldierSpawn2 == True:
        orcSoldier2.draw(screen)

    print(backgroundState)

    if orcSoldierSpawn2 == True or orcSoldierSpawn1 == True:
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0
    if backgroundState == 'back6':
         if player.x < 0:
            player.x = 0
    print(player.x)
    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    if guard1spawn == True:
        guard1.draw(screen)
    if guard2spawn == True:
            guard2.draw(screen)

    if backgroundState == 'back7':
        if player.x > 750:
            player.x = 750
        if player.x < 0:
            player.x = 0
    if larryThePumpkin.ox > 750:
        larryThePumpkin.ox = 750
    if larryThePumpkin.ox < 0:
        larryThePumpkin.ox = 0


    if dialogue == True:
        screen.blit(dialogueBox, (50, 510))
        currentDialogue = currentMessage
        textSurface = gameFont.render(currentDialogue, True, (255, 255, 255))
        screen.blit(textSurface, (80, 535))
    if backgroundState == 'back7' and bossFight == True:
        larryThePumpkin.Draw(screen)
    screen.blit(text, (20, 20))
    pygame.display.flip()  
    clock.tick(60) 
    