import pygame
from constants import *

class Bound(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        if player == 1:
            self.image = pygame.transform.scale(pygame.image.load('Assets/green.png'), (screen_width, 10))
            self.rect = self.image.get_rect(midbottom=(250, 10))
        elif player == 2:
            self.image = pygame.transform.scale(pygame.image.load('Assets/green.png'), (screen_width, 10))
            self.rect = self.image.get_rect(midbottom=(250, 600))