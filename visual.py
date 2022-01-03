#-------------------------------------------------------
# Autor: Renan Aranda
# Projeto: Xadrez em Python
#
# Implementação:
# * configurar tela, tabuleiro, casas e peças
# * determinar as posições iniciais das peças 
#
# Dados Importantes:
# * dados_do_tabuleiro [{peca: , time: ,  coordenada: , dados: }] // Lista que armazena todos os dados do tabuleiro
#-------------------------------------------------------

import pygame
import os
import pygame

pygame.init()

# Config da Tela-----------------------------------------------------------------------
largura_tela, altura_tela = 600, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Paleta de cores
branco = (220,220,220)
marrom_escuro = (92,60,10)
marrom_claro = (225,174,92)
marrom = (191, 126, 21)
vermelho = (250, 26, 21)

# Variáveis que armazenam o caminho para os diretorios-----------------------------------
diretorio_principal = os.path.dirname(__file__)
diretorio_imagem = os.path.join(diretorio_principal, 'imagens')
diretorio_audio = os.path.join(diretorio_principal, 'audio')

# Carregar audio-----------------------------------------------------------------------------
musica_andar = pygame.mixer.Sound(os.path.join(diretorio_audio, 'mover_peca.wav'))
musica_comer = pygame.mixer.Sound(os.path.join(diretorio_audio, 'comer_peca.wav'))

# Carregar as ilustrações das peças----------------------------------------------------------
peao_preto = pygame.image.load(os.path.join(diretorio_imagem, 'peao_preto.png')).convert_alpha()
peao_preto = pygame.transform.scale(peao_preto, (45,50))

peao_branco = pygame.image.load(os.path.join(diretorio_imagem, 'peao_branco.png')).convert_alpha()
peao_branco = pygame.transform.scale(peao_branco, (45,50))

torre_preto = pygame.image.load(os.path.join(diretorio_imagem, 'torre_preto.png')).convert_alpha()
torre_preto = pygame.transform.scale(torre_preto, (45,50))

torre_branco = pygame.image.load(os.path.join(diretorio_imagem, 'torre_branco.png')).convert_alpha()
torre_branco = pygame.transform.scale(torre_branco, (45,50))

cavalo_preto = pygame.image.load(os.path.join(diretorio_imagem, 'cavalo_preto.png')).convert_alpha()
cavalo_preto = pygame.transform.scale(cavalo_preto, (45,50))

cavalo_branco = pygame.image.load(os.path.join(diretorio_imagem, 'cavalo_branco.png')).convert_alpha()
cavalo_branco = pygame.transform.scale(cavalo_branco, (45,50))

bispo_preto = pygame.image.load(os.path.join(diretorio_imagem, 'bispo_preto.png')).convert_alpha()
bispo_preto = pygame.transform.scale(bispo_preto, (45,50))

bispo_branco = pygame.image.load(os.path.join(diretorio_imagem, 'bispo_branco.png')).convert_alpha()
bispo_branco = pygame.transform.scale(bispo_branco, (45,50))

rainha_preto = pygame.image.load(os.path.join(diretorio_imagem, 'rainha_preto.png')).convert_alpha()
rainha_preto = pygame.transform.scale(rainha_preto, (45,50))

rainha_branco = pygame.image.load(os.path.join(diretorio_imagem, 'rainha_branco.png')).convert_alpha()
rainha_branco = pygame.transform.scale(rainha_branco, (45,50))

rei_preto = pygame.image.load(os.path.join(diretorio_imagem, 'rei_preto.png')).convert_alpha()
rei_preto = pygame.transform.scale(rei_preto, (45,50))

rei_branco = pygame.image.load(os.path.join(diretorio_imagem, 'rei_branco.png')).convert_alpha()
rei_branco = pygame.transform.scale(rei_branco, (45,50))

coordenadas_casa = dict()
dados_casas = []

# Cria casas do tabuleiro e armazena as coordenadas-----------------------------------------------
def casas(largura_tela):
    for n in range(8):
        for i in range(8):
            casa_x_y = (largura_tela / 8 * i, largura_tela / 8 * n, 75, 75)
            if (i + n) % 2 == 0: 
                coordenadas_casa = {'cor': marrom_claro, 'coordenadas': casa_x_y}
                dados_casas.append(coordenadas_casa)
            else:
                coordenadas_casa = {'cor': marrom_escuro, 'coordenadas': casa_x_y}    
                dados_casas.append(coordenadas_casa) 
                           
