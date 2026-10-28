import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Survival Game")

clock = pygame.time.Clock()
velocityY = 0
OrcVelocityY = 0
running = True
jumpCount = 0
x = 0
y = 500
ox = 750
oy = 500
jumpHeight = -15
gravity = 0.9
base = 500
speed = 10
doubleJump = True

orcOG = pygame.image.load('survivalGame/Orc1.png')
playerOG = pygame.image.load('survivalGame/Soldier1.png')  # Load the player image
player = pygame.transform.scale(playerOG,(70,70))
orc = pygame.transform.scale(orcOG,(70,70))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MOVED HERE: Out of the right arrow key and into the event loop
        if event.type == pygame.KEYDOWN:
            # FIXED: Using event.key instead of keys array for clean single taps
            if event.key == pygame.K_SPACE and doubleJump == True:
                velocityY = jumpHeight  # Direct assignment gives a crisp double jump boost
                jumpCount += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if jumpCount >= 2:
        doubleJump = False

    if jumpCount <= 0:
        doubleJump = True

    if y == base:
        jumpCount = 0        


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


    if x == ox and y == oy:
        x = 0
        y = 500
        ox = 750
        oy = 500

    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(player, (x, y))  # Draw the player image at the current position
    screen.blit(orc, (ox, oy))  # Draw the orc image at a fixed position
    pygame.draw.rect(screen, (139, 69, 19), (0, 570, 800, 50))  # Draw a brown rectangle
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

    print(x)
    print(y)
    

pygame.quit()