import pygame
import random
import time

width = 1920
height = 1080

pygame.init()
root = pygame.display.set_mode((width, height))
pygame.display.set_caption('ПРостая игра')
score = 0
black = (0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
player_x = width//2
player_y = height//2

player_width = 50
player_height = 50

ball_radius = 20
ball_speed = 0.3

cr = [red, green, blue]
balls = []

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

'''def fg():
    g = random.randint(0, len(cr) - 1)
    time.sleep(3)'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 20
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += 20

    if random.randint(0, 100) < 5:
        ball_x = random.randint(0, width - ball_radius * 2)
        ball_y = 0
        balls.append((ball_x, ball_y))

    i=0
    while i < len(balls):
        ball_x = balls[i][0]
        ball_y = balls[i][1]
        ball_y += ball_speed
        balls[i] = (ball_x, ball_y)

        if (player_x < ball_x + ball_radius and player_x + player_width > ball_x - ball_radius and player_y < ball_y + ball_radius and player_y + player_height > ball_y - ball_radius):
            balls.pop(i)
            score += 1
        else:
            i += 1
    root.fill(black)
    pygame.draw.rect(root, white, (player_x, player_y, player_width, player_height))

    for ball_x, ball_y in balls:

        pygame.draw.circle(root, red, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)
    score_text = font.render(f'Счет {score}', True, green)
    pygame.display.flip()

    print(balls)

pygame.display.flip()