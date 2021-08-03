import pygame
from pygame.constants import KEYDOWN, K_r
from visual import largura_tela, altura_tela, tela    

def tela(cont):
    while cont:
        # Config da tela de Game Over
        tela.fill((18, 18, 18))

        # titulo
        font_2 = pygame.font.SysFont('Arial', 42, True, False)
        mensagem_over = f'Check Mate!'
        text_over = font_2.render(mensagem_over, True, (250, 250, 250))
        text_over_format = text_over.get_rect()
        text_over_format.center = (largura_tela // 2, altura_tela // 2 - 18)
        tela.blit(text_over, text_over_format)

        # condicional para finalizar o jogo
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_r:
                    cont = False
