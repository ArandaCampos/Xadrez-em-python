#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Anda uma casa em qualquer direção 
#-------------------------------------------------------

import comando, tela_check
from visual import dados_do_tabuleiro
        
def reconhecer_casas(index, adversario, finalidade = 0,* num):
    for n in num:    
        casa = 0
        casa = index + n
        if finalidade == 0:
            if casa >=0 and casa <= 63:
                comando.pintar(casa, str(adversario))
        elif dados_do_tabuleiro[casa]['peca'] == 'peao' and dados_do_tabuleiro[casa]['time'] == str(adversario):
            print('Checkmate peao')
            #tela_check.tela(True)
        else:
            pass


def reconhecer_jogadas(index, adversario):
        x = index % 8
        if x == 0:
            reconhecer_casas(index, adversario, 0, 1, 8, 9, -7, -8)
        elif x == 7: 
            reconhecer_casas(index, adversario, 0, -1, 7, 8, -8, -9)
        else:
            reconhecer_casas(index, adversario, 0, 1, -1, 7, 8, 9, -7, -8, -9)
           

def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas(index, 'branco')
        reconhecer_jogadas(index, 'vazio')
    else:
        reconhecer_jogadas(index, 'preto')
        reconhecer_jogadas(index, 'vazio')