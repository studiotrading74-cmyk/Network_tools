import socket

#!/usr/bin/env python3
"""
Port Scanner
============
Autore: Bruno Figus
Descrizione: Scansione delle porte TCP (1-1024) su un host tramite socket Python.
             Uso esclusivamente su sistemi propri o con autorizzazione esplicita.
"""


a = input("inserisci l'IP da scannerizzare: ")
x = range (1, 1024)
for y in x:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    risultato = s.connect_ex((a, y))
    s.close()
    if risultato ==0:
        print(y)
    
