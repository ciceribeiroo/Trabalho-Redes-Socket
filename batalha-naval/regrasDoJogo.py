from os import system
import random

def quemComeca():
    r = random.randint(1,2)
    if(r == 1):
        return '1'
    return '2'

def colocarNavios(tabuleiro):
    print("Defina seus navios no tabuleiro")
    posicao =0
    direcao = ""
    print("Vamos começar pelo porta-avião")
    posicao= input("Insira a posição do navio(LC): ")
    comSucesso = validaJogada(tabuleiro, posicao)
    while not comSucesso:
        print("Posicao errada! Tente novamente")
        posicao= input("Insira a posição do navio(LC): ")
        comSucesso = validaJogada(tabuleiro, posicao)
    direcaoCorreta = False
    while not direcaoCorreta:
        direcao = input("Insira a direção do navio(v/h): ")
        if( direcao == 'v' or direcao == 'h'):
            definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, 5)
            direcaoCorreta = True
    
    na=1
    while na>= 2:
        print("Agora vamos posicionar o navio-tanque "+ na)
        print("Vamos começar pelo porta-avião")
        posicao= input("Insira a posição do navio(LC): ")
        comSucesso = validaJogada(tabuleiro, posicao)
        while not comSucesso:
            print("Posicao errada! Tente novamente")
            posicao= input("Insira a posição do navio(LC): ")
            comSucesso = validaJogada(tabuleiro, posicao)

        direcaoCorreta = False
        while not direcaoCorreta:
            direcao = input("Insira a direção do navio(v/h): ")
            if( direcao == 'v' or direcao == 'h'):
                colocarComSucesso = definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, 4)
                direcaoCorreta = True
        na = na + 1

    ct = 1
    while ct >= 3:
        print("Agora vamos posicionar o contra-torpedo "+ ct)
        posicao= input("Insira a posição do navio(LC): ")
        comSucesso = validaJogada(tabuleiro, posicao)
        while not comSucesso:
            print("Posicao errada! Tente novamente")
            posicao= input("Insira a posição do navio(LC): ")
            comSucesso = validaJogada(tabuleiro, posicao)
        direcaoCorreta = False
        while not direcaoCorreta:
            direcao = input("Insira a direção do navio(v/h): ")
            if( direcao == 'v' or direcao == 'h'):
                colocarComSucesso = definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, 3)
                direcaoCorreta = True
        ct = ct + 1

    s=1
    while s >= 4:
        print("Agora vamos posicionar o submarino "+ s)
        posicao= input("Insira a posição do navio(LC): ")
        comSucesso = validaJogada(tabuleiro, posicao)
        while not comSucesso:
            print("Posicao errada! Tente novamente")
            posicao= input("Insira a posição do navio(LC): ")
            comSucesso = validaJogada(tabuleiro, posicao)
        direcaoCorreta = False
        while not direcaoCorreta:
            direcao = input("Insira a direção do navio(v/h): ")
            if( direcao == 'v' or direcao == 'h'):
                colocarComSucesso = definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, 2)
                direcaoCorreta = True
        s = s + 1

def definirNavios(tabuleiro, linha, coluna, direcao, tamanho):
    if direcao == 'h':
        if(int(linha)+tamanho >9):
            return False
        while tamanho > 0:
            if tabuleiro[linha][coluna] == 'O':
                return False
            tabuleiro[linha][coluna] = 'O'
            tamanho = tamanho - 1
            linha = linha + 1
    else:
        if(int(coluna)+tamanho >9):
            return False
        while tamanho > 0:
            if tabuleiro[linha][coluna] == 'O':
                return False
            tabuleiro[linha][coluna] = 'O'
            tamanho = tamanho - 1
            coluna = coluna + 1
    return True

def imprimeRegras(jogador):    
    print("##------------------------------------------------------------##")
    print("##------------------------ BATALHA NAVAL ---------------------##")
    print("##------------------------------------------------------------##")
    print("##                          ~INSTRUÇÕES~                      ##")
    print("## Você é o jogador ", jogador, ". Para sair do jogo, digite 'sair'    ##")
    return

def imprimirTabuleiros(tabuleiro1, tabuleiro2):
    print("Defenda |o|")
    imprimeTabuleiro(tabuleiro1)
    print("Ataque |o|")
    imprimeTabuleiro(tabuleiro2)

