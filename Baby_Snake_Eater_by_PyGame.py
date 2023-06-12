import pygame
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1

def main():
    pygame.init()
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Sk. Salahuddin")

    player = pygame.Rect(0, 0, SIZE, SIZE)
    goal = pygame.Rect(360, 360, 20, 20)
    score = 0
    font = pygame.font.Font(None, 20)

    movement_direction = [1, 0]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                handle_key_press(event.key, movement_direction)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos, player, movement_direction)

        player.x += SIZE * movement_direction[0]
        player.y += SIZE * movement_direction[1]

        player_x = player.x
        player_y = player.y

        if (
            player_x > CANVAS_WIDTH - SIZE
            or player_x < 0
            or player_y > CANVAS_HEIGHT - SIZE
            or player_y < 0
        ):
            game_over(canvas, score)
            return

        if player.colliderect(goal):
            hit_goal(goal)
            score += 1

        canvas.fill((0, 0, 0))
        pygame.draw.rect(canvas, (0, 0, 255), player)
        pygame.draw.rect(canvas, (255, 69, 0), goal)
        score_text = font.render("Your points: " + str(score), True, (255, 255, 255))
        canvas.blit(score_text, (5, 385))

        pygame.display.flip()
        clock.tick(10)

def handle_key_press(key, movement_direction):
    if key == pygame.K_LEFT:
        movement_direction[0] = -1
        movement_direction[1] = 0
    elif key == pygame.K_RIGHT:
        movement_direction[0] = 1
        movement_direction[1] = 0
    elif key == pygame.K_UP:
        movement_direction[0] = 0
        movement_direction[1] = -1
    elif key == pygame.K_DOWN:
        movement_direction[0] = 0
        movement_direction[1] = 1

def handle_mouse_click(position, player, movement_direction):
    player.x = position[0] - SIZE // 2
    player.y = position[1] - SIZE // 2
    movement_direction[0] = 0
    movement_direction[1] = 0

def game_over(canvas, score):
    font = pygame.font.Font(None, 40)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render("Your score is: " + str(score), True, (0, 0, 255))
    canvas.blit(game_over_text, (100, 170))
    canvas.blit(score_text, (100, 200))
    pygame.display.flip()
    pygame.time.wait(2000)

def hit_goal(goal):
    goal.x = random.randrange(0, CANVAS_WIDTH - SIZE + 1, SIZE)
    goal.y = random.randrange(0, CANVAS_HEIGHT - SIZE + 1, SIZE)

if __name__ == "__main__":
    main()
