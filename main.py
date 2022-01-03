#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * inicializar pygame
# * chamar as funções game
#-------------------------------------------------------

import pygame

import game

pygame.init()

game.jogo()

#-------------------------------------------------------
# Falta implementar
# * bug: quando o peão ainda não sofreu nenhuma jogada, ele consegue andar duas casas mesmo com uma peça a sua frente
# * checkmate
# * Quando o peão chegar na extremidade oposta ele pode tornar-se um bispo, ou cavalo, ou torre, ou dama
# ------------------------------------------------------
# Futuras implementações
# * Telas de menu inicial, recomeçar, checkmate
# * Cronometro
#-------------------------------------------------------

