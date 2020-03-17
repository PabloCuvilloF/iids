#! /usr/bin/env python3

from scapy.all import*

import os
import datetime
import signal

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {})".format(signal))
    exit(0)


def id_time():

    dateTime = datetime.datetime.now()
    dateTime_str = str(dateTime)
    todayDate = dateTime_str.split(" ")[0]
    hourNow = dateTime_str.split(" ")[1].split(":")[0]
    minuteNow = dateTime_str.split(" ")[1].split(":")[1]

    id_time = todayDate + '_' + hourNow + minuteNow

    return id_time #string


def tmpDirPath():
    dir_path = "./"+id_time().split("_")[0]+"_"+id_time().split("_")[1][:4]        # Crea carpeta nueva cada 5 minutos
    if int(dir_path[-1]) < 5:
        dir_path = dir_path[:-1] + '0'
    else:
        dir_path = dir_path[:-1] + '5'

    return dir_path


def main():
    i = 0
    while i < 60:
        net_capture = sniff(count=1000)
        #net_capture.nsummary()  #Si queremos que muestre modo verboso los paquetes

        dir_path = tmpDirPath()
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            i = 0
        file_path = './' + dir_path + '/output' + str(i) + '_' + id_time() + '.pcap'
        wrpcap(file_path, net_capture)
        i += 1

    return


if __name__ == "__main__":

    signal.signal(signal.SIGINT, keyboardInterruptHandler) # Activa un handler que se activa con un ctrl+C
    main()

#El autor es Alberto Rafael Rodríguez Iglesias
#fc2029102a9bfad976b59f0ee443b1eb030557033b6710554f458972dd8d132d 
