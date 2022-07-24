import pygame
from global_variables import Global
from pacman import Pacman
from scenario import Scenario

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

size = 600 // 30
pacman = Pacman(size)
scenario = Scenario(size)

while True:
    # calculo de regras
    pacman.calcular_regras()

    # pinta
    screen.fill(Global.PRETO)
    scenario.pintar(screen, pacman)
    pacman.pintar(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # Eventos
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()

        pacman.processar_evetos(eventos)
        # pacman.processar_eventos_mouse(eventos)
