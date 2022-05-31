import pygame

AMARELO = (255, 255, 0)
PRETO = (0,0,0)
VELOCIDADE = 1
RAIO = 50
pygame.init()

tela = pygame.display.set_mode((680, 480), 0)
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE
while True:
    #calculo de regras
    x = x + vel_x
    y = y + vel_y

    if x + RAIO> 680:
        vel_x = - VELOCIDADE
    elif x - RAIO < 0:
        vel_x = VELOCIDADE

    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    elif y - RAIO < 0:
        vel_y = VELOCIDADE

    #pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, ( int(x), int(y)), RAIO, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            exit()