import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the paddle and ball size
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
BALL_SIZE = 15

# Set the paddle offset from the edge of the screen
PADDLE_OFFSET = 20

# Set the ball's initial speed and direction
ball_speed = 5
ball_dx = ball_speed
ball_dy = ball_speed

# Set the score to win
SCORE_TO_WIN = 3

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the font
font = pygame.font.SysFont(None, 50)

# Set the window caption
pygame.display.set_caption("Pong")

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the initial paddle positions
paddle_left_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_right_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set the initial ball position
ball_x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
ball_y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2

# Initialize the scores
score_left = 0
score_right = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_left_y > 0:
        paddle_left_y -= 5
    if keys[pygame.K_s] and paddle_left_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_left_y += 5
    if keys[pygame.K_UP] and paddle_right_y > 0:
        paddle_right_y -= 5
    if keys[pygame.K_DOWN] and paddle_right_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_right_y += 5

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collision with top and bottom walls
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Check for collision with left and right paddles
    if ball_x <= PADDLE_OFFSET + PADDLE_WIDTH and paddle_left_y <= ball_y + BALL_SIZE <= paddle_left_y + PADDLE_HEIGHT:
        ball_dx *= -1
    if ball_x >= WINDOW_WIDTH - PADDLE_OFFSET - PADDLE_WIDTH - BALL_SIZE and paddle_right_y <= ball_y + BALL_SIZE <= paddle_right_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Check for scoring
    if ball_x <= 0:
        score_right += 1
        ball_x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball_y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1
    elif ball_x >= WINDOW_WIDTH - BALL_SIZE:
        score_left += 1
        ball_x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball_y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1

    # Check for winner
    if score_left == SCORE_TO_WIN or score_right == SCORE_TO_WIN:
        winner_text = "Player 1 Wins!" if score_left == SCORE_TO_WIN else "Player 2 Wins!"
        winner_surface = font.render(winner_text, True, WHITE)
        winner_rect = winner_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(winner_surface, winner_rect)
        pygame.display.update()

        # Wait for 3 seconds and then reset the game
        pygame.time.delay(3000)
        score_left = 0
        score_right = 0
        ball_x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball_y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = ball_speed
        ball_dy = ball_speed
        paddle_left_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
        paddle_right_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
        continue

    # Draw the background and the paddles
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (PADDLE_OFFSET, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, (WINDOW_WIDTH - PADDLE_OFFSET - PADDLE_WIDTH, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(window, WHITE, (ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2), BALL_SIZE // 2)

    # Draw the scores
    score_surface = font.render(str(score_left) + " - " + str(score_right), True, WHITE)
    score_rect = score_surface.get_rect(center=(WINDOW_WIDTH // 2, 50))
    window.blit(score_surface, score_rect)

    # Update the window
    pygame.display.update()

    # Set the game clock
    clock = pygame.time.Clock()
    clock.tick(60)


