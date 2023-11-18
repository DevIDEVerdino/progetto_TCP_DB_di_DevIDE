#from ast import Return
import facilities as fa
import threading 
import socket
import mysql.connector
import time

lock = threading.Lock()

conn_sql = mysql.connector.connect(
        host="127.0.0.1",  # 127.0.0.1 per test a casa 127.0.0.1/phpmyadmin altrimenti 10.10.0.10
        user="davide_verdino",
        password="verdino1234",
        database="5ATepsit",
        port=3306, # la porta di default è la 3306 ma comunque potete impostarne un'altra
    )

PASSWORD = "CIAO"

def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    i=0
    while data != PASSWORD and i<2:
        i+=1
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {2-i} ".encode())
        data = conn.recv(1024).decode()      

    if(data != PASSWORD):
        conn.send(f"Password ERRATA troppe volte, arrivederci".encode())
        conn.close()
        return

    

    while True:
        conn.send("Benvenuto, cosa vuoi fare: I=insert, U=update, R=read, D=delete, E=exit".encode())
        data = conn.recv(1024).decode()
        print(data)

        if data == "R":
            conn.send("su che tabella vuoi cercare: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()            
            dati_query = db_get(data)
            print(dati_query)
            conn.send(fa.list_to_bytes(dati_query))
        
        elif data == "I":
            conn.send("su quale tabella vuoi inserire: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()
            db_set(data, conn)
            conn.send("modifica effettuata con successo!! (premere ENTER)".encode())

        
        elif data == "U":
            conn.send("quale tabella vuoi modificare: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()
            db_update(data, conn)
            conn.send("modifica effettuata con successo!! (premere ENTER)".encode())
        
        elif data == "D":
            conn.send("in quale tabella vuoi eliminare: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()
            db_del(data, conn)
            conn.send("modifica effettuata con successo!! (premere ENTER)".encode())

        elif data == "E":
            conn.send("chiusura della connessione".encode())
            break


    return


def db_get(d):

    """
    funzione con cui ricevo i dati dalle tabelle
    """

    cur = conn_sql.cursor()

    if d == "D":
        query = "SELECT * FROM dipendenti_davide_verdino"
    
    elif d == "Z":
        query = "SELECT * FROM zone_di_lavoro_davide_verdino"

    cur.execute(query)
    dati = cur.fetchall()
    return dati


def db_set(d, conn):

    cur = conn_sql.cursor()


    if d == "D":
        #inserimento dei campi della tabella dipendenti
        conn.send("inserisci nome dipendente: ".encode())
        nome = conn.recv(1024).decode()
        conn.send("inserisci cognome: ".encode())
        cognome = conn.recv(1024).decode()
        conn.send("inserisci la posizione lavorativa del dipendente: ".encode())
        pos_lav = conn.recv(1024).decode()
        conn.send("inserisci la data di assunzione(formato ('YYYY-MM-DD')): ".encode())
        data_as = conn.recv(1024).decode()
        conn.send("inserire il numero di telefono: ".encode())
        tel = conn.recv(1024).decode()
        conn.send("inserire l'indirizzo di casa del dipendente: ".encode())
        ind = conn.recv(1024).decode()
        query = "INSERT INTO `dipendenti_davide_verdino` (`nome`, `cognome`, `posizione lavorativa`, `data di assunzione`, `telefono`, `indirizzo`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(nome, cognome, pos_lav, data_as, tel, ind)

    elif d == "Z":
        conn.send("inserisci il nome della zona di lavoro: ".encode())
        nome_zona = conn.recv(1024).decode()
        conn.send("inserisci il numero di dipendenti: ".encode())
        numero_clienti = conn.recv(1024).decode()
        conn.send("inserisci l'id della zona: ".encode())
        id_dipendente = conn.recv(1024).decode()
        conn.send("inserici l'orario di lavoro (esempio: 8:00-14:00 15:00-17:00): ".encode())
        orario_lavoro = conn.recv(1024).decode()
        query = "INSERT INTO `zone_di_lavoro_davide_verdino` (`nome_zona`, `numero_clienti`, `id_dipendente`, `orario_lavoro`) VALUES ('{}','{}','{}','{}')".format(nome_zona, numero_clienti, id_dipendente, orario_lavoro)

    time.sleep(0.025)
    lock.acquire()
    time.sleep(0.025)
    cur.execute(query)
    try:
        conn_sql.commit()
    except:
        conn_sql.rollback()
    lock.release()

    return


def db_update(d, conn):

    cur = conn_sql.cursor()



    if d == "D":
        conn.send("inserisci l'id del dipendente di cui vuoi modificare gli attributi: ".encode())
        id = conn.recv(1024).decode()
        conn.send("Inserisci il nome del attributo in questione che vuoi modificare: ".encode())
        attr = conn.recv(1024).decode()
        conn.send("Inserisci il nuovo valore del attributo: ".encode())
        val = conn.recv(1024).decode()
        query = "UPDATE dipendenti_davide_verdino SET {} = '{}' WHERE id = '{}'".format(attr, val, id)



    elif d == "Z":
        conn.send("Inserisci l'id della zona di cui vuoi modificare gli attributi: ".encode())
        id = conn.recv(1024).decode()
        conn.send("Inserisci il nome del attributo in questione che vuoi modificare: ".encode())
        attr = conn.recv(1024).decode()
        conn.send("Inserisci il nuovo valore del attributo: ".encode())
        val = conn.recv(1024).decode()
        query = "UPDATE zone_di_lavoro_davide_verdino SET {} = '{}' WHERE id_zona = '{}'".format(attr, val, id)

    time.sleep(0.025)
    lock.acquire()
    time.sleep(0.025)
    cur.execute(query)
    try:
        conn_sql.commit()
    except:
        conn_sql.rollback()
    lock.release()
    return



def db_del(d, conn):

    cur = conn_sql.cursor()
    
    
    
    if d == "D":
        conn.send("inserisci l'id del dipendete che vuoi togliere dalla tabella: ".encode())
        id = conn.recv(1024).decode()
        query = "DELETE FROM dipendenti_davide_verdino WHERE id = '{}'".format(id)

    elif d == "Z":
        conn.send("inserisci l'id della zona che vuoi togliere dalla tabella: ".encode())
        id = conn.recv(1024).decode()
        query = "DELETE FROM zone_di_lavoro_davide_verdino WHERE id_zona = '{}'".format(id)

    
    time.sleep(0.025)
    lock.acquire()
    time.sleep(0.025)
    cur.execute(query)
    try:
        conn_sql.commit()
    except:
        conn_sql.rollback()
    lock.release()
    return


if __name__ == "__main__":
    print("server in ascolto: ")
    lock = threading.Lock()
    HOST = '127.0.0.1'
    PORT = 50013            # Porta dinamica a piacere
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    thread = []
    lista_connessioni = []
    i=0

    while True:
        lista_connessioni.append( s.accept() ) #connessione = s.accept()
        print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
        thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) ))
        thread[i].start()
        i+=1
