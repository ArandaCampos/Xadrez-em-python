#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Localizar a casa foi clicada
# * Identicar qual peça está na casa clicada
# * Chamar a função da respectiva peça
# * Pintar as casas possíveis conforme retorno da função
#-------------------------------------------------------


from pecas import peao, torre, cavalo, rainha, rei, bispo
import validacao
from visual import dados_do_tabuleiro, dados_casas, marrom, vermelho

lista_index = []

def pintar(jogada, adversario):
    if dados_do_tabuleiro[jogada]['time'] == str(adversario):
        if str(adversario) == 'vazio':
            dados_casas[jogada]['cor'] = marrom
        else:
            dados_casas[jogada]['cor'] = vermelho

def identificar_peca(index):
    if dados_do_tabuleiro[index]['peca'] == 'peao':
        peao.reconhecer_time(index)   
    elif dados_do_tabuleiro[index]['peca'] == 'torre':
        torre.reconhecer_time(index)    
    elif dados_do_tabuleiro[index]['peca'] == 'bispo':
        bispo.reconhecer_time(index)  
    elif dados_do_tabuleiro[index]['peca'] == 'cavalo':
        cavalo.reconhecer_time(index)     
    elif dados_do_tabuleiro[index]['peca'] == 'rainha':
        rainha.reconhecer_time(index)    
    elif dados_do_tabuleiro[index]['peca'] == 'rei':
        rei.reconhecer_time(index)   
    elif dados_do_tabuleiro[index]['peca'] == 'vazio':
        pass

def localizar_click(botao_x, botao_y, click):
    for i in range(8):
        for n in range(8):
            if botao_x == i and botao_y == n:
                index = 8 * n + i
                lista_index.append(index)
                if click == True:
                    identificar_peca(index)
                else:
                    validacao.validar_jogada(index, lista_index)