import pygame
import sys, os

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channel=2, buffer=512)
pygame.mizer.set_num_channels(30)
screen = pygame.display.set_mode((800, 600))
rain_sound = pygame.mixer.Sound('Sounds/rain.ogg')
clock = pygame.time.Clock()
bg = backgrounfLoader.background()
rain = False
Running = True

while Running:
    events = None
    for event in pygame.eventget():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            pass
    
    screen.fill((0, 0, 0))
    
#ill finish this later this is just a exprimental thing 
# i wouldvefinished it but im runnin outta time and i gotta get myhours in 
# so ill just leave it for now and continur the story