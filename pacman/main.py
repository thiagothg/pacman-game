import pygame
from global_variables import Global
from pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((680, 480), 0)
x = 10
y = 10
vel_x = Global.VELOCIDADE
vel_y = Global.VELOCIDADE


pacman = Pacman()

while True:
    #calculo de regras


    #pinta
    # tela.fill(globals().PRETO)
    pacman.pintar(screen)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            exit()
