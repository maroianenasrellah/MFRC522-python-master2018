        # Authenticate with private key
##        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, secteurBloc,keyA_Privé, uid)
##
##        # Check if authenticated
##        if (status == MIFAREReader.MI_OK):
##            MIFAREReader.MFRC522_Read(secteurBloc)
##            MIFAREReader.MFRC522_StopCrypto1()
##            cmpt=cmpt+1
##           # print("card readed Number: ",cmpt)
##            break
##        else:
##            print ("Erreur d\'Authentification Avec la Clee keyA_Privé ")
##            print('\n')
##  