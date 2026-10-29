import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Survival Game")

maceX = 50
maceY = 20
x = 0
y = 500
oldX = 0


orcsX = [750, 740, 730, 720, 710, 700, 690, 680]
orcsY = [500, 500, 500, 500, 500, 500, 500, 500]

tntX = [0, 90, 180, 270, 360, 450, 540, 630, 720]

tntDistances = []



velocityY = 0
Orc1VelocityY = 0
Orc2VelocityY = 0
Orc3VelocityY = 0
Orc4VelocityY = 0
Orc5VelocityY = 0
Orc6VelocityY = 0
Orc7VelocityY = 0
Orc8VelocityY = 0

orcHelth = [150, 100, 100, 100, 100, 100, 100, 100]

tntVelocity = 0

clock = pygame.time.Clock()


tntY = 0

running = True
doubleJump = True
inAir = False
playerDir = 'Right'
rodPulled = False
currentWeapon = 'mace'
attack = False
exploded = False
orcSpawn1 = False
orcSpawn2 = False
orcSpawn3 = False
orcSpawn4 = False
orcSpawn5 = False
orcSpawn6 = False
orcSpawn7 = False
orcSpawn8 = False
gameBegin = True
menuButtonPress = True
showDialogue = False
lunge = False
override = False
enter = 0
lungeCounter = 0

jumpCount = 0
jumpHeight = -25
maceJump = - 30
gravity = 0.9
base = 500
speed = 8
Power = 20
enterCounter = 0
orcSpeed = 3
counter = 0
count = 0
cycles = 0

gameMenu = pygame.image.load('survivalGame/frontMenu.png').convert()
playButton = pygame.image.load('survivalGame/playButton.png').convert()
exitButton = pygame.image.load('survivalGame/exitButton.png').convert()


orc1OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc2OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc3OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc4OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc5OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc6OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc7OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc8OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()

playerOG = pygame.image.load('survivalGame/Soldier1.png').convert_alpha()

maceOG = pygame.image.load('survivalGame/mace.png').convert_alpha()

tnt1OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt2OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt3OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt4OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt5OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt6OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt7OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt8OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt9OG = pygame.image.load('survivalGame/tnt.jpeg').convert()

platform1OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform2OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform3OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform4OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform5OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform6OG = pygame.image.load('survivalGame/platform.png').convert_alpha()

player = pygame.transform.scale(playerOG,(70,70))

orc1 = pygame.transform.scale(orc1OG,(70,70))
orc2 = pygame.transform.scale(orc2OG,(70,70))
orc3 = pygame.transform.scale(orc3OG,(70,70))
orc4 = pygame.transform.scale(orc4OG,(70,70))
orc5 = pygame.transform.scale(orc5OG,(70,70))
orc6 = pygame.transform.scale(orc6OG,(70,70))
orc7 = pygame.transform.scale(orc7OG,(70,70))
orc8 = pygame.transform.scale(orc8OG,(70,70))


mace = pygame.transform.scale(maceOG,(30,30))

tnt1 = pygame.transform.scale(tnt1OG,(30,30))
tnt2 = pygame.transform.scale(tnt2OG,(30,30))
tnt3 = pygame.transform.scale(tnt3OG,(30,30))
tnt4 = pygame.transform.scale(tnt4OG,(30,30))
tnt5 = pygame.transform.scale(tnt5OG,(30,30))
tnt6 = pygame.transform.scale(tnt6OG,(30,30))
tnt7 = pygame.transform.scale(tnt7OG,(30,30))
tnt8 = pygame.transform.scale(tnt8OG,(30,30))
tnt9 = pygame.transform.scale(tnt9OG,(30,30))

platform = pygame.transform.scale(platform1OG,(150,50))

platform2 = pygame.transform.scale(platform2OG,(150,50))
platform3 = pygame.transform.scale(platform3OG,(150,50))
platform4 = pygame.transform.scale(platform4OG,(150,50))
platform5 = pygame.transform.scale(platform5OG,(150,50))
platform6 = pygame.transform.scale(platform6OG,(150,50))

