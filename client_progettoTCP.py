import socket
import string
import facilities as fa

if __name__ == "__main__":
    HOST = 'localhost'    # Il nodo remoto, qui metti il tuo indirizzo IP per provare connessione server e client dalla tua macchina alla tua macchina
    PORT = 50010             # La stessa porta usata dal server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024)
        #print("ho ricevuto i dati:", data)
        #lista = fa.bytes_to_list(data)
        """
        if lista == type(list):
            print("ho identificato una lista")
            print('Received: ', lista)
        else:
        """
        if type(fa.bytes_to_list(data)) is list:
            #print("ho identificato una lista")
            print('Received: ', fa.bytes_to_list(data))
            continue
        else:
            #print("ho identificato una stringa")
            print('Received: ', data.decode())
            if data == "chiusura della connessione":
                break



        testo = input(">").encode()
        s.send(testo)



