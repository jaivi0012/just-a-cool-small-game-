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
bg = backgroundLoader.background()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
player = playerLogic.Player(0, 500)   
Weapons = weapons.Weapons(player)
Running = True
guard1 = orcSpawn.OrcSpawn(900, 500, 250, 1, False)
guard2 = orcSpawn.OrcSpawn(800, 500, 250, 1, False)
orc_List = [guard1, guard2]
guard1spawn = True
guard2spawn = True
playerInSewer = False
lunge = True
attack = False
lungeCounter = 0
mace = True
maceCounter = 0
dialogue = True
currentMessage = None
guardMove = [500, 400]
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
movement = False
backgroundState = 'back1'

messageIndex = 0
currentSection = 'Beggining'

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
            if movement == True:
                
                    if event.key == pygame.K_SPACE:
                        player.jump()  
                    if event.key == pygame.K_a:
                        lunge = True
                        attack = True
                    if event.key == pygame.K_d and mace == True:
                        Weapons.mace(orc_List, player)
                        mace = False    
    if currentSection == 'Beggining':
        currentMessage = message[messageIndex]
    if currentSection == 'Mid':
        currentMessage = message2[messageIndex]
    screen.fill((0, 0, 0))
    bg.draw(screen, backgroundState)
    key = pygame.key.get_pressed()

    if movement == True:
        player.move(key)
        player.playerDirection(key)

    Weapons.update(player, orc_List)

    if guard2.ox < 520 and currentSection == 'Mid':
        dialogue = True

    if player.y > 650:
        movement = False
        playerInSewer = True

    if dialogue == True:
        movement = False
    if mace == False:
        maceCounter += 1
 
    if maceCounter >= 5:
        maceCounter = 0
        mace = True
    
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

    if currentSection == 'InTunnel':
        guardMove[0] = 1000
        guardMove[1] = 1000

    player.playerDisplay(screen)
    Weapons.draw(screen, player)
    if guard1spawn == True:
        guard1.draw(screen)
    if guard2spawn == True:
            guard2.draw(screen)

    if dialogue == True:
        screen.blit(dialogueBox, (50, 510))
        currentDialogue = currentMessage
        textSurface = gameFont.render(currentDialogue, True, (255, 255, 255))
        screen.blit(textSurface, (80, 535))

    pygame.display.flip()  
    clock.tick(60) 
    