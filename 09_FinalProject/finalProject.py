#Final Project, Christian Ortiz, v0.0s
import sys, random, pygame

resolution = 0  # 0 = low resolution(800, 600), 1 = high resolution (1920, 1080).

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080 

pygame.init()

difficulty = int(input("Please type the exact name of the level you would like to play.\n"))

if difficulty == 'Stereo Madness':
    pygame.display.set_caption('Stereo Madness')
else:
    pygame.display.set_caption('Lobotomy wave')

screen = pygame.display.set_mode((x, y))