import os
import sys
import time
import random
from msvcrt import getch

# Game Settings
WIDTH, HEIGHT = 20, 15
CELL = '■'
FOOD = '●'
EMPTY = ' '

class SnakeGame:
    def __init__(self):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (1, 0)  # Right
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
    
    def create_food(self):
        while True:
            food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            if food not in self.snake:
                return food
    
    def move(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        # Check food
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()
    
    def change_direction(self, key):
        directions = {
            b'w': (0, -1),  # Up
            b's': (0, 1),   # Down
            b'a': (-1, 0),  # Left
            b'd': (1, 0),   # Right
            b'H': (0, -1),  # Arrow Up
            b'P': (0, 1),   # Arrow Down
            b'K': (-1, 0),  # Arrow Left
            b'M': (1, 0)    # Arrow Right
        }
        
        if key in directions:
            new_dir = directions[key]
            # Prevent 180 degree turn
            if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
                self.direction = new_dir
    
    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Top border
        print('┌' + '─' * (WIDTH * 2) + '┐')
        
        # Game board
        for y in range(HEIGHT):
            print('│', end='')
            for x in range(WIDTH):
                if (x, y) in self.snake:
                    if (x, y) == self.snake[0]:
                        print('█ ', end='')  # Snake head
                    else:
                        print(CELL + ' ', end='')
                elif (x, y) == self.food:
                    print(FOOD + ' ', end='')
                else:
                    print(EMPTY + ' ', end='')
            print('│')
        
        # Bottom border
        print('└' + '─' * (WIDTH * 2) + '┘')
        print(f'\nScore: {self.score}')
        print('Controls: W/A/S/D or Arrow Keys | Q to Quit')

def main():
    game = SnakeGame()
    
    print("Snake Game Starting...")
    print("Controls: W/A/S/D or Arrow Keys")
    print("Press any key to start...")
    getch()
    
    while not game.game_over:
        game.draw()
        
        # Non-blocking input check
        start_time = time.time()
        while time.time() - start_time < 0.15:  # Game speed
            if sys.platform == 'win32':
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'q' or key == b'Q':
                        game.game_over = True
                        break
                    # Handle arrow keys
                    if key == b'\xe0':  # Arrow key prefix
                        key = msvcrt.getch()
                    game.change_direction(key)
                    break
        
        if not game.game_over:
            game.move()
    
    game.draw()
    print('\n🎮 GAME OVER! 🎮')
    print(f'Final Score: {game.score}')
    print('\nPress any key to exit...')
    getch()

if __name__ == "__main__":
    main()