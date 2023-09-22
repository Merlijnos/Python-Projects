import pygame
import random

pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Elden Ring")

# Load background music
pygame.mixer.music.load("Elden-Ring/background_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Load sound effect
explosion_sound = pygame.mixer.Sound("Elden-Ring/explosion.wav")

# Load player image
player_image = pygame.image.load("Elden-Ring/player.png")
player_width = player_image.get_width()
player_height = player_image.get_height()
player_image = pygame.transform.scale(player_image, (player_width // 2, player_height // 2))
player_width = player_image.get_width()
player_height = player_image.get_height()
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Load enemy image
enemy_image = pygame.image.load("Elden-Ring/enemy.png")
enemy_image = pygame.transform.rotate(enemy_image, -90)
enemy_image = pygame.transform.scale(enemy_image, (64, 64))
enemy_x = random.randint(0, screen_width - enemy_image.get_width())
enemy_y = random.randint(-screen_height, -enemy_image.get_height())
enemy_speed = 1

# Load background image
background_image = pygame.image.load("Elden-Ring/background.png")

# Define score variable
score = 0

# Define game over variables
game_over = False
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        enemy_y += enemy_speed + score // 10
        if enemy_y > screen_height:
            enemy_x = random.randint(0, screen_width - enemy_image.get_width())
            enemy_y = random.randint(-screen_height, -enemy_image.get_height())
            score += 1

        # Check for collisions
        if player_image.get_rect(topleft=(player_x, player_y)).colliderect(enemy_image.get_rect(topleft=(enemy_x, enemy_y))):
            explosion_sound.play()
            game_over = True

            # Stop background music
            pygame.mixer.music.stop()

    # Draw game objects
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw game over screen
    if game_over:
        screen.blit(game_over_text, game_over_rect)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()