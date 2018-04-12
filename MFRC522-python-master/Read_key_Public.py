#Read key
#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

GPIO.setwarnings(False)
cmpt=0

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Lecture terminée")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#print ("Press Ctrl-C to stop.")
secteurBloc=eval(input("Entrez un Secteur :\n"))

print ("Passer le tag RFID a lire")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    #print ("Passer le tag RFID a lire")
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Carte detectee")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print ("UID de la carte : "+str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])+"."+str(uid[4]))
    
        # Clee d authentification par defaut
        keyA_Public = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        #key = [0x00,0x00,0x00,0x00,0x00,0x00]
    
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
      
        # Authenticate with Public key
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, secteurBloc, keyA_Public, uid)
            # Check if authenticated
        if (status == MIFAREReader.MI_OK):
                print ("Authentification Avec la Clee Public ")
                MIFAREReader.MFRC522_Read(secteurBloc)
                MIFAREReader.MFRC522_StopCrypto1()
        else:
            print ("Erreur d\'Authentification Avec la Clee Public ")
       
        time.sleep(3)



