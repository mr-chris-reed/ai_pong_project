import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up game objects
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
left_paddle = pygame.Rect(50, HEIGHT/2 - 60, 20, 120)
right_paddle = pygame.Rect(WIDTH - 70, HEIGHT/2 - 60, 20, 120)

###
# load custom images
###
left_paddle_overlay = pygame.image.load("green_sword.png")
right_paddle_overlay = pygame.image.load("red_sword.png")
ancient_ball = pygame.image.load("ball.png")

###
# scale ball image
###
ancient_ball = pygame.transform.scale(ancient_ball, (75, 75))

###
# changed speed from 7 to 5
###
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
paddle_speed = 0
player1_speed = 0
player2_speed = 0

# Set up score variables
player1_score = 0
player2_score = 0

###
# set font and font size
###
font = pygame.font.Font('UnifrakturCook-Bold.ttf', 40)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -7
            if event.key == pygame.K_s:
                player1_speed = 7
            if event.key == pygame.K_UP:
                player2_speed = -7
            if event.key == pygame.K_DOWN:
                player2_speed = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_speed = 0

    # Move paddles
    left_paddle.y += player1_speed
    right_paddle.y += player2_speed
    if left_paddle.top <= 0:
        left_paddle.top = 0
    if left_paddle.bottom >= HEIGHT:
        left_paddle.bottom = HEIGHT
    if right_paddle.top <= 0:
        right_paddle.top = 0
    if right_paddle.bottom >= HEIGHT:
        right_paddle.bottom = HEIGHT

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.right >= WIDTH:
        player1_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Clear the screen
    screen.fill(BLACK)

    ###
    # changed color of rectangle paddles
    ###
    # Draw the paddles and ball
    pygame.draw.rect(screen, BLACK, left_paddle)
    pygame.draw.rect(screen, BLACK, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    ###
    # draw images on top of rectangles and ball
    ###
    screen.blit(left_paddle_overlay, ((left_paddle.right - left_paddle.left) / 2 - 8, left_paddle.top))
    screen.blit(right_paddle_overlay, (WIDTH - 118, right_paddle.top))
    screen.blit(ancient_ball, (ball.left - 25, ball.top - 25))

    ###
    # draw the name of the game
    ###
    game_name = font.render("Ancient Pong", True, (50, 205, 50))
    screen.blit(game_name, (WIDTH/2 - 90, 20))

    # Draw the score
    player1_text = font.render(f"{player1_score}", True, (50, 205, 50))
    player2_text = font.render(f"{player2_score}", True, (252, 52, 42))
    screen.blit(player1_text, (WIDTH/4 - player1_text.get_width()/2, 20))
    screen.blit(player2_text, (WIDTH*3/4 - player2_text.get_width()/2, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
