import pygame, sys
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fenetre.fill([10,186,181])

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()

fenetre.blit(perso, position_perso)

pygame.display.flip()

while True :
  pass


for event in pygame.event.get():   
  if event.type == KEYDOWN:
    if event.key == K_RIGHT:
      print("flèche droite appuyée")
