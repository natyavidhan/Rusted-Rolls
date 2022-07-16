import pygame, json, os
import engine

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dino Run: Story Mode")
clock = pygame.time.Clock()
RUNNING = True

game_map = engine.SceneMap("assets/maps/map1.json", "assets/art/terrain")
level_1 = engine.Scene(screen, game_map)


while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    level_1.draw()
    pygame.display.flip()