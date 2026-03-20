# ACNH Installer
# Creato il 14 Marzo 2026
# Creato da mitzikritzi2191

# "Path" permette l'uso della directory "home" dell'utente
from pathlib import Path
# Questo permette l'uso di funzionalità come la creazione delle directory
import os
# Questo permette il download dei file da internet
import requests
# Questo permette l'estrazione di file zip
from zipfile import ZipFile
# Questo permette lo spostamento di file
import shutil

# Setto una variabile chiamata "home" in Path.home() in modo da poter usare la directory "home" dell'utente
home = Path.home()
# Conservo la cartella "Download"
downloads_folder = f"{home}\\Downloads"
# Conservo l'url di Ryujinx come stringa per utilizzarlo dopo
ryujinx_url = "https://git.ryujinx.app/api/v4/projects/68/packages/generic/Ryubing-Canary/1.3.265/ryujinx-canary-1.3.265-win_x64.zip"
# Conservo il tipo di file da scaricare
file_type = {"downloadformat": "zip"}
# Setto il nome del file da scaricare come "Ryujinx.zip"
file_name = f"{home}\\Downloads\\Ryujinx.zip"
# Setto la destinazione finale dell'installazione di Ryujinx
extracted_ryujinx = f"{home}\\Downloads\\Ryujinx"
# Setto la destinazione della directory portatile di Ryujinx con le keys
portable_dir = f"{extracted_ryujinx}\\publish\\portable"
keys_dir = f"{portable_dir}\\system"
# Variabili di check dei file
fw_check = Path(f"{home}\\Downloads\\Firmware.21.0.0.zip")
fw_extract = Path(f"{home}\\Downloads\\Firmware.21.0.0")
keys_check = Path(f"{home}\\Downloads\\prod.keys")
# Setto dove installare il firmware 
fw_install_path = f"{portable_dir}\\bis\\system\\Contents\\registered"
fw_files = []

# Stampo del testo nel terminale
print("Ciao! Benvenuto nell'installer ufficiale di ACNH.")
print("Questo script scaricherà e installerà Ryujinx per te!")
print("Inclusi i prod.keys e title.keys!")
# Ricevo il consenso per scaricare Ryujinx
consent = input("Posso scaricare Ryujinx? (Sì/No): ")

# Questa funzione installa Ryujinx
def downloadRyujinx(consent):
    # Se il consenso non è stato dato, termino il programma
    # So che questa funzione if è lunghetta, ma fa sì che includa tutti i casi possibili per "No"
    if consent == "n" or consent == "N" or consent == "No" or consent == "no" or consent == "nO" or consent == "NO":
        print("Va bene! ^^ Allora non scaricherò Ryujinx.")
        print("Questo programma verrà terminato. Grazie per averlo provato!")
    # Se il consenso è stato dato, scarica Ryujinx
    # Anche qui, un elif lunghetto, ma fa sì che siano inclusi tutti i casi di Sì/Yes
    elif consent == "y" or consent == "Y" or consent == "yes" or consent == "Yes" or consent == "YEs" or consent == "YES" or consent == "yEs" or consent == "yES" or consent == "yeS" or consent == "YeS" or consent == "s" or consent == "S" or consent == "si" or consent == "sI" or consent == "Si" or consent == "SI" or consent == "sì" or consent == "Sì" or consent == "SÌ" or consent == "sÌ":
        # Dico all'utente che sto installando Ryujinx
        print("Ok! Download di Ryujinx in corso...")
        # Mando la richiesta di Gitlab di Ryujinx ed eseguo il download
        downloaded_file = requests.get(ryujinx_url, params=file_type)
        # Controllo se il file è corrotto
        sanity_check = downloaded_file.ok
        # Se il sanity check fallisce, dico all'utente che il download è fallito e di riavviare il programma
        if sanity_check == False:
            print("Download fallito! Sanity check error!! Per favore, riavvia il programma.")
        # Se il sanity check è passato, dico all'utente che il download è riuscito e salvo il file
        elif sanity_check == True:
            print("Download completato! Salvataggio del file in corso...")
            with open(file_name, mode="wb") as file:
                file.write(downloaded_file.content)
            print(f"Ryujinx è stato scaricato e salvato in {file_name}!Preparazione della prossima fase dell'installazione")
