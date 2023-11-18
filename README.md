# Progetto_TCP_DB

E' un progetto il cui scopo e' la gestione da riga di comando di dati contenuti in un DB
mysql. La connessione viene gestita tramite socket

## Installazione

il primo passo è clonare la repository:

```bash
git clone https://github.com/DevIDEVerdino/progetto_TCP_DB_di_DevIDE.git
```


Installare i requisiti tramite il comando [pip](https://pip.pypa.io/en/stable/) dopo aver clonato la repository:

```bash
pip install -r /path/to/requirements.txt
```

ATTENZIONE un passaggio importante è anche quello di installare XAMPP o comunque fare il setup di un server mysql importando le tabelle contenute nel clone della repository

## Usage

Una volta installati i requisiti si puo' procedere all'utilizzo dei programmi client e server. In ordine avviate prima il server e poi il client con i comandi seguenti:

-per il server
```bash
python3 server_progettoTCP
```

-per il client
```bash
python3 client_progettoTCP
```

Da questo momento possiamo interagire da CLI tramite il programma client con il server. La password predefinita è CIAO ma voi la potete cambiare come volete.
