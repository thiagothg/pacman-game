import pygame.draw
from global_variables import Global

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 50
        self.raio = self.tamanho // 2

    def pintar(self, tela):
        #desenho o corpo do pacman
        pygame.draw.circle(tela, Global.AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # desenho da boca do pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, Global.PRETO, pontos, 0)

        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)

        pygame.draw.circle(tela, Global.PRETO, (olho_x, olho_y), olho_raio, 0)