downloadRyujinx(consent)
# Notifico l'utente cosa accadrà nella seconda fase dell'installazione
print(f"In questa fase successiva, estraggo 'Ryujinx.zip' che si trova in {file_name}!")
print("Creerò inoltre una cartella chiamata 'portable' nella directory di Ryujinx, infine creerò una sottocartella chiamata 'system' ^-^")

# Questa funzione rende Ryujinx utilizzabile
def setupRyujinx():
    # Apro il file ed estraggo dove dovrebbe andare
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractall(path=f"{extracted_ryujinx}")
    # Notifico l'utente che Ryujinx è stato estratto e dove si trova
    print(f"Ryujinx è stato estratto con successo e si trova in {extracted_ryujinx}!")
    # Dico all'utente che sto creando una nuova directory
    print("Inserimento nella cartella 'user'...")
    # Creazione effettiva della directory
    if not os.path.exists(portable_dir):
        os.makedirs(portable_dir)
    # Dico all'utente che è avvenuto con successo
    print("Cartella 'portable' creata!")
    # Ora faccio la stessa cosa ma con le keys
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
    print("Cartella 'system' creata!")
    # ...e col firmware
    if not os.path.exists(fw_install_path):
        os.makedirs(fw_install_path)
    print("Percorso di installazione del Firmware creato!")
setupRyujinx()
# Informo l'utente che Ryujinx è stato installato in maniera portatile, poi avverto che sto cercando nella cartella Download
print(f"Ryujinx è stato installato ed è portatile! Controllo nella cartella di Download alla ricerca del file 'prod.keys'...")

# Installo le keys
def installKeys():
    # Avverto l'utente
    print("Installazione delle keys! Attendi...")
    try:
        # Tentativo di spostamento delle keys nella directory corrispondente
        shutil.copy(keys_check, f"{keys_dir}\\prod.keys")
        # Caso di installazione avvenuta
        print("Keys installate!")
    # Se il file non è stato trovato, dico all'utente come risolvere, poi continuo
    except FileNotFoundError:
        print("Keys non trovate! Per favore inseriscile nella cartella di Download e assicurati che il file si chiami 'prod.keys'!")
installKeys()

def instalFw():
    # Rimuovo il firmware attualmente installato
    shutil.rmtree(fw_install_path)
    # Creo una struttura di cartelle per il firmware
    os.mkdir(fw_install_path)
    # Avverto l'utente dell'installazione
    print("Installazione del Firmware! Potrebbe volerci un po', attendi...")
    # Estraggo il firmware
    try:
        with ZipFile(fw_check, 'r') as zObject:
            zObject.extractall(path=f"{fw_extract}")
        # Aggiungo il filename nella lista fw_files
        for filename in os.listdir(fw_extract):
            if os.path.isfile(os.path.join(fw_extract, filename)):
                fw_files.append(filename)
        # Faccio un loop nel nome del file e creo le directory appropriate, dopo le sposto
        for i in fw_files:
            os.makedirs(f"{fw_install_path}\\{i}")
            shutil.move(f"{fw_extract}\\{i}", f"{fw_install_path}\\{i}\\00")
    except FileNotFoundError:
        print("Firmware non trovato! Per favore, assicurati che sia nella cartella di Download e che si chiami 'Firmware.21.0.0.zip'!")
instalFw()
# Dico all'utente che Ryujinx è stato installato e di premere Invio per uscire
# E fare una bella pubblicità eheh :Bellapsycho:
print("Tutto pronto! Se ancora non ci sei, unisciti al nostro server discord per treasure islands divertenti ed hangouts!")
print("https://discord.gg/actreasurehub")
end = input("Ryujinx è stato installato! Premi Invio per terminare il programma!")
