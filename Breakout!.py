import pygame
import random

# Constants
SCREEN_WIDTH = 655
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
PADDLE_COLOR = (255, 255, 255)
BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_COLOR = (255, 0, 0)
BRICK_ROWS = 5
BRICK_COLUMNS = 10
BRICK_GAP = 5

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-2, 2])
        self.speed_y = -2

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check for collision with walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Check for collision with paddle
        if self.rect.colliderect(paddle.rect):
            self.speed_y = -self.speed_y

# Brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(BRICK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Group for bricks
bricks = pygame.sprite.Group()

# Create bricks
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        x = col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP
        y = row * (BRICK_HEIGHT + BRICK_GAP) + BRICK_GAP + 50
        brick = Brick(x, y)
        bricks.add(brick)

# Create paddle and ball
paddle = Paddle()
ball = Ball()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    paddle.update()
    ball.update()

    # Check for collision with bricks
    hit_bricks = pygame.sprite.spritecollide(ball, bricks, True)
    if hit_bricks:
        ball.speed_y = -ball.speed_y

    # Check for ball going out of bounds
    if ball.rect.bottom >= SCREEN_HEIGHT:
        running = False

    # Render
    screen.fill((0, 0, 0))
    screen.blit(paddle.image, paddle.rect)
    screen.blit(ball.image, ball.rect)
    bricks.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
