import pygame
from pygame.locals import *
from sys import exit
import math
import numpy

pygame.init()

largura = 800
altura = 700

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Argand-Gauss Plan')
fonte = pygame.font.SysFont('arial',15,bold=True,italic = False)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0,0,0), (0,0,largura,altura))
    pygame.draw.line(tela, (255,255,255), (largura/2,0), (largura/2,altura), 2)
    pygame.draw.line(tela, (255,255,255), (0,altura/2), (largura,altura/2), 2)

    mouse = pygame.mouse.get_pos()
    posicio = int(mouse[0]) - 400
    posicio2 = int(mouse[1]) - 350
    posicio2 = posicio2*-1
    mod =int( (posicio**2 + posicio2**2)**0.5)
    tg = 0
    ang = 0
    cos = posicio/mod
    sen = posicio2/mod
    try:
        ang = numpy.arcsin (sen)
        ang = numpy.rad2deg(ang)
    except:
        ang = math.acos(cos)
        ang = numpy.rad2deg(ang)
    if ang < 0:
        ang = ang*-1
    if posicio < 0 and posicio2 > 0:
        ang = 180 - ang
    elif posicio < 0 and posicio2 < 0:
        ang = 180 + ang
    elif posicio > 0 and posicio2 < 0:
        ang = 360 - ang
        
    mensagem = f'{posicio}'
    mensagem_1 = f'{posicio2}i'
    mensagem2 = '|{a} + {b}i|'.format(a=posicio, b=posicio2)
    mensagem3 = '{c}(cos{d} + i.sen{d})'.format(c=mod,d=int(ang))
    theta = 'θ = {q}'.format(q=int(ang))
    theta_format = fonte.render(theta, False, (150,150,150))
    tela.blit(theta_format, (largura/2 + 10, altura/2 + 10 ))
    texto_formatado = fonte.render(mensagem, False, (150,0,0))
    texto_formatado_1 = fonte.render(mensagem_1, False, (150,0,0))
    tela.blit(texto_formatado,(posicio + 400, altura/2 + 5))
    tela.blit(texto_formatado_1,(largura/2 - 35, posicio2*-1 + 350))
    
    
    texto_formatado2 = fonte.render(mensagem2, False, (255,255,255))
    texto_formatado3 = fonte.render(mensagem3, False, (150,150,150))
    tela.blit(texto_formatado2,(posicio - 20+ 400 , posicio2*-1 + 40 + 350))
    tela.blit(texto_formatado3,(largura/2,0))
    pygame.draw.circle(tela, (150,150,150), (largura/2, altura/2), 10, 1)
    pygame.draw.line(tela, (150,0,0), (largura/2,altura/2), (posicio + 400,posicio2*-1 + 350), 2)
    
    pygame.draw.line(tela, (80,0,0), mouse, (mouse[0],altura/2), 2)
    pygame.draw.line(tela, (80,0,0), mouse, (largura/2,mouse[1]), 2)


    
    
    
    pygame.display.update()