#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Anda tanto para frente quanto para trás
# * Anda no eixo Y ou X até a próxima peça
# * Come a primeira peça no eixo X ou Y adversária 
#-------------------------------------------------------

import comando
from visual import dados_do_tabuleiro
       
def reconhecer_jogadas(index, aliado, adversario, finalidade = 0):
    for i in range(-1,2,2):
        n = 1
        continuar = True
        posicao = 0 
        posicao = index + i * 8 * n
        while posicao >= 0 and posicao <= 63 and dados_do_tabuleiro[posicao]['time'] != str(aliado) and continuar == True:  
            if finalidade == 0:
                if dados_do_tabuleiro[posicao]['peca'] == 'vazio':   
                    comando.pintar(posicao, 'vazio')
                else:
                    comando.pintar(posicao, str(adversario))
                    continuar = False
            else:
                if dados_do_tabuleiro[posicao]['peca'] == 'torre' or dados_do_tabuleiro[posicao]['peca'] == 'rainha':
                    print('Checkmate torre')
                    continuar = False
                elif dados_do_tabuleiro[posicao]['peca'] == 'vazio':
                    pass
            n +=1
            posicao = index + i * 8 * n

    for i in range(-1,2,2):
        n = 1
        continuar = True
        posicao = index + 1 * i
        y = index // 8
        x = index - y * 8
        x = x + 1 * i
        while x >= 0 and x <= 7 and dados_do_tabuleiro[posicao]['time'] != str(aliado) and continuar == True:  
            if dados_do_tabuleiro[posicao]['peca'] == 'vazio':   
                comando.pintar(posicao, 'vazio')
            else:
                comando.pintar(posicao, str(adversario))
                continuar = False
            n +=1
            x = x + 1 * i
            posicao = index + i * n  

def reconhecer_time(index):
    if dados_do_tabuleiro[index]['time'] == 'preto':
        reconhecer_jogadas(index, 'preto', 'branco')
    else:
        reconhecer_jogadas(index, 'branco', 'preto')