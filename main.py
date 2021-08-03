#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * inicializar pygame
# * chamar as funções visual e game 
#-------------------------------------------------------

import pygame

import game

pygame.init()

game.jogo()


#-------------------------------------------------------
# Falta implementar
# * bug: quando o peão ainda não sofreu nenhuma jogada, ele consegue andar duas casas mesmo com uma peça a sua frente 
# * Testar recursividade no Bispo e na Torre e verificar a velocidade de processamento
# * checkmate
# * Quando o peão chegar na extremidade oposta ele pode virar um bispo, ou cavalo, ou torre, ou dama
# * Tela de restart 
#-------------------------------------------------------
            