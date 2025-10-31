import pygame
import sys
 
# Initialize pygame
pygame.init()
 
# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
 
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
 
# Clock
clock = pygame.time.Clock()
 
# Player setup
player_size = 20
player = pygame.Rect(50, 50, player_size, player_size)
 
# Goal setup
goal = pygame.Rect(550, 350, player_size, player_size)
 
# Maze walls (list of rectangles)
walls = [
   pygame.Rect(100, 0, 20, 300),
   pygame.Rect(200, 100, 20, 300),
   pygame.Rect(300, 0, 20, 250),
   pygame.Rect(400, 150, 20, 250),
   pygame.Rect(500, 0, 20, 250),
]
 
# Function to check wall collisions
def check_collision(rect, walls):
   for wall in walls:
       if rect.colliderect(wall):
           return True
   return False
 
# Game loop
running = True
while running:
   screen.fill(WHITE)
 
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
 
   keys = pygame.key.get_pressed()
   move_x, move_y = 0, 0
 
   if keys[pygame.K_LEFT]:
       move_x = -3
   if keys[pygame.K_RIGHT]:
       move_x = 3
   if keys[pygame.K_UP]:
       move_y = -3
   if keys[pygame.K_DOWN]:
       move_y = 3
 
   # Move player
   player.move_ip(move_x, move_y)
 
   # Collision with walls → undo move
   if check_collision(player, walls):
       player.move_ip(-move_x, -move_y)
 
   # Win condition
   if player.colliderect(goal):
       font = pygame.font.SysFont("Arial", 28)
       text = font.render("🎉 You Win!", True, RED)
       screen.blit(text, (230, 180))
       pygame.display.flip()
       pygame.time.wait(2000)
       running = False
 
   # Draw walls
   for wall in walls:
       pygame.draw.rect(screen, BLACK, wall)
 
   # Draw goal
   pygame.draw.rect(screen, GREEN, goal)
 
   # Draw player
   pygame.draw.rect(screen, BLUE, player)
 
   pygame.display.flip()
   clock.tick(30)
 
pygame.quit()
sys.exit()
 
