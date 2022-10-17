import pygame
from constants import speed, screen_width

player2_image = pygame.transform.scale(pygame.image.load('Assets/redrect.png'), (20, 100))


class PLayer2(pygame.sprite.Sprite):
    def __init__(self, ready):
        super().__init__()

        # Attributes
        self.ready = ready
        self.image = self.ready
        self.rect = self.image.get_rect(midbottom=(screen_width-20, 300))

        # phases
        self.up = False
        self.down = False

    def update(self):
        if self.up == True:
            self.rect.y -= speed
        if self.down == True:
            self.rect.y += speed
