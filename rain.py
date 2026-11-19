import random
import pygame


class RainSystem:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.drops = []

   
    for _ in range(150):
      x = random.randint(0, self.width)
      y = random.randint(-self.height, 0)
      speed = random.randint(10, 18)
      length = random.randint(10, 25)
      self.drops.append([x, y, speed, length])

  def update(self, screen):
    rain_color = (170, 190, 210) 

    for drop in self.drops:
      drop[1] += drop[2]
      if drop[1] > self.height:
        drop[1] = random.randint(-50, 0)
        drop[0] = random.randint(0, self.width)

      pygame.draw.line(
          screen,
          rain_color,
          (drop[0], drop[1]),
          (
              drop[0] + 1,
              drop[1] + drop[3],
          ),  
          1,
      )