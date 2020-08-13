import socket 

def Main(): 
	# localhost
	host = '127.0.0.1'

	# Define the port on which you want to connect 
	port = 12345
    #cria o socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	# conecta o servidor no localhost
	s.connect((host,port)) 
	# insere uma mensagem pra mandar pro servidor 
	message = input('Insira sua mensagem: ')
	while True: 

		# envia uma mensagem 
		s.send(message.encode('utf-8')) 

		# mensagem recebida do servidor
		data = s.recv(1024) 
		print('Recebido :',str(data.decode('utf-8'))) 

		# o cliente quer continuar 
		ans = input('\nQuer enviar uma nova mensagem(s/n) :') 
		if ans == 's': 
			continue
		else: 
			break
	# encerra a conexao 
	s.close() 

if __name__ == '__main__': 
	Main() 
