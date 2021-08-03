#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Validar se a jogada está correta
# * Restaurar a cor do tabuleiro 
#-------------------------------------------------------

import checkmate
from visual import dados_do_tabuleiro, dados_casas, marrom_claro, marrom, marrom_escuro, vermelho, musica_andar

c = 0

def efetuar_jogada(index, lista_index):
    dados_do_tabuleiro[index]['peca'] = dados_do_tabuleiro[lista_index[0]]['peca'] 
    dados_do_tabuleiro[index]['time'] = dados_do_tabuleiro[lista_index[0]]['time']
    dados_do_tabuleiro[index]['dados'] = dados_do_tabuleiro[lista_index[0]]['dados']
    dados_do_tabuleiro[lista_index[0]]['dados'] = 'vazio'    
    dados_do_tabuleiro[lista_index[0]]['peca'] = 'vazio'
    dados_do_tabuleiro[lista_index[0]]['time'] = 'vazio'
    dados_do_tabuleiro[index]['dados'] = False
    musica_andar.play()
    checkmate.localizar_rei()

def restaurar_cor(lista_index):
    for n in range(8):
        for i in range(8):
            index = 8 * n + i
            if (i + n) % 2 == 0:
                dados_casas[index]['cor'] = marrom_claro
            else:
                dados_casas[index]['cor'] = marrom_escuro
    lista_index.clear()
    
def jogador_da_vez():
    global c
    c += 1

def validar_jogada(index, lista_index): 
    if c % 2 == 0 and dados_do_tabuleiro[lista_index[0]]['time'] == 'preto':
        if dados_casas[index]['cor'] == marrom or dados_casas[index]['cor'] == vermelho:
            jogador_da_vez()
            efetuar_jogada(index, lista_index)
            restaurar_cor(lista_index)
        else:
            restaurar_cor(lista_index)
    elif c % 2 == 1 and dados_do_tabuleiro[lista_index[0]]['time'] == 'branco':
        if dados_casas[index]['cor'] == marrom or dados_casas[index]['cor'] == vermelho:
            jogador_da_vez()
            efetuar_jogada(index, lista_index)
            restaurar_cor(lista_index)
        else:
            restaurar_cor(lista_index)
    else:
        restaurar_cor(lista_index)
    