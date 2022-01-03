#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * inicializar o loopping do jogo
# * criar os eventos 
#-------------------------------------------------------

import pygame
import visual
import comando
from visual import branco, tela, largura_tela
from pygame.constants import KEYDOWN, K_UP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT

def jogo():
    pygame.display.set_caption("Renan's Chess")
    relogio = pygame.time.Clock()
    primeiro_click = True

    while True:
        
        relogio.tick(10)
        tela.fill(branco)

        # config do mouse
        mouse = pygame.mouse.get_pos()
        pos_x = mouse[0]
        pos_y = mouse[1]
        botao_x = pos_x // 75
        botao_y = pos_y // 75
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:       
                    comando.localizar_click(botao_x, botao_y, primeiro_click)
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    primeiro_click = not primeiro_click
       
        visual.casas(largura_tela)
        visual.desenhar_tabuleiro()
        visual.posicao()
        
        pygame.display.flip()