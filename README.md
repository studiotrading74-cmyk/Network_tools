# Network_tools
Script Python per networking e sicurezza di rete — port scanner e tools di analisi

# 🌐 network-tools

Script Python per networking e sicurezza di rete.  
Progetto sviluppato durante il percorso di studio in **cybersecurity e penetration testing**.

---

## 🛠️ Strumenti inclusi

### `port_scanner.py` — Port Scanner TCP
Scansiona le porte TCP da 1 a 1024 su un host specificato e restituisce le porte aperte.  
Sviluppato da zero usando i **socket Python** — stessa logica di base di nmap, senza dipendenze esterne.

---

## 🚀 Utilizzo

```bash
python3 port_scanner.py
```

Inserisci l'IP quando richiesto. Esempio su localhost:

```
Inserisci l'IP da scannerizzare: 127.0.0.1
631
```

---

### `scanmap_tool.py` — ScanMap Tool
Scansiona le porte TCP da 1 a 1024 su un host specificato tramite **nmap**,
rileva il nome del servizio per ogni porta aperta e salva i risultati in un report `.txt` con timestamp.

**Requisiti:**
- nmap installato sul sistema (`sudo apt install nmap`)
- libreria python-nmap (`pip install python-nmap`)

**Esempio output report:**
```
Report scansione: 127.0.0.1
Data: 20260406_190031
────────────────────────────────────────
Porta 631 | ipp | open
```

## ⚠️ Avvertenza legale

Questo tool è sviluppato a **scopo didattico**.  
Scansionare porte su sistemi altrui senza autorizzazione esplicita è **illegale**.  
Usalo esclusivamente su sistemi di tua proprietà o su reti per cui hai il permesso scritto.

---

## 🎯 Obiettivo del progetto

Comprendere il funzionamento dei socket TCP e la logica alla base degli strumenti di network scanning,  
attraverso un'implementazione minimale in Python puro.

Gli script sono stati sviluppati in collaborazione con AI (Claude di Anthropic),
con focus sulla comprensione del codice e dei concetti sottostanti,
più che sulla scrittura autonoma da zero.

---

## 👤 Autore

**Bruno Figus**  
[LinkedIn](https://www.linkedin.com/in/bruno-figus-b77495177/) · Siliqua (CA), Sardegna
