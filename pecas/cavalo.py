#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Anda em L com no máximo 3 casas
# * Só come na ponta da trajetória do L 
#-------------------------------------------------------

import comando
from visual import dados_do_tabuleiro
       
def reconhecer_jogadas(index, aliado, adversario, finalidade = 0):
    continuar = True
    for sentido_y in range(-1,2,2):
        for sentido_x in range(-1,2,2):
            for modulo_y in range(1,3):
                modulo_x = 3 - modulo_y 
                y = index // 8 + modulo_y * sentido_y
                x = index % 8 + modulo_x * sentido_x
                posicao = y * 8 + x
                if y >= 0 and y <= 7 and x >= 0 and x <= 7 and posicao <= 63 and dados_do_tabuleiro[posicao]['time'] != str(aliado) and continuar == True: 
                    if finalidade == 0:
                        if dados_do_tabuleiro[posicao]['peca'] == 'vazio':   
                            comando.pintar(posicao, 'vazio')
                        else:
                            comando.pintar(posicao, str(adversario))
                    elif dados_do_tabuleiro[posicao]['peca'] == 'cavalo' or dados_do_tabuleiro[posicao]['peca'] == 'rainha':
                        return dados_do_tabuleiro[posicao]
                    else:
                        pass

         
def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas(index, 'preto', 'branco')
    else:
        reconhecer_jogadas(index, 'branco', 'preto')
    