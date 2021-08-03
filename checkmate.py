from visual import dados_do_tabuleiro
import cavalo, torre, bispo, rei

def localizar_rei(x = 0, y = 63):
    while dados_do_tabuleiro[x]['peca'] != 'rei':
        x += 1
        
    while dados_do_tabuleiro[y]['peca'] != 'rei':
        y -= 1

    cavalo.reconhecer_jogadas(x, 'preto', 'branco', 1)
    cavalo.reconhecer_jogadas(y, 'branco', 'preto', 1)
    torre.reconhecer_jogadas(x, 'preto', 'branco', 1)
    torre.reconhecer_jogadas(y, 'branco', 'preto', 1)
    bispo.reconhecer_jogadas(x, 'preto', 'branco', 1)
    bispo.reconhecer_jogadas(y, 'branco', 'preto', 1)
    rei.reconhecer_casas(x, 'branco', 1, 7, 9)
    rei.reconhecer_casas(y, 'preto', 1, -7, -9)