import socket
ip     = "127.0.0.1"
porta   = 4444
kb  = 1024 #1kb


Messaggiosrv       = "Benvenuto nel server udp"
bytesToSend         = str.encode(Messaggiosrv)  #Codifica UTF-8

su = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #stabilisco che voglio IPV4 e UDP

su.bind((ip, porta)) # Lego ip e porta
print("Il server udp è avviato e pronto a ricevere le connessioni")

while(1):
   
    bytesAddressPair = su.recvfrom(kb)
    messaggio = bytesAddressPair[0] #Array con i dati
    ip_remoto = bytesAddressPair[1]

    msgclient = "Messaggio dal client:{}".format(messaggio)
    ip_client_remoto  = "Ip client remoto:{}".format(ip_remoto)
    
    ipremotopulito = ip_remoto[0]

    print(msgclient)
    print(ipremotopulito)
   

  