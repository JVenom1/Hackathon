import pygame, sys
from settings import * 
from level import Level
from settings import screen_height, screen_width
import os
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
WIN = pygame.display.set_mode((screen_width, screen_height))
space = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd()+ "\graphics/character/background/", 'road.webp')), (screen_width, screen_height))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			x = False
	WIN.blit(space, (0, 0))
	level.run()

	pygame.display.update()
	clock.tick(60)