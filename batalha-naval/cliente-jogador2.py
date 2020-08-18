import socket
import time
from regrasDoJogo import *

Host = '127.0.0.1'
Port = 12345

em_jogo = True
tabuleiroproprio = []
tabuleirooponente = []
antingidos = 0
jogador = '2'

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.connect((Host, Port))

tabuleiroproprio = criaTabuleiro()
tabuleirooponente = criaTabuleiro()
imprimeRegras(jogador)
colocarNavios(tabuleiroproprio)
imprimirTabuleiros(tabuleiroproprio, tabuleirooponente)

print ('Preparar, apontar....')
while em_jogo:
	quemJoga = socket_tcp.recv(1024)
	quemJoga = quemJoga.decode()
#------------------------------------------------------------------------------------------------------------------------#
	while(quemJoga == '2'):
		jogada = input("Jogada: ")

		while validaJogada(tabuleirooponente,jogada) == False : 
			jogada = input("Digite uma jogada válida =>  ")

		socket_tcp.send(jogada.encode())

		if jogada == "sair" or jogada == "SAIR":
			print ("Fim de jogo")
			em_jogo = False
		else:
			msg = socket_tcp.recv(1024)
			jogada = msg.decode()
			if(msg == 'X'): 
				tabuleirooponente[jogada[0]][jogada[1]] = msg
				antingidos = antingidos + 1
			else:
				tabuleirooponente[jogada[0]][jogada[1]] = msg
				quemJoga == '1'

		fim = fimDeJogo(antingidos)
		if fim > 0:
			print("\nVocê Ganhou! Parabéns! :D")
			print ("\nJogo Terminado!")
			em_jogo = False
#---------------------------------------------------------------------------------------------------------------------#
	while(quemJoga == '1'):	
		#recebe
		if em_jogo:
			print("\nAguarde a jogada do servidor...")
			msg = socket_tcp.recv(1024)
			jogada = msg.decode()

			if not msg or jogada == "sair":
				print ('\nServidor ', Host, ' desconectou-se.\n')
				em_jogo = False
			else:
				sucesso = executarTiro(tabuleiroproprio, jogada)
				if(sucesso):
					mensagem = 'X'
					socket_tcp.send(mensagem.encode()) 
				else:
					mensagem = '.'
					socket_tcp.send(mensagem.encode()) 
		
				fim = fimDeJogo(antingidos)
				if fim > 0:
					if fim == 1: 
						print("\nVocê Perdeu! :(")				
					print ("\nJogo Terminado!")
					em_jogo = False

print("Fechando conexao")
socket_tcp.close()
