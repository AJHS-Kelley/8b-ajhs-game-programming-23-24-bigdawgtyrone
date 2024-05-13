import pygame
from sys import exit
screen = pygame.display.set_mode((800,400))
# pygame.font.Font('')
pygame.display.set_caption('lobotomy dash')
clock = pygame.time.Clock()

background = pygame.image.load('gdbackground_V1.png')
playbutton = pygame.image.load('playbutton_V1.png')
# character = pygame.image.load('newlobotomy.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    screen.blit(playbutton,(285,100))
    #screen.blit(character,(300,100))

    pygame.display.update()
    clock.tick(60)
    pass


if event.type == pygame.MOUSEBUTTONDOWN:
        if gdpb_rect.collidepoint(event.pos):
            game_active = True
if game_active == True:
    screen = screen2
    screen.blit(background, (0,0))
    screen.blit(newlobotomy.png (300,130))
    screen.blit()
    screen.blit()
    level_name = font2.render('Lobotomy dash', False, WHITE)