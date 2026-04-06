#!/usr/bin/env python3
"""
ScanMap Tool
============
Autore: Bruno Figus
Descrizione: Scansione porte TCP tramite nmap con salvataggio report.
             Uso esclusivamente su sistemi propri o con autorizzazione esplicita.
"""

import nmap
import datetime

def scansiona(ip: str) -> dict:
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')
    return nm

def salva_report(ip: str, nm: dict) -> None:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_file = f"report_{ip}_{timestamp}.txt"
    with open(nome_file, 'w') as f:
        f.write(f"Report scansione: {ip}\n")
        f.write(f"Data: {timestamp}\n")
        f.write("─" * 40 + "\n")
        for porta in nm[ip]['tcp']:
            servizio = nm[ip]['tcp'][porta]['name']
            stato = nm[ip]['tcp'][porta]['state']
            f.write(f"Porta {porta} | {servizio} | {stato}\n")
    print(f"\n  ✔  Report salvato: {nome_file}")


def main() -> None:
    print("\n" + "=" * 40)
    print("      SCANMAP TOOL")
    print("=" * 40)
    ip = input("\n  IP da scansionare: ").strip()
    print(f"\n  Scansione in corso su {ip}...")
    nm = scansiona(ip)
    salva_report(ip, nm)

if __name__ == "__main__":
    main()    
