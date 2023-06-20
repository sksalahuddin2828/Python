# This game is not completed
# It's not bouncing ! and sorry because i'm very busy with my Stanford University study

import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Sk. Salahuddin")
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_radius = 10
ball_color = RED
paddle_width = 100
paddle_height = 10
paddle_color = WHITE
paddle_pos = [(SCREEN_WIDTH - paddle_width) // 2, SCREEN_HEIGHT - paddle_height * 2]
brick_width = 60
brick_height = 20
brick_color = WHITE
brick_gap = 10
brick_offset = 30
brick_list = []
for i in range(7):
    for j in range(5):
        brick_x = brick_offset + i * (brick_width + brick_gap)
        brick_y = brick_offset + j * (brick_height + brick_gap)
        brick_list.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
clock = pygame.time.Clock()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= 5
    if keys[pygame.K_RIGHT] and paddle_pos[0] < SCREEN_WIDTH - paddle_width:
        paddle_pos[0] += 5 
    ball_vel = [2, 2]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > SCREEN_WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - ball_radius < 0:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] + ball_radius > SCREEN_HEIGHT:
        game_over = True
    if ball_pos[1] + ball_radius >= paddle_pos[1] and \
            paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + paddle_width:
        ball_vel[1] = -ball_vel[1]
        ball_pos[1] = paddle_pos[1] - ball_radius
    for brick in brick_list:
        if brick.collidepoint(ball_pos):
            brick_list.remove(brick)
            ball_vel[1] = -ball_vel[1]
            ball_color = WHITE
            break
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)
    pygame.draw.rect(screen, paddle_color, paddle_rect)
    for brick in brick_list:
        pygame.draw.rect(screen, brick_color, brick)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
