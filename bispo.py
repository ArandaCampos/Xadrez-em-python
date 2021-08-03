#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Anda na diagonal até a próxima peça
# * Só come a primeira peça do oponente nas diagonais 
#-------------------------------------------------------

import comando
from visual import dados_do_tabuleiro

def reconhecer_jogadas(index, aliado, adversario, finalidade = 0):
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            vertical = 1
            horizontal = 1
            continuar = True
            y = index // 8 + i
            x = index % 8 + j
            posicao = index + vertical * i * 8 + j * horizontal
            while y >= 0 and y <= 7 and x >= 0 and x <= 7 and dados_do_tabuleiro[posicao]['time'] != str(aliado) and continuar == True:  
                if finalidade == 0:
                    if dados_do_tabuleiro[posicao]['peca'] == 'vazio':   
                        comando.pintar(posicao, 'vazio')
                    else:
                        comando.pintar(posicao, str(adversario))
                        continuar = False
                elif dados_do_tabuleiro[posicao]['peca'] == 'bispo' or dados_do_tabuleiro[posicao]['peca'] == 'rainha':
                    print('Checkmate bispo')
                    continuar = False
                else:
                    pass
                vertical += 1
                horizontal += 1
                posicao = index + vertical * i * 8 + j * horizontal
                x = x + j
                y += i
        
def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas(index, 'preto', 'branco')
    else:
        reconhecer_jogadas(index, 'branco', 'preto')