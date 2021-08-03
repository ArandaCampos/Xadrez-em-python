#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Combinar os movimentos da torre e do bispo 
#-------------------------------------------------------

from visual import dados_do_tabuleiro
import torre
import bispo
        
def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        bispo.reconhecer_jogadas(index, 'preto', 'branco')
        torre.reconhecer_jogadas(index, 'preto', 'branco')
    else:
        bispo.reconhecer_jogadas(index, 'branco', 'preto')
        torre.reconhecer_jogadas(index, 'branco', 'preto')