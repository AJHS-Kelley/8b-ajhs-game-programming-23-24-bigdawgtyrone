import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('bintricalizationability')
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')
                                
spike_surface = pygame.image.load()  
spike_x_pos = 600

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
           
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    spike_x_pos -= 4
    if spike_x_pos < -100: spike_x_pos = 800
    screen.blit(spike_surface,(300,300))
   
    pygame.display.update()
    clock.tick(60)
  