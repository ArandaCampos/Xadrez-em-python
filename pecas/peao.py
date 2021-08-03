#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Só anda uma casa no eixo X
# * Só come nas diagonais 1 casa 
#-------------------------------------------------------

import comando
from visual import dados_do_tabuleiro

def reconhecer_jogadas_preto(index):
    if dados_do_tabuleiro[index]['dados'] == False:
        comando.pintar(index + 8, 'vazio')
        if index % 8 == 0:
            comando.pintar(index + 9, 'branco')
        elif index % 8 == 7:
            comando.pintar(index + 7, 'branco')
        else:
            comando.pintar(index + 9, 'branco')
            comando.pintar(index + 7, 'branco')
    else:
        comando.pintar(index + 8, 'vazio')
        comando.pintar(index + 9, 'branco')
        comando.pintar(index + 7, 'branco')
        comando.pintar(index + 16, 'vazio')
        
        
def reconhecer_jogadas_branco(index):
    if dados_do_tabuleiro[index]['dados'] == False:    
        comando.pintar(index - 8, 'vazio')
        if index % 8 == 0:
            comando.pintar(index - 7, 'preto')
        elif index % 8 == 7:
            comando.pintar(index - 9, 'preto')
        else:
            comando.pintar(index - 9, 'preto')
            comando.pintar(index - 7, 'preto')
    else:
        comando.pintar(index - 8, 'vazio')
        comando.pintar(index - 9, 'preto')
        comando.pintar(index - 7, 'preto')
        comando.pintar(index - 16, 'vazio')

def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas_preto(index)
    else:
        reconhecer_jogadas_branco(index)