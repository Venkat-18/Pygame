import pygame
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Constants import Constants
from Game import Game
from common.colors import Colors
# pygame.init()
# pygame.mixer.init()
screen_width = Constants.screen_width + (6*Constants.tile_size)
screen_height = Constants.screen_height
FPS = Constants.FPS
main_screen = pygame.display.set_mode([screen_width, screen_height])
# Initializing the font module to work.
pygame.font.init()
play_screen = pygame.Surface(main_screen.get_size())
game = Game(play_screen)
pygame.display.set_caption(Constants.game_name)
clock = pygame.time.Clock()
running = True
play_screen.fill((255, 255, 255))
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            game.key_event(event)
    game.update()
    main_screen.blit(play_screen, (0, 0))
    pygame.display.update()

pygame.quit()
