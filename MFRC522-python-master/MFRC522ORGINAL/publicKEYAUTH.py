##        
##        # Authenticate with Public key
##        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, secteurBloc,keyA_Public, uid)
##        # Check if authenticated
##        if(status == MIFAREReader.MI_OK):
##                MIFAREReader.MFRC522_Read(secteurBloc)
##                MIFAREReader.MFRC522_StopCrypto1()
##                print ("Authentification Avec la Clee Public ")    
##        else:
##            print ("Erreur d\'Authentification Avec la Clee Public ")