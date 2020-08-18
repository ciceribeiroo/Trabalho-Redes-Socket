#!/usr/bin/python3

#---------------------------------------------------------#
# Implementacao das regras do Jogo da Velha.              #
#---------------------------------------------------------#
from os import system
import random

def quemComeca():
    r = random.randint(1,2)
    if r==1:
        return False
    else:
        return True
##-------------------------------------------------##
## Imprime regras do jogo                          ##
##-------------------------------------------------##
def imprimeRegras(jogador):
    system("clear") # Limpa a tela (somente linux)
    
    # Imprime instruções do jogo na tela
    print("##------------------------------------------------------------##")
    print("##------------------------ BATALHA NAVAL ---------------------##")
    print("##------------------------------------------------------------##")
    print("##                          ~INSTRUÇÕES~                      ##")
    print("## Você é o jogador ", jogador, ". Para sair do jogo, digite 'sair'    ##")
    return

##-------------------------------------------------##
## Imprime tabuleiro                               ##
##-------------------------------------------------##
def imprimeSeuTabuleiro(tabuleiro):
    
    print("Defenda |o|")
    print(" ")
    print("  0   1   2   3   4   5   6   7   8   9  ")
    print("  ______________________________________")
    print("a| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2], tabuleiro[0][3], tabuleiro[0][4], tabuleiro[0][5], tabuleiro[0][6], tabuleiro[0][7], tabuleiro[0][8],tabuleiro[0][9]) )
    print("  --------------------------------------")
    print("b| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2], tabuleiro[1][3], tabuleiro[1][4], tabuleiro[1][5], tabuleiro[1][6], tabuleiro[1][7], tabuleiro[1][8],tabuleiro[1][9]) )
    print("  ---------------------------------------")
    print("c| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2], tabuleiro[2][3], tabuleiro[2][4], tabuleiro[2][5], tabuleiro[2][6], tabuleiro[2][7], tabuleiro[2][8],tabuleiro[2][9]) )
    print(" ---------------------------------------")
    print("d| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[3][0], tabuleiro[3][1], tabuleiro[3][2], tabuleiro[3][3], tabuleiro[3][4], tabuleiro[3][5], tabuleiro[3][6], tabuleiro[3][7], tabuleiro[3][8],tabuleiro[3][9]) )
    print(" ---------------------------------------")
    print("e| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[4][0], tabuleiro[4][1], tabuleiro[4][2], tabuleiro[4][3], tabuleiro[4][4], tabuleiro[4][5], tabuleiro[4][6], tabuleiro[4][7], tabuleiro[4][8],tabuleiro[4][9]) )
    print(" ---------------------------------------")
    print("f| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[5][0], tabuleiro[5][1], tabuleiro[5][2], tabuleiro[5][3], tabuleiro[5][4], tabuleiro[5][5], tabuleiro[5][6], tabuleiro[5][7], tabuleiro[5][8],tabuleiro[5][9]) )
    print("  ---------------------------------------")
    print("g| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
           % ( tabuleiro[6][0], tabuleiro[6][1], tabuleiro[6][2], tabuleiro[6][3], tabuleiro[6][4], tabuleiro[6][5], tabuleiro[6][6], tabuleiro[6][7], tabuleiro[6][8],tabuleiro[6][9]) )
    print("  -------------------------")
    print("h| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
           % ( tabuleiro[7][0], tabuleiro[7][1], tabuleiro[7][2], tabuleiro[7][3], tabuleiro[7][4], tabuleiro[7][5], tabuleiro[7][6], tabuleiro[7][7], tabuleiro[7][8],tabuleiro[7][9]) )
    print("  ---------------------------------------")
    print("i| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[8][0], tabuleiro[8][1], tabuleiro[8][2], tabuleiro[8][3], tabuleiro[8][4], tabuleiro[8][5], tabuleiro[8][6], tabuleiro[8][7], tabuleiro[8][8],tabuleiro[8][9]) )
    print("  ---------------------------------------")
    print("j| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[9][0], tabuleiro[9][1], tabuleiro[9][2], tabuleiro[9][3], tabuleiro[9][4], tabuleiro[9][5], tabuleiro[9][6], tabuleiro[9][7], tabuleiro[9][8],tabuleiro[9][9]) )
    print("  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
    return

def imprimeTabuleiroOponente():
    
    print("Ataque |o|")
    print(" ")
    print("  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
    print("  0   1   2   3   4   5   6   7   8   9  ")
    print("  ---------------------------------------")
    print("a| - | - | - | - | - | - | - | - | - | - ") 
    print("  ---------------------------------------")
    print("b| - | - | - | - | - | - | - | - | - | - ")
    print("  ---------------------------------------")
    print("c| - | - | - | - | - | - | - | - | - | - ") 
    print("  ---------------------------------------")
    print("d| - | - | - | - | - | - | - | - | - | - ")
    print("  ---------------------------------------")
    print("e| - | - | - | - | - | - | - | - | - | - ") 
    print("  ---------------------------------------")
    print("f| - | - | - | - | - | - | - | - | - | - ")
    print("  ---------------------------------------")
    print("g| - | - | - | - | - | - | - | - | - | - ") 
    print("  ---------------------------------------")
    print("h| - | - | - | - | - | - | - | - | - | - ")
    print("  ---------------------------------------")
    print("i| - | - | - | - | - | - | - | - | - | - ") 
    print("  ---------------------------------------")
    print("j| - | - | - | - | - | - | - | - | - | - ")
    print("  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
    return


##-------------------------------------------------##
## Cria tabuleiro                                  ##
##-------------------------------------------------##
def criaTabuleiro():
	novoTabuleiro = []
	for _ in range(10):
		novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
	return novoTabuleiro

##-------------------------------------------------##
## Validar a jogada                                ##
##-------------------------------------------------##
def validaJogada(tabuleiro, jogada) :
    
    # Verifica se a entrada é um comando de saída, o que é válido
    if jogada == "sair" : 
        return True
    
    # Verifica se a entrada está no tipo 'LC' (linhaxcoluna)
    if len(jogada) != 2 :
        print("\tO formato correto é LC!") 
        return False
    
    # Verifica se os números da entrada possuem intervalo definido entre 0 e 2 e A e C
    if int(jogada[0]) < 0 or int(jogada[0]) > 2 or int(jogada[1]) < 0 or int(jogada[1]) > 2: 
        print("\tAs coordenadas devem estar no intervalo 0 a 2!")
        return False
    
    # Verifica se a entrada corresponde a uma jogada que foi feita anteriormente
    if tabuleiro[int(jogada[0])][int(jogada[1])] != '-':
        print("\tjogada já foi feita!") 
        return False
    
    # Retorna true se depois de todas as verificações, a entrada é valida
    return True


##-------------------------------------------------##
## Função que verifica se foi empate.              ##
## O empate ocorre quando se percorre todo o tabu- ##
## leiro e nao ha posicoes vazias.                 ##
##-------------------------------------------------##
def empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '-':
                return False
    return True

##-------------------------------------------------##
## Verificar fim de jogo                           ##
## Funçao que verifica se o jogo terminou em       ##
## (vitoria/derrota ou empate).                    ##
# retorna:                                         ##
#   0 - continua o jogo                            ##
#   1 - houve vitória                              ##
#   2 - empate                                     ##
##-------------------------------------------------##
def fimDeJogo(tabuleiro):
    
    # verifica vitoria pelas linhas
    # a vitória ocorre quando todas as linhas são percorridas
    # e há a ocorrência de X,X,X ou O,O,O 
    for linha in tabuleiro:
        if linha == ['X','X','X'] or linha == ['O','O','O']:
            return 1
    
    
    # verifica vitoria pelas colunas
    # as colunas são transformadas em linhas para facilitar a verificação
    # e a vitória ocorre quando todas as linhas são percorridas
    # e há ocorrência de X,X,X ou O,O,O
    for i in range(3) :
        coluna = []
        for j in range(3):
            coluna.append(tabuleiro[j][i])
        if coluna == ['X','X','X'] or coluna == ['O','O','O']:
            return 1
        
    # verifica diagonal principal
    # a diagonal principal [i][i] por meio de uma função é transformada em uma linha
    # para facilitar a verificação
    # e a vitória ocorre quando toda a linha é percorrida
    # e há ocorrência de X,X,X ou O,O,O
    diagonal = []
    for i in range(3):
        diagonal.append(tabuleiro[i][i])
    if diagonal == ['X','X','X'] or diagonal == ['O','O','O']:
        return 1
    
    # verifica diagonal secundaria
    # a diagonal secundária [i][2-i] por meio de uma função é transformada em uma linha
    # para facilitar a verificação
    # e a vitória ocorre quando toda a linha é percorrida
    # e há ocorrência de X,X,X ou O,O,O
    diagonal = []
    for i in range(3):
        diagonal.append(tabuleiro[i][2-i])
    if diagonal == ['X','X','X'] or diagonal == ['O','O','O']:
        return 1
    
    
    # Se depois de fazer a verificação por linhas, colunas 
    # e diagonais ninguém venceu, verifica se foi empate
    # chamando a função empate e passando o tabuleiro como parâmetro.
    if empate(tabuleiro):
        return 2
    
    # Se não houve vitória ou empate, o jogo continua, então retorna 0
    return 0