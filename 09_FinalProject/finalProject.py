import pygame
from sys import exit

# START SCREEN
#font = pygame.font.Font('Seagram.ttf', 30)
screen = pygame.display.set_mode((800,400))
screen2 = False
screen3 = False
pygame.display.set_caption('lobotomy dash')
game_active = False
background = pygame.image.load('gdbackground_V1.png')
#start_wordsurface = font.render('Lobotomy dash', False, 'GREEN')
playbutton = pygame.image.load('playbutton_V1.png')
play_rect = playbutton.get_rect(center = (285,100))

#level_icon = pygame.image.load('newlobotomy.png')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    screen.blit(playbutton,(285,100))
    #screen.blit(level_icon,(300,100))


    


    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_rect.collidepoint(event.pos):
            game_active = True
    if game_active == True:
        screen = screen2
        screen.blit(background, (0,0))
        screen.blit('newlobotomy.png' (300,130))
        #screen.blit()
        #screen.blit()
        level_name = font.render('Lobotomy dash', False, 'WHITE')
    
    pygame.display.update()
    clock.tick(60)