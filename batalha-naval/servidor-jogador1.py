import socket
from regrasDoJogo import *

Host = ''
Port = 12345

em_jogo = True
tabuleiroproprio = []
tabuleirooponente = []
atingidos = 0
jogador = '1'

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((Host, Port))
socket_tcp.listen(5)

print ('Preparar, apontar....')
while True:
	print("Aguardando conexão do jogador")
	conn, client_host = socket_tcp.accept()
	print ('Jogador ', client_host, ' conectou.')

	tabuleiroproprio = criaTabuleiro()
	tabuleirooponente = criaTabuleiro()
	imprimeRegras(jogador)
	colocarNavios(tabuleiroproprio)
	imprimirTabuleiros(tabuleiroproprio, tabuleirooponente)

	while em_jogo:
		quemJoga = quemComeca()
		socket_tcp.send(quemJoga.encode())
#---------------------------------------------------------------------------------------------------------------------#
		while(quemJoga == '2'):
			print("Aguarde a jogada do", client_host, "...")
			#quando eu recebo   
			msg = conn.recv(1024) 
			jogada = msg.decode()
			
			if not msg or jogada == "sair" or jogada == "SAIR":
				print ("Jogador desconectou")
				em_jogo = False
			else:
				sucesso = executarTiro(tabuleiroproprio, jogada)
				if(sucesso):
					mensagem = 'X'
					socket_tcp.send(mensagem.encode()) 
				else:
					mensagem = '.'
					socket_tcp.send(mensagem.encode()) 
	
				fim = fimDeJogo(atingidos)
				if fim > 0:
					print("\nVocê Perdeu! :(")
					print ("\nJogo Terminado!")
					em_jogo = False
#----------------------------------------------------------------------------------------------------------------------#
		while(quemJoga == '1'):
				jogada = input("\n\tJogada =>  ")

				while validaJogada(tabuleiroproprio, jogada) == False: 
					jogada = input("Digite uma jogada válida: ")

				conn.send(jogada.encode())
		
				if jogada == "sair" or jogada == "SAIR":
					print ('Aplicação foi finalizada\n')
					em_jogo = False
				else:
					msg = socket_tcp.recv(1024)
					jogada = msg.decode()
					if(msg == 'X'): 
						tabuleirooponente[jogada[0]][jogada[1]] = msg
						antingidos = antingidos + 1
					else:
						tabuleirooponente[jogada[0]][jogada[1]] = msg
						quemJoga == '2'

					fim = fimDeJogo(atingidos)
					if fim > 0:
						print("\nVocê Ganhou! Parabéns! :D")						
						print ("\nJogo Terminado!")
						em_jogo = False

conn.close()

