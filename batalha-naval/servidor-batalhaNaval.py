#---------------------------------------------------------#
# Implementacao do Jogo da Velha com sockets em Python.   #
#---------------------------------------------------------#
import socket
from JogoDaVelha import *

## Informações do servidor: Host e porta para conexao
Host = ''
Port = 12345

# quem vai comecar o jogo
em_jogo = quemComeca()
tabuleiro1 = []
## o servidor é sempre o jogador1
##id=1
jogador = '1'
##---------------------------------------------------##
## Programa principal                                ##
##---------------------------------------------------##

## Criacao do socket TCP e inicio de escuta
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((Host, Port))
socket_tcp.listen(5)

print ('Preparar, apontar....')
# Laco para receber conexoes
while True:
	print("Aguardando conexão do jogador")
	conn, client_host = socket_tcp.accept()
	print ('Jogador ', client_host, ' conectou.')
	
	## Comecando o jogo
	em_jogo = True
	tabuleiroproprio = criaTabuleiro()
	tabuleirooponente = criaTabuleiro()
	imprimeRegras(jogador)
	imprimeSeuTabuleiro(tabuleiroproprio)
	imprimeTabuleiroOponente()

	##laco para receber e enviar jogadas
	while em_jogo:
		## Aguardando jogada do cliente
		print("Aguarde a jogada do", client_host, "...")   
		msg = conn.recv(1024) 
		jogada = msg.decode()
		
		##verifica se jogador quer sair
		if not msg or jogada == "sair" or jogada == "SAIR":
			print ("Jogador desconectou")
			em_jogo = False
		else:
			# se a resposta não está quebrada e não é um comando de saída, 
			# então o servidor deve aplicar a resposta no seu tabuleiro
			tabuleiroproprio[int(jogada[0])][int(jogada[1])] = "X"
			imprimeSeuTabuleiro(tabuleiroproprio)

			# verificar se com essa jogada o jogo terminou ou continua
			# fimDeJogo: parâmetro seu tabuleiro, o retorno da função será 0,1 ou 2
			# se for 1 então a resposta do cliente gerou uma vitória e o servidor perdeu,
			# se for 2 então a resposta do cliente gerou um empate,
			# se for 0 o jogo pode continuar
			fim = fimDeJogo(tabuleiroproprio)
			if fim > 0:
				if fim == 1: 
					print("\nVocê Perdeu! :(")
				elif fim == 2:
					print("\nJogo Empatado!")
				print ("\nJogo Terminado!")
				em_jogo = False

			if em_jogo:
				# lendo a jogada(entrada) do servidor para enviar ao cliente
				jogada = input("\n\tJogada =>  ")

				# a entrada deve ser verificada para garantir que é valida
				# se a entrada não for válida o programa continuará esperando por uma entrada válida
				while validaJogada(tabuleiroproprio, jogada) == False: 
					jogada = input("Digite uma jogada válida: ")

				# com uma entrada válida, o servidor envia uma resposta ao cliente
				conn.send(jogada.encode())
		
				# o servidor deve verificar se sua jogada foi um comando de saída,
				# se for um comando de saída então deve-se encerrar a partida
				if jogada == "sair" or jogada == "SAIR":
					print ('Aplicação foi finalizada\n')
					em_jogo = False
				else:
					## Jogada valida e nao eh uma saida do jogo. Inserir no tabuleiro
					tabuleiroproprio[int(jogada[0])][int(jogada[1])] = "O"
					imprimeSeuTabuleiro(tabuleiroproprio)

					# verificar se essa jogada encerra o jogo
					fim = fimDeJogo(tabuleiroproprio)
					if fim > 0:
						if fim == 1:
							## Jogo terminou. Entao a ultima jogada ganhou 
							print("\nVocê Ganhou! Parabéns! :D")
						elif fim == 2:
							print("\nJogo Empatado!")
						
						print ("\nJogo Terminado!")
						em_jogo = False
## Ao encerrar o programa, fechar porta para conexoes
conn.close()