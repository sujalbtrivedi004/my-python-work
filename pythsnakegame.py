import pygame
import random

# Initialize Pygame
pygame.init()

# Game Settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake setup
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL_SIZE, 0)  # Moving right initially

# Food setup
def create_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return (x, y)

food = create_food()
score = 0

# Game loop
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                # Reset game
                snake = [(WIDTH // 2, HEIGHT // 2)]
                direction = (CELL_SIZE, 0)
                food = create_food()
                score = 0
                game_over = False

    if not game_over:
        # Move snake
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        
        # Check collisions
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT or 
            new_head in snake):
            game_over = True
        else:
            snake.insert(0, new_head)
            
            # Check if food eaten
            if new_head == food:
                score += 1
                food = create_food()
            else:
                snake.pop()

    # Draw everything
    screen.fill(BLACK)
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("Game Over! Press SPACE to restart", True, WHITE)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()