def imprimeTabuleiro(tabuleiro):
    
    print(" ")
    print("  0   1   2   3   4   5   6   7   8   9  ")
    print("  ______________________________________")
    print("0| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2], tabuleiro[0][3], tabuleiro[0][4], tabuleiro[0][5], tabuleiro[0][6], tabuleiro[0][7], tabuleiro[0][8],tabuleiro[0][9]) )
    print("  --------------------------------------")
    print("1| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2], tabuleiro[1][3], tabuleiro[1][4], tabuleiro[1][5], tabuleiro[1][6], tabuleiro[1][7], tabuleiro[1][8],tabuleiro[1][9]) )
    print("  ---------------------------------------")
    print("2| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2], tabuleiro[2][3], tabuleiro[2][4], tabuleiro[2][5], tabuleiro[2][6], tabuleiro[2][7], tabuleiro[2][8],tabuleiro[2][9]) )
    print(" ---------------------------------------")
    print("3| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[3][0], tabuleiro[3][1], tabuleiro[3][2], tabuleiro[3][3], tabuleiro[3][4], tabuleiro[3][5], tabuleiro[3][6], tabuleiro[3][7], tabuleiro[3][8],tabuleiro[3][9]) )
    print(" ---------------------------------------")
    print("4| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[4][0], tabuleiro[4][1], tabuleiro[4][2], tabuleiro[4][3], tabuleiro[4][4], tabuleiro[4][5], tabuleiro[4][6], tabuleiro[4][7], tabuleiro[4][8],tabuleiro[4][9]) )
    print(" ---------------------------------------")
    print("5| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[5][0], tabuleiro[5][1], tabuleiro[5][2], tabuleiro[5][3], tabuleiro[5][4], tabuleiro[5][5], tabuleiro[5][6], tabuleiro[5][7], tabuleiro[5][8],tabuleiro[5][9]) )
    print("  ---------------------------------------")
    print("6| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
           % ( tabuleiro[6][0], tabuleiro[6][1], tabuleiro[6][2], tabuleiro[6][3], tabuleiro[6][4], tabuleiro[6][5], tabuleiro[6][6], tabuleiro[6][7], tabuleiro[6][8],tabuleiro[6][9]) )
    print("  -------------------------")
    print("7| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
           % ( tabuleiro[7][0], tabuleiro[7][1], tabuleiro[7][2], tabuleiro[7][3], tabuleiro[7][4], tabuleiro[7][5], tabuleiro[7][6], tabuleiro[7][7], tabuleiro[7][8],tabuleiro[7][9]) )
    print("  ---------------------------------------")
    print("8| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[8][0], tabuleiro[8][1], tabuleiro[8][2], tabuleiro[8][3], tabuleiro[8][4], tabuleiro[8][5], tabuleiro[8][6], tabuleiro[8][7], tabuleiro[8][8],tabuleiro[8][9]) )
    print("  ---------------------------------------")
    print("9| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro[9][0], tabuleiro[9][1], tabuleiro[9][2], tabuleiro[9][3], tabuleiro[9][4], tabuleiro[9][5], tabuleiro[9][6], tabuleiro[9][7], tabuleiro[9][8],tabuleiro[9][9]) )
    print("  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
    return

def criaTabuleiro():
	novoTabuleiro = []
	for _ in range(10):
		novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
	return novoTabuleiro


def validaJogada(tabuleiro, jogada) :
    if jogada == "sair" : 
        return True
    if len(jogada) != 2 :
        print("\tO formato correto é LC!") 
        return False
    if int(jogada[0]) < 0 or int(jogada[0]) > 10 or int(jogada[1]) < 0 or int(jogada[1]) > 10: 
        print("\tAs coordenadas devem estar no intervalo de 0 a 9!")
        return False
    if tabuleiro[int(jogada[0])][int(jogada[1])] != '-':
        print("\tEssa jogada já foi feita. Tente novamente") 
        return False
    return True

def fimDeJogo(acertos):
    if (acertos == 32):
        return 1    
    return 0

def executarTiro(tabuleiro, posicao):
    if tabuleiro[posicao[0]][tabuleiro[1]] == 'O':
        tabuleiro[posicao[0]][posicao[1]] == 'X'
        return True
    else:
        tabuleiro[posicao[0]][posicao[1]] == '.'
        return False