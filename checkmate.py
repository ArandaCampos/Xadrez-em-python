#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * Possibilidade do rei se movimentar e sair do check
# * Possibilidade de alguma peça aliada interceptar o ataque
#
# Tarefas:
# * Possibilidade do rei se movimentar e sair do check
# * Possibilidade de alguma peça aliada interceptar o ataque
#
#-------------------------------------------------------

from pecas import rei

def movimentacaoRei(index, adversario):
    x = index % 8
    if x == 0:
        movimentacao = rei.reconhecer_casas(index, adversario, 2, 1, 8, 9, -7, -8)
    elif x == 7: 
        movimentacao = rei.reconhecer_casas(index, adversario, 2, -1, 7, 8, -8, -9)
    else:
        movimentacao = rei.reconhecer_casas(index, adversario, 2, 1, -1, 7, 8, 9, -7, -8, -9)
    
    print(movimentacao)
    if movimentacao == None:
        possibilidade_de_interceptacao()
    else:
        print('pode andar')
    
def possibilidade_de_interceptacao():
    print('possibilidade de intercecptacao')