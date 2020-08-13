import socket
#criando o cliente com endereço e porta
def client(host = 'localhost', port=7183): 
    # Criando o socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Conectando no cliente 
    server_address = (host, port) 
    print ("Conectando em %s porta %s" % server_address) 
    sock.connect(server_address) 
    try: 
        # Enviando mensagem
        message = "Trabalho Redes Socket" 
        print ("Enviando %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Esperando pela mensagem
        amount_received = 0 
        amount_expected = len(message) 
        #recebe a mensagem de 16 em 16 bits
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Foi recebido: %s" % data) 
    #tratar erros
    except socket.error as e: 
        print ("Erro no socket: %s" %str(e)) 
    except Exception as e: 
        print ("Outros erros: %s" %str(e)) 
    #fechar a conexção
    finally: 
        print ("Até logo") 
        sock.close() 

client()