import pygame
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        image = '/graphics/character/Mc/TTB.png'
        mainPath = os.getcwd() + image
        self.image = pygame.image.load(
            os.path.join(mainPath))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift