import pygame
from global_variables import Global
from pacman import Pacman
from scenario import Scenario
from ghost import Ghost

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
font = pygame.font.SysFont('arial', 24, True, False)

size = 600 // 30
pacman = Pacman(size)
blinky = Ghost(Global.VERMELHO, size)
scenario = Scenario(size, pacman, font)

while True:
    # calculo de regras
    pacman.process_rules()
    scenario.process_rules()

    # pinta
    screen.fill(Global.PRETO)
    scenario.draw(screen)
    pacman.draw(screen)
    blinky.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # Eventos
    eventos = pygame.event.get()
    pacman.process_events(eventos)
    scenario.process_events(eventos)
    # pacman.processar_eventos_mouse(eventos)