mace_flipped = pygame.transform.flip(mace, True, False)  # Create a flipped version of the mace image
currentMace = mace_flipped  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if gameBegin == False:
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    enter = 1
                if event.key == pygame.K_UP:
                    menuButtonPress = True
                if event.key == pygame.K_DOWN:
                    menuButtonPress = False

        if gameBegin == True:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE and doubleJump == True:
                    velocityY = jumpHeight  
                    jumpCount += 1

                if event.key == pygame.K_d:
                    attack = True

                if event.key == pygame.K_s:
                    rodPulled = True
                    cycles = 0
                    count = 0

                if event.key == pygame.K_a:
                    lunge = True

    if lunge == True:
        lungeCounter += 1
    if lungeCounter == 4:
        lungeCounter = 0
        lunge = False
        
    if attack == True:
        counter += 1

    if counter >= 15:
        attack = False  
        counter = 0   


    print(lunge)
    playerRect = pygame.Rect(x + 21, y+ 22, 30, 40)
    
    maceRect = pygame.Rect(x + 25,y + 45,20,80)

    orc1Rect = pygame.Rect(orcsX[0] + 13, orcsY[0] + 25, 30, 35)
    orc2Rect = pygame.Rect(orcsX[1] + 13, orcsY[1] + 25, 30, 35)
    orc3Rect = pygame.Rect(orcsX[2] + 13, orcsY[2] + 25, 30, 35)
    orc4Rect = pygame.Rect(orcsX[3] + 13, orcsY[3] + 25, 30, 35)
    orc5Rect = pygame.Rect(orcsX[4] + 13, orcsY[4] + 25, 30, 35)
    orc6Rect = pygame.Rect(orcsX[5] + 13, orcsY[5] + 25, 30, 35)
    orc7Rect = pygame.Rect(orcsX[6] + 13, orcsY[6] + 25, 30, 35)
    orc8Rect = pygame.Rect(orcsX[7] + 13, orcsY[7] + 25, 30, 35)

    keys = pygame.key.get_pressed()

    if enter == 1:
        enterCounter += 1

    if enterCounter == 15:
        enter = 0
        enterCounter = 0
    if gameBegin == True:
        if keys[pygame.K_LEFT]:
            x -= speed

        if keys[pygame.K_RIGHT]:
            x += speed

        if lunge == True and playerDir == 'Right':
            x += Power
        if lunge == True and playerDir == 'Left':
            x -= Power

    if jumpCount >= 2:
        doubleJump = False

    if jumpCount <= 0:
        doubleJump = True

    if y == base:
        jumpCount = 0    

    if y >= 450:
        inAir = False

    if y < 500:
        inAir = True     

    if x > oldX:
        currentMace = mace_flipped
        playerDir = 'Right'
        maceX = 50

    if x < oldX:
        currentMace = mace    
        playerDir = 'Left'
        maceX = -15

    if x < 0:
        x = 0

    if x > 750:
        x = 750    

    if y > 500:
        y = 500
    
    velocityY += gravity
    y += velocityY
     
    if y > base:
        y = base
        velocityY = 0

    if maceRect.colliderect(orc1Rect) and attack == True and orcSpawn1 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[0] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc2Rect) and attack == True and orcSpawn2 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[1] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc3Rect) and attack == True and orcSpawn3 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[2] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc4Rect) and attack == True and orcSpawn4 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[3] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc5Rect) and attack == True and orcSpawn5 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[4] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc6Rect) and attack == True and orcSpawn6 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[5] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc7Rect) and attack == True and orcSpawn7 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[6] -= damage
        velocityY = maceJump                   
        attack = False

    if maceRect.colliderect(orc8Rect) and attack == True and orcSpawn8 == True:
        fallspeed = max(velocityY, 0)
        damage = 10 + fallspeed * 4
        orcHelth[7] -= damage
        velocityY = maceJump                   
        attack = False 


    if playerRect.colliderect(orc1Rect) and orcSpawn1 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc2Rect) and orcSpawn2 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc3Rect) and orcSpawn3 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc4Rect) and orcSpawn4 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc5Rect) and orcSpawn5 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc6Rect) and orcSpawn6 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc7Rect) and orcSpawn7 == True:
        x = 0
        y = 500

    if playerRect.colliderect(orc8Rect) and orcSpawn8 == True:
        x = 0
        y = 500
