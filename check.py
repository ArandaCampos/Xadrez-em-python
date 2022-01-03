#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Localizar o rei 
# * Escanear o tabuleiro para ver se existe um Check
# * Se existe, chamar função Checkmate
#-------------------------------------------------------

import checkmate
from visual import dados_do_tabuleiro
from pecas import cavalo, torre, rei, bispo


def localizar_rei(x = 0, y = 63):
    rei_preto = list(map(lambda p: p['coordenada'], filter(lambda p: p['peca'] == 'rei' and p['time'] == 'preto', dados_do_tabuleiro)))
    index_preto = rei_preto[0][0] // 75 + rei_preto[0][1] // 75 * 8
    rei_branco = list(map(lambda p: p['coordenada'], filter(lambda p: p['peca'] == 'rei' and p['time'] == 'branco', dados_do_tabuleiro)))
    index_branco = rei_branco[0][0] // 75 + rei_branco[0][1] // 75 * 8
    scaner_check(index_preto, index_branco)
    
def scaner_check(index_preto, index_branco, preto = 'preto', branco = 'branco'):
    retorno = []
    retorno.append(cavalo.reconhecer_jogadas(index_preto, preto, branco, 1))
    retorno.append(cavalo.reconhecer_jogadas(index_branco, branco, preto, 1))
    retorno.append(torre.reconhecer_jogadas(index_preto, preto, branco, 1))
    retorno.append(torre.reconhecer_jogadas(index_branco, branco, preto, 1))
    retorno.append(bispo.reconhecer_jogadas(index_preto, preto, branco, 1))
    retorno.append(bispo.reconhecer_jogadas(index_branco, branco, preto, 1))
    retorno.append(rei.reconhecer_casas(index_preto, branco, 1, 7, 9))
    retorno.append(rei.reconhecer_casas(index_branco, preto, 1, -7, -9))

    analise_retorno =  list(filter(lambda p: p != None, retorno))
    del retorno
    peca = []

    # peca= [(peça, time), (peca, time)]
    for i in range(len(analise_retorno)):
        peca_time = analise_retorno[i]['peca'], analise_retorno[i]['time']
        peca.append(peca_time)
        if analise_retorno[i]['time'] == 'preto':    
            checkmate.movimentacaoRei(index_preto, peca[0][1])
