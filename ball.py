import pygame
from constants import ball_x_speed, ball_y_speed, screen_height, screen_width
ball_image = pygame.transform.scale(pygame.image.load('Assets/White Circle.png'), (30, 30))

class Ball(pygame.sprite.Sprite):
    def __init__(self, ready, pos_x, pos_y):
        super().__init__()

        # Attributes
        self.ready = ready

        self.image = self.ready
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        # phases
        self.blue_collision = False
        self.red_collision = False
        self.up_collision = False
        self.down_collision = False

    def update(self):
        if self.blue_collision == True:
            self.rect.x += ball_x_speed
        if self.red_collision == True:
            self.rect.x -= ball_x_speed
        if self.up_collision == True:
            self.rect.y += ball_y_speed
        if self.down_collision == True:
            self.rect.y -= ball_y_speed