# ORC AI section
        
    if override == False:
        if x > orcsX[0]:
            orcsX[0] += orcSpeed

        if x < orcsX[0]:
            orcsX[0] -= orcSpeed      

    if x - 10 <= orcsX[0] and x + 10 >= orcsX[0] and y != base:
    
        if orcsX[0] <= 0:
            orcsX[0] += orcSpeed
        if orcsX[0] >= 750:
            orcsX[0] -= orcSpeed
        if orcsX[0] < 750 and orcsX[0] > 375:
            orcsX[0] += orcSpeed
        else:
            orcsX[0] -= orcSpeed

    if x != orcsX[0] and y == base:
        override = False   

    if x > orcsX[1]:
            orcsX[1] += orcSpeed + 2
    
    if x < orcsX[1]:
        orcsX[1] -= orcSpeed + 2

    
    if x > orcsX[2]:
            orcsX[2] += orcSpeed + 1
    
    if x < orcsX[2]:
        orcsX[2] -= orcSpeed + 1


    if x > orcsX[3]:
            orcsX[3] += orcSpeed + 0.5
    
    if x < orcsX[3]:
        orcsX[3] -= orcSpeed + 0.5

    
    if x > orcsX[4]:
            orcsX[4] += orcSpeed + 2.5
    
    if x < orcsX[4]:
        orcsX[4] -= orcSpeed + 2.5



    if x > orcsX[5]:
            orcsX[5] += orcSpeed + 0.9
    
    if x < orcsX[5]:
        orcsX[5] -= orcSpeed + 0.9


    if x > orcsX[6]:
            orcsX[6] += orcSpeed + 1.7
    
    if x < orcsX[6]:
        orcsX[6] -= orcSpeed + 1.7


    if x > orcsX[7]:
            orcsX[7] += orcSpeed + 1.3
    
    if x < orcsX[7]:
        orcsX[7] -= orcSpeed + 1.3


 # ---------------------------------------------------------------------------------------------------------------- 

    oldX = x

    if gameBegin == True:
        screen.blit(currentMace, (x + maceX, y + maceY))  # Draw the mace image at the player's position
        screen.blit(player, (x, y))  # Draw the player image at the current position

        if orcSpawn1 == True:
            screen.blit(orc1, (orcsX[0], orcsY[0]))  # Draw the orc image at a fixed position
        if orcSpawn2 == True:
            screen.blit(orc2, (orcsX[1], orcsY[1]))  # Draw the orc image at a fixed position
        if orcSpawn3 == True:
            screen.blit(orc3, (orcsX[2], orcsY[2]))  # Draw the orc image at a fixed position
        if orcSpawn4 == True:
            screen.blit(orc4, (orcsX[3], orcsY[3]))  # Draw the orc image at a fixed position
        if orcSpawn5 == True:
            screen.blit(orc5, (orcsX[4], orcsY[4]))  # Draw the orc image at a fixed position
        if orcSpawn6 == True:
            screen.blit(orc6, (orcsX[5], orcsY[5]))  # Draw the orc image at a fixed position
        if orcSpawn7 == True:
            screen.blit(orc7, (orcsX[6], orcsY[6]))  # Draw the orc image at a fixed position
        if orcSpawn8 == True:
            screen.blit(orc8, (orcsX[7], orcsY[7]))  # Draw the orc image at a fixed position

    playButtonRect = pygame.Rect(175, 235, 450, 100)
    exitButtonRect = pygame.Rect(175, 385, 450, 100)

    if gameBegin == False:
        if menuButtonPress == True:  
            pygame.draw.rect(screen,'red', playButtonRect)
        if menuButtonPress == False:
            pygame.draw.rect(screen,'red',exitButtonRect)

    if gameBegin == False:
        screen.blit(gameMenu, (150, 50))


    if enter == 1 and menuButtonPress == True:
        gameBegin = True
    if enter == 1 and menuButtonPress == False:
        running = False

    if gameBegin == False:
        screen.blit(playButton,(200, 250))
        screen.blit(exitButton,(200, 400))

    screen.blit(platform, (0, 560))  # Draw the platform image

    if rodPulled == True:
        count += 1

    if count >= 60:
        count = 0

    if count > 30:
        activation = True

    if count <= 0:
        activation = False
        cycles += 1
        
    if rodPulled == True and activation == False:
    
        screen.blit(tnt1, (0, tntY))  # Draw the TNT image at a fixed position
        screen.blit(tnt2, (90, tntY))  # Draw the second TNT image at a fixed position
        screen.blit(tnt3, (180, tntY))  # Draw the third TNT image at a fixed position
        screen.blit(tnt4, (270, tntY))  # Draw the fourth TNT image at a fixed position
        screen.blit(tnt5, (360, tntY))  # Draw the fifth TNT image at a fixed position
        screen.blit(tnt6, (450, tntY))  # Draw the sixth TNT image at a fixed position
        screen.blit(tnt7, (540, tntY))  # Draw the seventh TNT image at a fixed position
        screen.blit(tnt8, (630, tntY))  # Draw the seventh TNT image at a fixed position
        screen.blit(tnt9, (720, tntY))  # Draw the seventh TNT image at a fixed position

        tntVelocity += gravity
        tntY += tntVelocity

    if tntY > 528:
        tntY = 528
        tntVelocity = 0    


    if orcHelth[0] <= 0:
        orcHelth[0] = 150
        orcsX[0] = 750
        orcsY[0] = 500
    if orcHelth[1] <= 0:
        orcHelth[1] = 100
        orcsX[1] = 740
        orcsY[1] = 500

    if orcHelth[2] <= 0:
        orcHelth[2] = 100
        orcsX[2] = 730
        orcsY[2] = 500

    if orcHelth[3] <= 0:
        orcHelth[3] = 100
        orcsX[3] = 720
        orcsY[3] = 500    

    if orcHelth[4] <= 0:
        orcHelth[4] = 100
        orcsX[4] = 710
        orcsY[4] = 500
    
    if orcHelth[5] <= 0:
        orcHelth[5] = 100
        orcsX[5] = 700
        orcsY[5] = 500

    if orcHelth[6] <= 0:
        orcHelth[6] = 100
        orcsX[6] = 690
        orcsY[6] = 500

    if orcHelth[7] <= 0:
        orcHelth[7] = 100
        orcsX[7] = 680
        orcsY[7] = 500

    if cycles > 4:
        if rodPulled == True:
            for i in range(len(tntX)):
                ax = tntX[i] + 15
                ay = tntY + 15

                for l in range(len(orcsX)):
                    bx = orcsX[l] + 35
                    by = orcsY[l] + 35

                    distance = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
                    tntDistances.append(distance)

                    if distance < 65:
                        orcHelth[l] -= 200
        cycles = 0
        rodPulled = False
        tntY = 0
        tntVelocity = 0
        activation = False


    screen.blit(platform2, (150, 560))  # Draw the second platform image
    screen.blit(platform3, (301, 560))  # Draw the third platform image
    screen.blit(platform4, (450, 560))  # Draw the fourth platform image
    screen.blit(platform5, (600, 560))  # Draw the fifth platform image
    screen.blit(platform6, (750, 560))  # Draw the sixth platform image
   # pygame.draw.rect(screen, (139, 69, 19), (0, 570, 800, 50))  # Draw a brown rectangle
   # pygame.draw.rect(screen, (255, 0, 0), maceRect)  # Draw the red rectangle for the mace
   # pygame.draw.rect(screen, 'red', orc1Rect)
   # pygame.draw.rect(screen, 'red', playerRect)
    if rodPulled == True and activation == True:
            pygame.draw.rect(screen, ("white"), (0, tntY, 30, 30))  # Draw a red rectangle for the TNT
            pygame.draw.rect(screen, ("white"), (90, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (180, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (270, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (360, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (450, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (540, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (630, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (720, tntY, 30, 30))

   # pygame.draw.rect(screen, ('white'), (750, 100, 50, 50))

 
    if showDialogue == True:
            pygame.draw.rect(screen, (210,180,140), (0, 550, 800,50))
    
            tntVelocity += gravity
            tntY += tntVelocity
   # print(velocityY)
   # print(orcHelth[0], orcHelth[1], orcHelth[2], orcHelth[3], orcHelth[4], orcHelth[5], orcHelth[6], orcHelth[7])
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    screen.fill((0, 0, 0))  # Fill the screen with black


    
pygame.quit()