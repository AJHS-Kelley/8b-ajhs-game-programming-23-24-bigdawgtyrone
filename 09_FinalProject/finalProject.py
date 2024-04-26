import pygame
from sys import exit
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('lobotomy dash')
clock = pygame.time.Clock()

background = pygame.image.load('gdbackground_V1.png')
# playbutton = pygame.image.load('')
character = pygame.image.load('lobotomy.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    #screen.blit(playbutton,(0,0))
    screen.blit(character,(300,100))

    pygame.display.update()
    clock.tick(60)