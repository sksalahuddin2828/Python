import pygame
import random
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.1

def main():
    pygame.init()
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    clock = pygame.time.Clock()

    player = pygame.Rect(0, 0, SIZE, SIZE)
    goal = pygame.Rect(360, 360, SIZE, SIZE)
    score = 0
    font = pygame.font.Font(None, 20)

    movement_direction = [1, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            movement_direction = [-1, 0]
        elif keys[pygame.K_RIGHT]:
            movement_direction = [1, 0]
        elif keys[pygame.K_UP]:
            movement_direction = [0, -1]
        elif keys[pygame.K_DOWN]:
            movement_direction = [0, 1]

        player.x += SIZE * movement_direction[0]
        player.y += SIZE * movement_direction[1]

        if (
            player.x > CANVAS_WIDTH - SIZE
            or player.x < 0
            or player.y > CANVAS_HEIGHT - SIZE
            or player.y < 0
        ):
            game_over(canvas, score, goal)
            return

        if player.colliderect(goal):
            hit_goal(canvas, goal)
            score += 1

        canvas.fill((255, 255, 255))
        pygame.draw.rect(canvas, (0, 0, 255), player)
        pygame.draw.rect(canvas, (255, 0, 0), goal)

        score_text = font.render(f"Your score: {score}", True, (0, 0, 255))
        canvas.blit(score_text, (5, 385))

        pygame.display.flip()
        clock.tick(10)

def game_over(canvas, score, goal):
    font = pygame.font.Font(None, 30)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render(f"Your score is: {score}", True, (0, 0, 255))

    canvas.blit(game_over_text, (140, 170))
    canvas.blit(score_text, (130, 200))

    pygame.display.flip()
    time.sleep(3)

    pygame.quit()

def hit_goal(canvas, goal):
    goal.x = random.randrange(0, CANVAS_WIDTH - SIZE + 1, SIZE)
    goal.y = random.randrange(0, CANVAS_HEIGHT - SIZE + 1, SIZE)

if __name__ == '__main__':
    main()
