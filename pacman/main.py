import pygame
from global_variables import Global
from pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
x = 10
y = 10
vel_x = Global.VELOCIDADE
vel_y = Global.VELOCIDADE


pacman = Pacman()

while True:
    # calculo de regras
    pacman.calcular_regras()

    # pinta
    screen.fill(Global.PRETO)
    pacman.pintar(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # Eventos
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()

        pacman.processar_evetos(eventos)
