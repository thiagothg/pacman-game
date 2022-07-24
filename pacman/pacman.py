import pygame.draw
from global_variables import Global

class Pacman:
    def __init__(self, size):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = size
        self.raio = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0

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

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        # if self.centro_x + self.raio > 800:
        #     self.vel_x = -1
        # if self.centro_x - self.raio < 0:
        #     self.vel_x = 1
        #
        # if self.centro_y + self.raio > 600:
        #     self.vel_y = -1
        # if self.centro_y - self.raio < 0:
        #     self.vel_y = 1

    def processar_evetos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = Global.VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -Global.VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -Global.VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = Global.VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def processar_eventos_mouse(self, eventos):
        delay = 1000
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay
