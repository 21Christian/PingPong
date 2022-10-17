import pygame.sprite
from player1 import *
from player2 import *
from bounds import *
from ball import *
import random

# initialization
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')
color = (0, 0, 0)
background = pygame.transform.scale(pygame.image.load('Assets/Black.png'), (1000, 1000))
clock = pygame.time.Clock()
score_text = pygame.font.Font('font/Pixeltype.ttf', 20)
title_font = pygame.font.Font('font/Pixeltype.ttf', 40)
resume_text = pygame.font.Font('font/Pixeltype.ttf', 60)

player1_score = 0
player2_score = 0
ball_direction = random.randint(1, 40)

# class instances
player1 = PLayer1(player1_image)
player2 = PLayer2(player2_image)
up_bound = Bound(1)
low_bound = Bound(2)
ball = Ball(ball_image, screen_height/2, screen_height/2)

# groups
upper_bound = pygame.sprite.Group(up_bound)
lower_bound = pygame.sprite.Group(low_bound)
blue_player = pygame.sprite.Group(player1)
red_player = pygame.sprite.Group(player2)
the_ball = pygame.sprite.Group(ball)


# groups update
def groups_update():
    upper_bound.update()
    upper_bound.draw(screen)
    lower_bound.update()
    lower_bound.draw(screen)
    red_player.update()
    red_player.draw(screen)
    blue_player.update()
    blue_player.draw(screen)
    the_ball.update()
    the_ball.draw(screen)


# player input
def player_input():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            resume()
        if event.key == pygame.K_w:
            player1.up = True
        if event.key == pygame.K_s:
            player1.down = True
        if event.key == pygame.K_UP:
            player2.up = True
        if event.key == pygame.K_DOWN:
            player2.down = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            player1.up = False
        if event.key == pygame.K_s:
            player1.down = False
        if event.key == pygame.K_UP:
            player2.up = False
        if event.key == pygame.K_DOWN:
            player2.down = False


# collisions
def collision(player1, player2, upper_bound, lower_bound, ball_group, the_ball):
    global ball_x_speed
    # player collision with the borders
    if pygame.sprite.spritecollide(player1, upper_bound, dokill=False):
        player1.up = False
    if pygame.sprite.spritecollide(player1, lower_bound, dokill=False):
        player1.down = False
    if pygame.sprite.spritecollide(player2, upper_bound, dokill=False):
        player2.up = False
    if pygame.sprite.spritecollide(player2, lower_bound, dokill=False):
        player2.down = False

    # ball collision with the players
    player1_collision = pygame.sprite.spritecollide(player1, ball_group, dokill=False)
    player2_collision = pygame.sprite.spritecollide(player2, ball_group, dokill=False)
    if player1_collision:
        the_ball.blue_collision = True
        ball_x_speed *= -1
    if player2_collision:
        the_ball.red_collision = True
        ball_x_speed *= -1

def resume():
    playagain_surf = score_text.render('To resume the game press "space" ...', False, 'WHITE')
    playagain_rect = playagain_surf.get_rect(center=(screen_width/2, 200))
    screen.blit(playagain_surf, playagain_rect)
    pygame.display.update()

    resume = True
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resume = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def ball_collision(ball, border1, border2):
    global ball_y_speed
    # ball collision with the borders
    if pygame.Rect.colliderect(ball.rect, border1.rect):
        ball.down_collision = True
        ball_y_speed *= -1
    if pygame.Rect.colliderect(ball.rect, border2.rect):
        ball.up_collision = True
        ball_y_speed *= -1


def updating_ball_position():
    if ball_direction <= 10:
        ball.rect.x += ball_x_speed
        ball.rect.y += ball_y_speed
    if ball_direction >= 10 and ball_direction <= 20:
        ball.rect.x += ball_x_speed
        ball.rect.y -= ball_y_speed
    if ball_direction >= 20 and ball_direction <= 30:
        ball.rect.x -= ball_x_speed
        ball.rect.y += ball_y_speed
    if ball_direction >= 30 and ball_direction <= 40:
        ball.rect.x -= ball_x_speed
        ball.rect.y -= ball_y_speed

# displaying the text
def text():
    global player1_score, player2_score
    player1_text = score_text.render('Score: ' + str(player1_score), False, 'BLACK')
    player1_text_rect = player1_text.get_rect(topleft=(10, 0))

    player2_text = score_text.render('Score: ' + str(player2_score), False, 'BLACK')
    player2_text_rect = player2_text.get_rect(topleft=(screen_width-60, 0))

    screen.blit(player1_text, player1_text_rect)
    screen.blit(player2_text, player2_text_rect)

def menu_display():
    game_title_surf = title_font.render('PingPong Game', False, 'WHITE')
    game_title_rect = game_title_surf.get_rect(center=(screen_width/2, 200))
    screen.blit(game_title_surf, game_title_rect)

    start_surf = score_text.render('To start the game press "enter" ...', False, 'WHITE')
    start_rect = start_surf.get_rect(center=(screen_width/2, 240))
    screen.blit(start_surf, start_rect)

def ball_tracking():
    global player1_score, player2_score
    if ball.rect.x >= screen_width + 30 or ball.rect.x <= -30:
        ball.rect.x = screen_width / 2
        ball.rect.y = screen_height / 2
    else:
        pass
    if ball.rect.x >= screen_width + 5 and ball.rect.x <= screen_width + 6:
        player1_score += 1
    elif ball.rect.x <= 0 and ball.rect.x >= -2:
        player2_score += 1

# main loop
game_active = False
while True:
    if game_active == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            player_input()
        if player1_score >= 10 or player2_score >= 10:
            game_active = False
            player1_score = 0
            player2_score = 0

        ball_tracking()
        updating_ball_position()
        screen.blit(background, (0, 0))
        collision(player1, player2, upper_bound, lower_bound, the_ball, ball)
        ball_collision(ball, low_bound, up_bound)
        groups_update()
        text()
        pygame.display.flip()


    elif game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True

        screen.blit(background, (0, 0))
        menu_display()
    pygame.display.update()
    clock.tick(60)


