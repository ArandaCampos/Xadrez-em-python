#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Anda uma casa em qualquer direção 
# * finalidade: 0 = mapaer jogadas
#               1 = Check de peões e damas
#               2 = Possivel movimentação do rei em check
#-------------------------------------------------------

import checkmate
import comando
from visual import dados_do_tabuleiro
        
def reconhecer_casas(index, adversario, finalidade,* num):
    for n in num:    
        casa = 0
        casa = index + n
        if casa >=0 and casa <= 63:
            if finalidade == 0:
                comando.pintar(casa, str(adversario))
            elif finalidade == 1 and dados_do_tabuleiro[casa]['peca'] == 'peao' and dados_do_tabuleiro[casa]['time'] == str(adversario):
                return dados_do_tabuleiro[casa]
            elif finalidade == 2:
                if dados_do_tabuleiro[casa]['peca'] == str(adversario) or dados_do_tabuleiro[casa]['peca'] == 'vazio':
                    return True

def reconhecer_jogadas(index, adversario, finalidade):
        x = index % 8
        if x == 0:
            reconhecer_casas(index, adversario, finalidade, 1, 8, 9, -7, -8)
        elif x == 7: 
            reconhecer_casas(index, adversario, finalidade, -1, 7, 8, -8, -9)
        else:
            reconhecer_casas(index, adversario, finalidade, 1, -1, 7, 8, 9, -7, -8, -9)
           
def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas(index, 'branco', finalidade = 0)
        reconhecer_jogadas(index, 'vazio', finalidade = 0)
    else:
        reconhecer_jogadas(index, 'preto', finalidade = 0)
        reconhecer_jogadas(index, 'vazio', finalidade = 0)