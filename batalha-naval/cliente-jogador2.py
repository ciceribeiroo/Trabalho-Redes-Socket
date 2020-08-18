#---------------------------------------------------------#
# Implementacao de cliente para Jogo da Velha.            #
#---------------------------------------------------------#
import socket
import time
from JogoDaVelha import *

## Informacoes do servidor ao qual se conectar
Host = '127.0.0.1'
Port = 12345

em_jogo = True
tabuleiro2 = []
## Por enquanto o cliente é sempre o X
jogador = '2'

## Criacao do socket para comunicacao
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.connect((Host, Port))

#### Tudo certo para iniciar o jogo ####
tabuleiroproprio = criaTabuleiro()
tabuleirooponente = criaTabuleiro()
imprimeRegras(jogador)
imprimeSeuTabuleiro(tabuleiroproprio)
imprimeTabuleiroOponente()

## laco para enviar e receber jogadas
while em_jogo:
	## lendo mensagem
	jogada = input("Jogada: ")

	# verificar se a jogada eh valida. Se nao for, continua pedindo outra jogada
	while validaJogada(tabuleiroproprio,jogada) == False : 
		jogada = input("Digite uma jogada válida =>  ")

	## jogada validada. Enviar ao servidor
	socket_tcp.send(jogada.encode())

	##verifica se jogador quer sair
	if jogada == "sair" or jogada == "SAIR":
		print ("Fim de jogo")
		em_jogo = False
	else:
		# se a jogada eh valida e não eh um comando de saída, 
		# então o cliente deve aplicar a jogada no seu tabuleiro
		tabuleiroproprio[int(jogada[0])][int(jogada[1])] = "X"
		imprimeSeuTabuleiro(tabuleiroproprio)

		# verificar se com essa jogada o jogo terminou ou continua
		fim = fimDeJogo(tabuleiroproprio)
		if fim > 0:
			if fim == 1: 
				print("\nVocê Ganhou! Parabéns! :D")
			elif fim == 2:
				print("\nJogo Empatado!")
			print ("\nJogo Terminado!")
			em_jogo = False
		
		## se jogo continua
		if em_jogo:
			#aguardando a jogada do servidor
			print("\nAguarde a jogada do servidor...")
			# o cliente recebe a mensagem do servidor e a decodifica 
			msg = socket_tcp.recv(1024)
			jogada = msg.decode()

			#Verifica jogada
			if not msg or jogada == "sair":
				print ('\nServidor ', Host, ' desconectou-se.\n')
				em_jogo = False
			else:
				# se a jogada eh valida e não eh um comando de saída, 
				# então o cliente deve aplicar a jogada no seu tabuleiro
				tabuleiroproprio[int(jogada[0])][int(jogada[1])] = "O"
				imprimeSeuTabuleiro(tabuleiroproprio)
		
				# verificar se essa jogada encerra o jogo
				fim = fimDeJogo(tabuleiroproprio)
				if fim > 0:
					if fim == 1: 
						print("\nVocê Perdeu! :(")
					elif fim == 2:
						print("\nJogo Empatado!")
					
					print ("\nJogo Terminado!")
					em_jogo = False
## Fechar conexao
print("Fechando conexao")
socket_tcp.close()