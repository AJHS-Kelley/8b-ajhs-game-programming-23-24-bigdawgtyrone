#Final Project, Christian Ortiz, v0.0s
import sys, random, pygame

resolution = 0  # 0 = low resolution(800, 600), 1 = high resolution (1920, 1080).

screen = pygame.display.set_mode((x, y))

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080 