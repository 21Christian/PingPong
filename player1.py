import pygame
from constants import *

player1_image = pygame.transform.scale(pygame.image.load('Assets/bluerect.png'), (20, 100))


class PLayer1(pygame.sprite.Sprite):
    def __init__(self, ready):
        super().__init__()

        # Attributes
        self.ready = ready

        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(20, 300))

        # phases
        self.up = False
        self.down = False

    def update(self):
        if self.up == True:
            self.rect.y -= speed
        if self.down == True:
            self.rect.y += speed
