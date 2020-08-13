import socket
#definindo o servidor como localhost
def server(host = 'localhost', port=7183):
    data_payload = 2048 #max de bits de uma mensagem
    # Criando o socket TCP
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Permitindo que a porta seja reutilizada
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Ligando a porta e o servidor
    server_address = (host, port)
    print ("Iniciando o servidor %s na porta %s" % server_address)
    sock.bind(server_address)
    # Numero maximo de conexoes igual a 5
    sock.listen(5) 
    i = 0
    while True: 
        print ("Esperando...")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ("Mensagem: %s" %data)
            client.send(data)
            print ("Mandando %s bytes de volta para %s" % (data, address))
            # fim da conexão
            client.close()
            i+=1
            #depois de 3 mensagens fecha automaticamente
            if i>=3: break           
server()