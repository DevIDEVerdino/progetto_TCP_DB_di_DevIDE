import socket
import string
import facilities as fa

if __name__ == "__main__":
    HOST = 'localhost'    # Il nodo remoto, qui metti il tuo indirizzo IP per provare connessione server e client dalla tua macchina alla tua macchina
    PORT = 50013             # La stessa porta usata dal server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        data = s.recv(1024)

        if type(fa.bytes_to_list(data)) is list:
            data = fa.bytes_to_list(data)
            #print('Received: ', data)
            for i in range (0, len(data)):
                print("#################################")
                for k in range(0, len(data[i])):
                    print(data[i][k])
            continue
        else:
            print('Received: ', data.decode())
            if "chiusura della connessione" in data.decode():
                break


        testo = input(">").encode()
        s.send(testo)



