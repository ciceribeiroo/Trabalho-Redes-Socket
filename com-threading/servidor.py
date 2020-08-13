import socket 
from _thread import start_new_thread
import threading 

#trava a thread 
print_lock = threading.Lock() 
  
def threaded(c): 
    while True: 
  
        # recebe dados do cliente
        data = c.recv(1024) 
        # para encerrar
        if not data: 
            print('Até mais ;)') 
              
            # libera a thread 
            print_lock.release() 
            break
  
        # manda de volta 
        c.send(data) 
  
    # fecha a conexao 
    c.close() 
  
  
def Main():
    # localhost 
    host = "" 
    # define o servidor
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Socket ", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("Esperando uma conexão...") 
  
    # enquanto o cliente não escolhe sair 
    while True: 
  
        # conecta com o cliente
        c, addr = s.accept() 
  
        # trava o socket
        print_lock.acquire() 
        print('Conectado em :', addr[0], ':', addr[1]) 
  
        # começa uma nova thread
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 