# ACNH Installer
# Created March 14th, 2026
# Created by mitzikritzi2191

# Path allows us to use the user's home directory
from pathlib import Path
# This allows us to use functionalities such as making directories
import os
# This allows us to download files from the internet
import requests
# This allows us to extract files
from zipfile import ZipFile
# This allows us to move files
import shutil

# Set a variable called "home" to Path.home() so we can use the user's home directory
home = Path.home()
# Store the user's download folder
downloads_folder = f"{home}\\Downloads"
# Store Ryujinx's url as a string for use later
ryujinx_url = "https://git.ryujinx.app/api/v4/projects/68/packages/generic/Ryubing-Canary/1.3.265/ryujinx-canary-1.3.265-win_x64.zip"
# Store the type of download
file_type = {"downloadformat": "zip"}
# Set the file name of the Ryujinx zip
file_name = f"{home}\\Downloads\\Ryujinx.zip"
# Set the destination of where Ryujinx is installed
extracted_ryujinx = f"{home}\\Downloads\\Ryujinx"
# Set the destination of the Ryujinx portable directory and keys
portable_dir = f"{extracted_ryujinx}\\publish\\portable"
keys_dir = f"{portable_dir}\\system"
# File checking variables
fw_check = Path(f"{home}\\Downloads\\Firmware.21.0.0.zip")
fw_extract = Path(f"{home}\\Downloads\\Firmware.21.0.0")
keys_check = Path(f"{home}\\Downloads\\prod.keys")
# Set where the firmware is to be installed
fw_install_path = f"{portable_dir}\\bis\\system\\Contents\\registered"
fw_files = []

# Print text to the console
print("Hello! Welcome to the official installer for ACNH.")
print("This script will download Ryujinx for you and install")
print("the Prod.keys file and Title.keys file for you!")
# Get consent to download Ryujinx
consent = input("May I download Ryujinx? (Yes/No): ")

# This function downloads Ryujinx
def downloadRyujinx(consent):
    # If consent is not given, Terminate the program
    # I know the if statement is a bit lengthy but this ensures every possible combination of the word "No"
    if consent == "n" or consent == "N" or consent == "No" or consent == "no" or consent == "nO" or consent == "NO":
        print("That's okay ^^ I will not download Ryujinx.")
        print("This program will be terminated. Thank you for using it!")
    # If consent is given, Download Ryujinx
    # Again, another lengthy elif statement but this ensures every spelling of yes in both english and spanish
    elif consent == "y" or consent == "Y" or consent == "yes" or consent == "Yes" or consent == "YEs" or consent == "YES" or consent == "yEs" or consent == "yES" or consent == "yeS" or consent == "YeS" or consent == "s" or consent == "S" or consent == "si" or consent == "sI" or consent == "Si" or consent == "SI" or consent == "sí" or consent == "Sí" or consent == "SÍ" or consent == "sÍ":
        # Tell the user we're downloading Ryujinx
        print("Okay! Downloading Ryujinx now...")
        # Send a request to Ryujinx's gitlab and download
        downloaded_file = requests.get(ryujinx_url, params=file_type)
        # Check if the file is corrupted
        sanity_check = downloaded_file.ok
        # If the sanity check fails, tell the user that the download failed and to run the program again
        if sanity_check == False:
            print("Download Failed! Please restart the program.")
        # If the sanity check passes, Tell the user that the download succeeded and save the file
        elif sanity_check == True:
            print("Download Succeeded! Now saving...")
            with open(file_name, mode="wb") as file:
                file.write(downloaded_file.content)
            print(f"Ryujinx has been downloaded and saved to {file_name}! Now preparing for the next steps in installation!")
downloadRyujinx(consent)
# Notify to the user what is going to happen in phase 2 of install
print(f"In phase two of installation, I will be extracting 'Ryujinx.zip' that is located in {file_name}!")
print("I will also be creating a folder called 'portable' in the Ryujinx directory, and I will be creating a subdirectory called 'system' ^-^")

# This function sets up Ryujinx
def setupRyujinx():
    # Open the file and extract to where we want it to go
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractall(path=f"{extracted_ryujinx}")
    # Notify the user that Ryujinx has been extracted and where it is available
    print(f"Ryujinx has been extracted and is available in {extracted_ryujinx}!")
    # Tell the user we're making a new directory
    print("Now creating directory 'user'!")
    # Actually create the directory
    if not os.path.exists(portable_dir):
        os.makedirs(portable_dir)
    # Tell the user we made it
    print("'portable' directory created!")
    # Now do the same thing except this time for keys
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
    print("'system' directory created!")
    # ...and firmware
    if not os.path.exists(fw_install_path):
        os.makedirs(fw_install_path)
    print("Firmware install path created!")
setupRyujinx()
# Inform the user Ryujinx is installed and its a portable install, Then tell them we're searching the downloads folder
print(f"Ryujinx has now been installed and is a portable installation! I will be searching your downloads folder for Prod.keys now!")

# Install the keys
def installKeys():
    # Tell the user we're installing keys
    print("Installing keys! Please wait a moment...")
    try:
        # Attempt to move the keys into our keys directory
        shutil.copy(keys_check, f"{keys_dir}\\prod.keys")
        # Notify of a successful install
        print("Keys installed!")
    # If the file isnt found, tell the user how to fix it, then continue
    except FileNotFoundError:
        print("Keys file not found! Please put them in the Downloads folder on your computer and ensure its named 'prod.keys'!")
installKeys()

def instalFw():
    # Remove the firmware that's currently installed
    shutil.rmtree(fw_install_path)
    # Create the folder structure for fw
    os.mkdir(fw_install_path)
    # Notify the user that we are installing firmware
    print("Installing Firmware! This could take a moment, please wait...")
    # Extract the firmware
    try:
        with ZipFile(fw_check, 'r') as zObject:
            zObject.extractall(path=f"{fw_extract}")
        # Add the filename to the fw_files list
        for filename in os.listdir(fw_extract):
            if os.path.isfile(os.path.join(fw_extract, filename)):
                fw_files.append(filename)
        # Loop through the file name and create the appropriate directories then move the files
        for i in fw_files:
            os.makedirs(f"{fw_install_path}\\{i}")
            shutil.move(f"{fw_extract}\\{i}", f"{fw_install_path}\\{i}\\00")
    except FileNotFoundError:
        print("Firmware not found! Please make sure it is in your downloads folder and is called 'Firmware.21.0.0.zip'!")
instalFw()
# Tell the user that Ryujinx has been installed and to press enter to exit
# and do a lil advertising :Bellapsycho:
print("That's all! If you aren't already, join our discord server for fun treasure islands and hangouts!")
print("https://discord.gg/actreasurehub")
end = input("Ryujinx has been installed! Press enter to exit!")
