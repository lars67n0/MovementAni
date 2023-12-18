import pygame
import os

pygame.init()

# CONSTANTS
    # COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
    # SCREEN
WIDTH, HEIGHT = 900, 500
    # FRAMES PER SECOND
FPS = 60
    # PLAYER / ENEMY SIZE
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40

    # PlAYER IMAGES
PLAYER_IMAGES = [pygame.image.load(
    os.path.join('PlayerAni', f'Player{i}.png')) for i in range(1, 7)
]
# VARIABLES
active = True
player_dead = False
current_player_image = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice Game!")

def draw_window(Player):
    global current_player_image 
    WIN.fill(WHITE)
    WIN.blit(PLAYER_IMAGES[current_player_image], (Player.x, Player.y))
    current_player_image = (current_player_image + 1) % len(PLAYER_IMAGES)
    pygame.display.flip()

def movement(Player):
    x_change = 0
    y_change = 0
    GRAVITY = -1
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]: #LEFT
        x_change -= 5
        
    if keys_pressed[pygame.K_d]: # RIGHT
        x_change += 5

    if keys_pressed[pygame.K_SPACE] and Player.y == 410: # JUMP
        y_change = 70
    

    # X MOVEMENT
    if 0 <= Player.x < 860:
        Player.x += x_change
    
    # BOUNDARY CONDITION
    if Player.x < 0:
        Player.x = 0
    if Player.x >= 860:
        Player.x = 859
    
    
    # JUMP LOGIC
    if y_change > 0 or Player.y < 410:
       Player.y -= y_change
       Player.y -= GRAVITY
    
    if Player.y > 410:
       Player.y = 409

def main():
    Player = pygame.Rect(200, 410, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        movement(Player)
        draw_window(Player)

    pygame.quit()

if __name__ == "__main__":
    main()