# Desenha as peças no tabuleiro-----------------------------------------------------------------------
def desenhar_tabuleiro():
    for i in range(8):
        for n in range(8):
            c = i * 8 + n
            pygame.draw.rect(tela, dados_casas[c]['cor'], dados_casas[c]['coordenadas'])
        

dados_do_tabuleiro = []
dados = dict()

# Gera os dados de todo o jogo-----------------------------------------------------------------
for n in range(8):
    for i in range(8):
        x = int(largura_tela / 8 * i + 15)
        y = int(largura_tela / 8 * n + 12)
        coordenada = (x, y)
        dados = {'peca': 'vazio','time': 'vazio', 'coordenada': coordenada, 'dados': False} 
        dados_do_tabuleiro.append(dados)
        
for i in range(8):
    index = i + 8
    dados_do_tabuleiro[index]['peca'] = 'peao'
    dados_do_tabuleiro[index]['time'] = 'preto'
    dados_do_tabuleiro[index]['dados'] = True
    
for i in range(8):    
    index_b = i + 48
    dados_do_tabuleiro[index_b]['peca'] = 'peao'
    dados_do_tabuleiro[index_b]['time'] = 'branco'
    dados_do_tabuleiro[index_b]['dados'] = True

dados_do_tabuleiro[0]['peca'] = 'torre'
dados_do_tabuleiro[0]['time'] = 'preto'

dados_do_tabuleiro[7]['peca'] = 'torre'
dados_do_tabuleiro[7]['time'] = 'preto'

dados_do_tabuleiro[56]['peca'] = 'torre'
dados_do_tabuleiro[56]['time'] = 'branco'

dados_do_tabuleiro[63]['peca'] = 'torre'
dados_do_tabuleiro[63]['time'] = 'branco'

dados_do_tabuleiro[1]['peca'] = 'cavalo'
dados_do_tabuleiro[1]['time'] = 'preto'

dados_do_tabuleiro[6]['peca'] = 'cavalo'
dados_do_tabuleiro[6]['time'] = 'preto'

dados_do_tabuleiro[57]['peca'] = 'cavalo'
dados_do_tabuleiro[57]['time'] = 'branco'

dados_do_tabuleiro[62]['peca'] = 'cavalo'
dados_do_tabuleiro[62]['time'] = 'branco'

dados_do_tabuleiro[2]['peca'] = 'bispo'
dados_do_tabuleiro[2]['time'] = 'preto'

dados_do_tabuleiro[5]['peca'] = 'bispo'
dados_do_tabuleiro[5]['time'] = 'preto'

dados_do_tabuleiro[58]['peca'] = 'bispo'
dados_do_tabuleiro[58]['time'] = 'branco'

dados_do_tabuleiro[61]['peca'] = 'bispo'
dados_do_tabuleiro[61]['time'] = 'branco'

dados_do_tabuleiro[3]['peca'] = 'rainha'
dados_do_tabuleiro[3]['time'] = 'preto'

dados_do_tabuleiro[59]['peca'] = 'rainha'
dados_do_tabuleiro[59]['time'] = 'branco'

dados_do_tabuleiro[4]['peca'] = 'rei'
dados_do_tabuleiro[4]['time'] = 'preto'

dados_do_tabuleiro[60]['peca'] = 'rei'
dados_do_tabuleiro[60]['time'] = 'branco'

def posicao():
    for i in range(64):
        if dados_do_tabuleiro[i]['peca'] == 'peao' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(peao_preto, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'peao' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(peao_branco, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'torre' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(torre_preto, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'torre' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(torre_branco, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'cavalo' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(cavalo_preto, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'cavalo' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(cavalo_branco, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'bispo' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(bispo_preto, dados_do_tabuleiro[i]['coordenada'])
        elif  dados_do_tabuleiro[i]['peca'] == 'bispo' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(bispo_branco, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'rainha' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(rainha_preto, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'rainha' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(rainha_branco, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'rei' and dados_do_tabuleiro[i]['time'] == 'preto':    
            tela.blit(rei_preto, dados_do_tabuleiro[i]['coordenada'])
        elif dados_do_tabuleiro[i]['peca'] == 'rei' and dados_do_tabuleiro[i]['time'] == 'branco':
            tela.blit(rei_branco, dados_do_tabuleiro[i]['coordenada'])
        else:
            pass

tela.blit(peao_preto, dados_do_tabuleiro[8]['coordenada'])

