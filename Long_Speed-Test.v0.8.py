####################################################################################################
# #   Intro

f0=("""                                                                                
    .,.                                .#,    ..........                    ,.  
  .#M@M#                               .M,   .++%MMMM#++,                 ,%M,  
  %@. ..                               .M,      ,MMMM+     ..       ..   %MMM,. 
  @+      ,..::.    .::.    .::.    ,:,.M,      ,MMMM:   ,##:#+   +@%:%::@MMM%+ 
  %@.    .M+@%@@,  :@+%@,  :@+%@,  %@%##M,      ,MMMM:  ,MM: %M% :MM#. . %MMM,  
  .#M%,  .M@. .## .M,  +# .M,  +# :M,  +M,      ,MMMM:  #MM: %MM,%MMM%.  %MMM,  
    :#M+ .M+   :M.+@,,,+M.+@,,,+M.#%   .M,      ,MMMM: .MMM+,#MM+:MMMM#. %MMM,  
      :M..M:   ,M,%@#####.%@#####.#%   .M,      ,MMMM: .MMM%::::, %MMMM% %MMM,  
      .M,.M:   :M.+@      +@      ##   ,M,      ,MMMM:  @MM:   ..  %MMMM %MMM,..
  ,   +M..M#. .## ,M:     ,M:     :M,  %M,      ,MMMM:  :MM:  .#.. .%MM@ +MMM,+,
  @@#@M: .M#@#@@.  :M###+  :M###+  %M#@+M,      ,MMMM:   +M%,:%, :%:,M@: .#MM#: 
  .,:,.  .M:.:,     .::,    .::,    ,:. ,.      .,,,,.    .::.    .,:,.    .,   
         .M:                                                                   
  #####  .M:  ############################################################                                                         
                             - created by Napo_II
                                    - v0.8
    			          - python 3.7
                - https://github.com/NapoII/Long-Time-Speedtest

""")
print(" \nProgramm wird gestartet ...")
print(" Einzeltest wird ausgeführt ...")

####################################################################################################
#import
import speedtest
import time
from datetime import date
import pandas as pd
import numpy as np
import os.path
import os
import shutil   # um temp Ornder mit inhalt zu löschen
import re
import seaborn as sns
import matplotlib.pyplot as plt 

####################################################################################################

def ERROR_504():
    
    print(f0+"\n")
    print("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMM##########################################MMMM
MMM#                                          #MMM
MMM#                                          #MMM
MMM#                                          #MMM
MMM#                 ,MMMMM+                  #MMM
MMM#                 ,MMMMM+                  #MMM
MMM#                 .MMMMM+                  #MMM
MMM#                 .MMMMM+                  #MMM
MMM#                 .MMMMM:                  #MMM
MMM#                 .MMMMM:                  #MMM
MMM#                  MMMMM:                  #MMM
MMM#                  MMMMM,                  #MMM
MMM#                  @MMMM,                  #MMM
MMM#                  @MMMM,                  #MMM
MMM#                  @MMMM.                  #MMM
MMM#                  #MMMM.                  #MMM
MMM#                  %####.                  #MMM
MMM#                                          #MMM
MMM#                                          #MMM
MMM#                                          #MMM
MMM#                                          #MMM
MMM#                 .+@M@#,                  #MMM
MMM#                .#MMMMMM,                 #MMM
MMM#                :MMMMMMM#                 #MMM
MMM#                +MMMMMMM@                 #MMM
MMM#                ,MMMMMMM%                 #MMM
MMM#                 +MMMMM#.                 #MMM
MMM#                  ,+%%:                   #MMM
MMM#                                          #MMM
MMM#                                          #MMM
MMMM##########################################MMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
    print("""
    >>> Error 522 <<<
    Zeitüberschreitung beim Verbindungsaufbau

    Es wurde keine Internet Verbindung festgestelt:\
    """)
    konti = False
    abfrage = (input("\n Soll für eine Stunde eine ,\nInternet abfrage Schleife durchgeführt werden?`\n(k) für kontinuierlich (y/n): ").lower())
    #abfrage = "y"
    if '-kontinuierlich' in abfrage or '-k' in abfrage or 'k' in abfrage :                # abfrage ob -k in abfrage
        konti = True
        abfrage = "y -k"
    if not '-kontinuierlich' in abfrage and not '-k' in abfrage and not 'k' in abfrage and not "y" in abfrage and not "yes" in abfrage and not "ja" in abfrage and not "j" in abfrage:
        print (" Deine eingabe war ungültig")
        ERROR_504()
    if "y" in abfrage.lower() or "yes" in abfrage.lower() or "ja" in abfrage.lower() or "j" in abfrage.lower():
        print("\n")
        start_time = time.time()
        Zeit_Stempel_ = (time.strftime("%d.%m.%Y %H:%M Uhr"))
        print(Zeit_Stempel_)
        print("\nEs wird eine Internet abfrage durchgeführt...\n")
        while True:
            w_time = 10
            if konti == True :
                w_time = (360*24*60*60)
            current_time = time.time()
            elapsed_time = current_time - start_time        # berechung rest Zeit
            if elapsed_time < w_time:                      # Rest Zeit abgleichn mit Interval
                try:
                    speedtest.Speedtest()
                    print("""
                .,:+%#@@@@@##%+:.                 
             .:%@@@@@@@@@@@@@@@@@#%:.             
          .:#@@@@@@@@@@@@@@@@@@@@@@@@%,           
        .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,         
       :@@@@@@@@@@%+:,.....,,:+#@@@@@@@@@%,       
     ,#@@@@@@@#+,               .,+@@@@@@@@+.     
    +@@@@@@@+,                     .:#@@@@@@#,    
  .%@@@@@@+.     .,+%##@@@##%+:.      ,%@@@@@@:   
 ,#@@@@@%.    .+#@@@@@@@@@@@@@@@#+,     :#@@@@@%. 
,@@@@@@:    ,%@@@@@@@@@@@@@@@@@@@@@#:    .%@@@@@%.
%@@@@#.   ,%@@@@@@@@@@@@@@@@@@@@@@@@@#:    :@@@@@%
.%@@%.  .+@@@@@@@@@%+:,,,,,:+%#@@@@@@@@%.   ,#@@@,
 .%+   ,#@@@@@@@+,             ,+#@@@@@@@:   .#@, 
  .   :@@@@@@#:.                  ,#@@@@@@+.  .,  
     +@@@@@@:     .:+%##@@#%+:.     ,#@@@@@%.     
    ,@@@@@%.    :%@@@@@@@@@@@@@#:.   .+@@@@@#     
     +@@@+    :#@@@@@@@@@@@@@@@@@@+.   ,@@@@:     
      +@:   ,#@@@@@@@@@@@@@@@@@@@@@#,   ,#@:      
       .   :@@@@@@@%+,..  .,:%@@@@@@@+.  .:       
          +@@@@@@+.           .:#@@@@@%.          
         ,@@@@@+.               .:@@@@@#          
          +@@#,     .:+%%%+:.     .#@@@:          
           +#.    ,%@@@@@@@@@#:.   .%@:           
            .   .%@@@@@@@@@@@@@#,    ,            
               :@@@@@@@###@@@@@@@+                
              ,@@@@@%,.    ,+@@@@@+               
               +@@%.   ,,,   .+@@@:               
                ++   :#@@@#:   :@:                
                    :@@@@@@@:   .                 
                   .#@@@@@@@@.                    
                   ,@@@@@@@@@,                    
                   ,@@@@@@@@@,                    
                   .@@@@@@@@@.                    
                    %@@@@@@@%                     
                    .#@@@@@#.                     
                     .+#@#+.    
                     
                     """)
                    print("\nEs wurde eine Internet Verbindung am " + (time.strftime("%d.%m.%Y %H:%M Uhr"))+ " festgestellt.\n")
                    i=input("Beliebige Eingabe um den Speed-Test nun fortzufahren.")
                    break
                except:
                    continue
            else :
                try:
                    speedtest.Speedtest()
                    print("""
                .,:+%#@@@@@##%+:.                 
             .:%@@@@@@@@@@@@@@@@@#%:.             
          .:#@@@@@@@@@@@@@@@@@@@@@@@@%,           
        .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,         
       :@@@@@@@@@@%+:,.....,,:+#@@@@@@@@@%,       
     ,#@@@@@@@#+,               .,+@@@@@@@@+.     
    +@@@@@@@+,                     .:#@@@@@@#,    
  .%@@@@@@+.     .,+%##@@@##%+:.      ,%@@@@@@:   
 ,#@@@@@%.    .+#@@@@@@@@@@@@@@@#+,     :#@@@@@%. 
,@@@@@@:    ,%@@@@@@@@@@@@@@@@@@@@@#:    .%@@@@@%.
%@@@@#.   ,%@@@@@@@@@@@@@@@@@@@@@@@@@#:    :@@@@@%
.%@@%.  .+@@@@@@@@@%+:,,,,,:+%#@@@@@@@@%.   ,#@@@,
 .%+   ,#@@@@@@@+,             ,+#@@@@@@@:   .#@, 
  .   :@@@@@@#:.                  ,#@@@@@@+.  .,  
     +@@@@@@:     .:+%##@@#%+:.     ,#@@@@@%.     
    ,@@@@@%.    :%@@@@@@@@@@@@@#:.   .+@@@@@#     
     +@@@+    :#@@@@@@@@@@@@@@@@@@+.   ,@@@@:     
      +@:   ,#@@@@@@@@@@@@@@@@@@@@@#,   ,#@:      
       .   :@@@@@@@%+,..  .,:%@@@@@@@+.  .:       
          +@@@@@@+.           .:#@@@@@%.          
         ,@@@@@+.               .:@@@@@#          
          +@@#,     .:+%%%+:.     .#@@@:          
           +#.    ,%@@@@@@@@@#:.   .%@:           
            .   .%@@@@@@@@@@@@@#,    ,            
               :@@@@@@@###@@@@@@@+                
              ,@@@@@%,.    ,+@@@@@+               
               +@@%.   ,,,   .+@@@:               
                ++   :#@@@#:   :@:                
                    :@@@@@@@:   .                 
                   .#@@@@@@@@.                    
                   ,@@@@@@@@@,                    
                   ,@@@@@@@@@,                    
                   .@@@@@@@@@.                    
                    %@@@@@@@%                     
                    .#@@@@@#.                     
                     .+#@#+.    
                     
                     """)
                    print("\nEs wurde eine Internet Verbindung am " + (time.strftime("%d.%m.%Y %H:%M Uhr"))+ " festgestellt.\n")
                    i=input("Beliebige Eingabe um den Speed-Test nun fortzufahren.")
                    break
                except:
                    ERROR_504()

####################################################################################################
#Modul Daten werden erhoben
try:
    test = speedtest.Speedtest()
except:
    ERROR_504()
test = speedtest.Speedtest()

start_time = time.time()
aktuellesDatum = date.today()

####################################################################################################
# Einzel Speed Test wird ausgefühert (ausgabe im Intro)

print("\n")
print ("Download Test wird ausgeführt...")
download_Test = test.download()                                 # Download Test wird ausgeführt.
download_result = round((download_Test / 1024 / 1024),2)        # Download Ergebniss wird umgerechnet.

print("Upload Test wird ausgeführt...")
upload_Test = test.upload()                                     # Upload Test wird ausgeführt.
upload_result = round((upload_Test / 1024 / 1024),2)            # Upload Ergebniss wird umgerechnet.

print("Ping Test wird ausgeführt...")
test.get_servers()
best = test.get_best_server()   
ping_Test = test.results.ping                                   # Ping Test wird ausgeführt.
ping_result = round ( ping_Test, 3)                             # Ping Ergebniss wird umgerechnet. (abgerundet)
print("\n")

####################################################################################################
#INTRO
print("\n")
print (f0)

print ("-----------------------------------------------------------")
print ("            " + (time.strftime("%d.%m.%Y %H:%M Uhr")))
print ("-----------------------------------------------------------")
print ("Download:   " + str(download_result) +" Mbit/sec")    
print ("Upload:     " + str(upload_result) +" Mbit/sec")
print ("Ping:       " + str(ping_result) +" ms")
print (f"Server: {best ['host']}")
print (f"von {best ['sponsor']} liegt {best ['d']:.2f} km entfernt in {best['country']}.")
print ("-----------------------------------------------------------")

print("\n")

####################################################################################################
#Instruktionen

print (""" Um eine Langzeitmessung zu starten geben sie die gewünschte Zeit an.
        Sie können in der Zeitabfrage den Parameter -s oder -shutdown
        zusetzlich eingeben wenn sie möchten das der PC
        im anschluss des Langzeittest herunterfährt.
        
Falls sie keine Langzeitmessung durchführen möchten, können sie das Programm jetzt schließen. """ )
print("\n")

while True:
  abfrage = (input("\nZeit in Minuten angeben: ")).lower()
  abfrage_Zahl = False
  zahl=re.findall('\d+[,.]\d+|\d+', abfrage)        # Filtert Zahl aus str
  try:
    zahl=int(zahl[0])
    abfrage_Zahl = True
  except:
    print("""
    Um eine Langzeitmessung zu starten geben sie die gewünschte Zeit an.
        Sie können in der Zeitabfrage den Parameter -s oder -shutdown
        zusetzlich eingeben wenn sie möchten das der PC
        im anschluss des Langzeittest herunterfährt.

Falls sie keine Langzeitmessung durchführen möchten, können sie das Programm jetzt schließen.


    !!! Sie müssen mindestens eine Zahl eingeben. !!!
    """)
  

  only_Strig = ''.join([i for i in abfrage if not i.isdigit()])     # Filtert Buchstaben und - aus Strg

  if "s" in only_Strig or "-s" in only_Strig or "-shutdown" in only_Strig or "shutdown" in only_Strig:
    abfrage_Para = True
  else:
    abfrage_Para = False

  if abfrage_Zahl == True and abfrage_Para == False:
    try:
      int(abfrage)                                      # Über prüft ob nur eine Zahl vorliegt das schelife beden wenn True
      break
    except:
      print("""
    Um eine Langzeitmessung zu starten geben sie die gewünschte Zeit an.
        Sie können in der Zeitabfrage den Parameter -s oder -shutdown
        zusetzlich eingeben wenn sie möchten das der PC
        im anschluss des Langzeittest herunterfährt.

Falls sie keine Langzeitmessung durchführen möchten, können sie das Programm jetzt schließen.

      
      !!! Dieser Parameter exsestiert nicht. !!!
      """)


  if abfrage_Zahl == True and abfrage_Para == True:
    break

print(abfrage)

####################################################################################################
# shutdown ja oder nein min 60min dann ja wenn gewollt.

text = abfrage
shutdown = False
New_Time = False

zahl=re.findall('\d+[,.]\d+|\d+', text) # Filtert aus Eingabe eine Zahl herraus
zahl=int(zahl[0])
Zeit_Interval=zahl
if '-shutdown' in text.lower() or '-s' in text.lower() or 's' in text.lower() :
    if zahl > 59:
        shutdown = True
    else:
        print ("""\n                       ,++.                       
                      ,+,,+.                      
                      +:%%:+                      
                     ::%%%%:,                     
                    .++%%%%:+                     
                    +,%%%%%%::                    
                   .++%%%%%%++.                   
                   +:%%%%%%%%,+                   
                  ,:%%%%%%%%%++.                  
                 .+:%%%%:+%%%%:+                  
                 ::%%%%%..%%%%%:,                 
                .++%%%%:  :%%%%:+.                
                +,%%%%%.  .%%%%%::                
               ,+%%%%%,    :%%%%++.               
               +:%%%%+  ,, .%%%%%,+               
              ::%%%%%..%@@% ,%%%%%:,              
             .+:%%%%: :@@@@, +%%%%:+              
             ::%%%%%. :@@@@, .%%%%%::             
            .++%%%%,  ,@@@@,  :%%%%:+.            
            +:%%%%+   ,@@@@.  .%%%%%,+            
           ,:%%%%%,   .@@@@.   ,%%%%++.           
           +:%%%%+    .@@@#     +%%%%:+           
          ::%%%%%.     @@@#     ,%%%%%:,          
         .++%%%%:      #@@%      +%%%%:+          
         +,%%%%%.      #@@%      .%%%%%::         
        .++%%%%,       %@@+       :%%%%++.        
        +:%%%%+        +@@+       .%%%%%,+        
       ,:%%%%%.        +@@:        ,%%%%++.       
      .+:%%%%:         :@@,         +%%%%:+       
      ::%%%%%.         :@@,         .%%%%%:,      
     .++%%%%:          ,@@.          :%%%%:+.     
     +,%%%%%.           :,           .%%%%%::     
    ,+%%%%%,           .,,            :%%%%++.    
    +:%%%%+           .#@@%           .%%%%%,+    
   ::%%%%%.           :@@@@,           ,%%%%%:,   
  .+:%%%%:            :@@@@,            +%%%%:+   
  :,%%%%%.            .#@@%             .%%%%%::  
 .++%%%%,              .,,.              :%%%%++. 
 +:%%%%%.................................,%%%%%,+ 
,:%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%++.
+:%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:+
+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%++
++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:+
:+::::::::::::::::::::::::::::::::::::::::::::::+,
        
        Der PC fährt nicht herunter !!!!
        Damit der PC nach dem Speedtest herunterfahren soll,
        muss der Test mindestens auf 60 min eingestellt werden.
        """)
        New_Time = (input("Soll die Test Zeit auf 60 min eingestelt werden damit der PC im Anschluss herunterfährt?  (y/n): ")).lower()
        if New_Time == "y" or New_Time == "yes" or New_Time == "ja" or New_Time == "j" :
            New_Time = True
            Zeit_Interval = 60
        else:
            New_Time = False

if '-shutdown' in text.lower() and zahl > 59 or '-s' in text.lower() and zahl > 59 :
  shutdown = True

if shutdown == True or New_Time == True:
    shutdown = True
else :
    shutdown = False

####################################################################################################
#-shutdown -s

if shutdown == True :
    Time_Shoudown_min = Zeit_Interval + 5
    os.system("shutdown -s -t "+ str(Time_Shoudown_min*60))
    print("\n")
    print("Der PC fährt in "+ str(Time_Shoudown_min) + " min herunter.")

####################################################################################################
# Ordner Struktur wird erstllet / geprüft

print("\n")
print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
folder = "Speed_Test_Ergebnisse"
dir = "~/Documents/"+str(folder)           # gibt gewünschten Datei-Pfad an
full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(full_path)
    print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(full_path))
print("\n")

## Unter Ornder nach datum name erstellt
folder = (aktuellesDatum.strftime("%m_%Y"))

full_path = str(full_path)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an

if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(full_path)
    print("Der Ordner ["+ (folder) +"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(full_path))
print("\n")

#####################################################################################################
# Temp Ordner erstllen 

temp_folder = ("temp")

temp_full_path = str(full_path)+"/"+str(temp_folder)           # gibt gewünschten Datei-Pfad an

if os.path.exists(temp_full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(temp_full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(temp_full_path)
    print("Der Ordner ["+ (temp_folder) +"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(temp_full_path))
print("\n")

####################################################################################################
# Temp Datein erstellen

#################### temp datei DL
datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_DW_temp_file = ("DW_SpeedTest-temp-"+(datei_Date))       # Generiert Datei name

save_path = temp_full_path

complete_Name_DW_temp = os.path.join(save_path, name_of_DW_temp_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_DW_temp_file)+"] wird erstellt...")
file1 = open(complete_Name_DW_temp, "a")                                         # Datei erstellen
#toFile = input("Write what you want into the field")                   # Datei input def.
#file1.write(toFile)                                                    # Datei wird gefüllt mit input
file1.close()                                                           # Datei wird gespeichert und geschlossen

#################### temp datei UPL
datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_UPL_temp_file = ("UPL_SpeedTest-temp-"+(datei_Date))       # Generiert Datei name

save_path = temp_full_path

complete_Name_UPL_temp = os.path.join(save_path, name_of_UPL_temp_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_UPL_temp_file)+"] wird erstellt...")
file1 = open(complete_Name_UPL_temp, "a")                                         # Datei erstellen
#toFile = input("Write what you want into the field")                   # Datei input def.
#file1.write(toFile)                                                    # Datei wird gefüllt mit input
file1.close()                                                           # Datei wird gespeichert und geschlossen

#################### temp datei PING
datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_PING_temp_file = ("PING_SpeedTest-temp-"+(datei_Date))       # Generiert Datei name

save_path = temp_full_path

complete_Name_PING_temp = os.path.join(save_path, name_of_PING_temp_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_PING_temp_file)+"] wird erstellt...")
file1 = open(complete_Name_PING_temp, "a")                                         # Datei erstellen
file1.close()                                                          # Datei wird gespeichert und geschlossen

#################### temp datei TIMESTEMP
datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_TIMESTEMP_temp_file = ("TIMESTEMP_SpeedTest-temp-"+(datei_Date))       # Generiert Datei name

save_path = temp_full_path

complete_Name_TIMESTEMP_temp = os.path.join(save_path, name_of_TIMESTEMP_temp_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_TIMESTEMP_temp_file)+"] wird erstellt...")
file1 = open(complete_Name_TIMESTEMP_temp, "a")                                         # Datei erstellen
file1.close()
print("\n")                                                           # Datei wird gespeichert und geschlossen

####################################################################################################
# Speed test nach Zeit intervall

seconds = Zeit_Interval*60                                    # von Sec in min umrechung
x = -1   ## Gibt die anzahl der Messungen an
Zeit_Stempel = (time.strftime("%d.%m.%Y %H:%M Uhr"))
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time > seconds:
        if elapsed_time > 120:
            print("Test beendet. Er lief " + str(int((elapsed_time)/60))  + " Minuten")
        else :
            print("Test beendet. Er lief " + str(int(elapsed_time))  + " Sekunden")
        break
    if elapsed_time < seconds:
        if elapsed_time < seconds:
        
            if seconds-elapsed_time > 120 :
                x=x+1   # Gibt die anzahl der Messungen an
                print(" Es wurden bereits " + str(x) + " Messungen durchgeführt.")
                print("Test endet in "+ str(int((seconds-elapsed_time)/60)) + " Minuten.")

            else :
                x=x+1   # Gibt die anzahl der Messungen an
                print("     Es wurden bereits " + str(x) + " Messungen durchgeführt.")
                print("     Test endet in "+ str(int((seconds-elapsed_time))) + " Sekunden.")


        print("\n")
        print("\n")
        
        print ("Download Test wird ausgeführt...")
        download_Test = test.download()                                 # Download Test wird ausgeführt.
        download_result = round((download_Test / 1024 / 1024),2)        # Download Ergebniss wird umgerechnet.

        print("Upload Test wird ausgeführt...")
        upload_Test = test.upload()                                     # Upload Test wird ausgeführt.
        upload_result = round((upload_Test / 1024 / 1024),2)            # Upload Ergebniss wird umgerechnet.

        print("ping Test wird ausgeführt...")
        test.get_servers()
        best = test.get_best_server()   
        ping_Test = test.results.ping                                   # Ping Test wird ausgeführt.
        ping_result = round ( ping_Test, 3)                             # Ping Ergebniss wird umgerechnet. (abgerundet)

        print ("Zeitstempel wird ausgeführt...")                        # Timestemp wird ausgeführt
        TIMESTEMP = time.time()
        print("\n")

        try:
            speedtest.Speedtest()
            print("\n")
            toFile = str(download_result) + "\n"                         # DL Temp File wird item hinzugefügt
            file1 = open(complete_Name_DW_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_DW_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  
            toFile = str(upload_result) + "\n"         # UPL Temp File wird item hinzugefügt # def inhalt das hinzugefügt wird
            file1 = open(complete_Name_UPL_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_UPL_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  
            toFile = str(ping_result) + "\n"          # Ping Temp File wird item hinzugefügt        # def inhalt das hinzugefügt wird
            file1 = open(complete_Name_PING_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_PING_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()
            toFile = str(TIMESTEMP) + "\n"                         # TimestempTemp File wird item hinzugefügt
            file1 = open(complete_Name_TIMESTEMP_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_TIMESTEMP_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  

            print("\n")
            print ("-----------------------------------------------------------")
            print ("            " + (time.strftime("%d.%m.%Y %H:%M Uhr")))
            print ("-----------------------------------------------------------")
            print ("Download:   " + str(download_result) +" Mbit/sec")    
            print ("Upload:     " + str(upload_result) +" Mbit/sec")
            print ("Ping:       " + str(ping_result) +" ms")
            print (f"Server: {best ['host']}")
            print (f"von {best ['sponsor']} liegt {best ['d']:.2f} km entfernt in {best['country']}.")
            print ("-----------------------------------------------------------")
            
        except:
            print("\n")
            toFile = str(0) + "\n"                         # DL Temp File wird item hinzugefügt
            file1 = open(complete_Name_DW_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_DW_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  
            toFile = str(0) + "\n"         # UPL Temp File wird item hinzugefügt # def inhalt das hinzugefügt wird
            file1 = open(complete_Name_UPL_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_UPL_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  
            toFile = str(0) + "\n"          # Ping Temp File wird item hinzugefügt        # def inhalt das hinzugefügt wird
            file1 = open(complete_Name_PING_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_PING_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            toFile = str(0) + "\n"                         # DL Temp File wird item hinzugefügt
            file1 = open(complete_Name_DW_temp, "a")                                 # Datei wird geöffnet
            print("Datei ["+str(name_of_DW_temp_file) + "] wird beschrieben und gespeichtert...")
            file1.write(toFile)                                             # Datei wird gefüllt mit input
            file1.close()  
            file1.close()
            print("\n")
            print ("-----------------------------------------------------------")
            print ("               " + (time.strftime("%d.%m.%Y %H:%M Uhr")))
            print ("-----------------------------------------------------------")
            print ("                  >>> Error 522 <<<")
            print ("        Zeitüberschreitung beim Verbindungsaufbau")
            print ("-----------------------------------------------------------")
            print ("Test wird Pausiert für 30 sec um das Ergebnis nicht zu verfälschen.")
            print ("-----------------------------------------------------------")
            start_time_504 = time.time()
            seconds_504 = 30
            while True:                                                  # Zeit schelife startet
                current_time504 = time.time()
                elapsed_time504 = current_time504 - start_time_504        # berechung rest Zeit
                if elapsed_time504 < seconds_504:                        # Rest Zeit abgleichn mit Interval
                    continue
                else :
                    break

####################################################################################################
# Ende der Messung 
Zeit_Stempel_end = (time.strftime("%d.%m.%Y %H:%M Uhr"))
End_time = time.time()



####################################################################################################
# erhobene daten aus temp auslesen

# Listen erstellen
download_result_list = []
upload_result_list = []
ping_result_list = []
timestemp_list = []

###################### Daten auslesen aus DW temp
print("\nGemessene Daten werden aus Temp Datei ausgelesen...")

with open(complete_Name_DW_temp,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  download_result_list.append(float(item))

###################### Daten auslesen aus UPL temp
with open(complete_Name_UPL_temp,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  upload_result_list.append(float(item))

###################### Daten auslesen aus PING temp
with open(complete_Name_PING_temp,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  ping_result_list.append(float(item))
###################### Daten auslesen aus TIMESTEMP temp
with open(complete_Name_TIMESTEMP_temp,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  timestemp_list.append(float(item))

pd_timestemp_list=[]
for item in timestemp_list:                        # Liste in Panda Datum umwandeln
    a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item))
    b =pd.to_datetime(a,dayfirst=True)
    pd_timestemp_list.append(b)

###################### Daten zussamen fassen in panda data frame

index = pd_timestemp_list
df = pd.DataFrame(ping_result_list, index = index, columns =['Ping (ms)'])
df.insert(0, "Upload (Mbit/sec)", upload_result_list, allow_duplicates=True)
df.insert(0, "Download (Mbit/sec)", download_result_list, allow_duplicates=True)

# erhobene Daten
print("Folgende Daten wurden im Test gemessen:\n")

print(df)

print("\n")

####################################################################################################
# text Datei erstellen nach Datum und Uhrzeit

datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_file = ("SpeedTest-"+(datei_Date))                      # Generiert Datei name

save_path = full_path

completeName = os.path.join(save_path, name_of_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_file)+"] wird erstellt...")
file1 = open(completeName, "a")                                 # Datei erstellen
file1.close()                                                   # Datei wird gespeichert und geschlossen

####################################################################################################
### Standat abweichung ###


### Standat  DL abweichung ###
f1 = "Das Ergebniss des Download Tests: \n"
print(f1)
data = np.array([download_result_list])

data_size = data.size               # size gibt die länge der Liste an
f2=("\nAnzahl der Messungen:							"+str(data_size)+"\n")
print(f2)

data_Sum = data.sum()                        # gibt die summe des listen inhalts an 

data_m = np.mean(data)              # (data_Sum/data_len) gibt die mean an
f3 = ("Der Mittelwert der beträgt:						" + str(int(data_m)))+"\n"
print(f3)
data_Var = np.var(data)

data_std =np.std(data)

data_m_plus = data_m + data_std  # range inerhalb der Standartabweichung +
data_m_minus = data_m - data_std # range inerhalb der Standartabweichung -
f4 = ("Die Standardabweichung Grenze liegt am rand von:			"+str(int(data_m_plus)) + " und " + str(int(data_m_minus)))+"\n"+"\n"
print(f4)
data_Ü_St = data[(data > data_m_plus)] #data_Ü_St = Data der Standardabweichung über der Normal verteilung
data_Ü_St_Size = data_Ü_St.size  # Die Anzahl der abweichungen über der Standardabweichung

data_U_St = data[(data < data_m_minus)] #data_U_St = Data der Standardabweichung unter der Normal verteilung
data_U_St_Size = data_U_St.size  # Die Anzahl der abweichungen unter der Standardabweichung


data_St = np.append(data_U_St,data_Ü_St)
data_St_Size = data_St.size # Die Anzahl der abweichungen der Standardabweichung

f5 = ("Die Anzahl der abweichungen der Standardabweichung:			" + str(data_St_Size)+"\n")
f6 = (str(data_St)+"\n"+"\n")
f7 = ("Die Anzahl der abweichungen über der Standardabweichung:		" + str(data_Ü_St_Size)+"\n")
f8 = (str(data_Ü_St)+"\n"+"\n")
f9 = ("Die Anzahl der abweichungen unter der Standardabweichung: 		" + str(data_U_St_Size)+"\n")
f10 = (str(data_U_St)+"\n"+"\n")
print(f5+f6+f7+f8+f9+f10)

data_P = data[(data < data_m_plus) & (data > data_m_minus) ]    
data_P_Size  = data_P.size # Die Anzahl der Werte die inerhalb der Standardabweichung liegen

f11= ("Die Anzahl der Werte die inerhalb der Standardabweichung liegen:         " + str(data_P_Size)+ "\n")
f12 = (str(data_P) + "\n"+"\n"+"\n Alle Werte im Überblick:\n")
print (f11+f12)


#################
#Test Datei header
f01 = ("\n\n Die Messung began am \n"+ str(Zeit_Stempel)+ " und leif bis zum: "+ str(Zeit_Stempel_end) +"\n Dauer: "+str(int((elapsed_time)/60)) +" min.\n\n")



### Data in Text Datei gespeichert

toFile = f0 +f01 +f1 + f2 +f3 +f4 +f5 +f6 +f7 +f8 +f9 +f10 +f11 +f12                             # def inhalt das hinzugefügt wird
file1 = open(completeName, "a")                                 # Datei wird geöffnet
print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
file1.write(toFile)                                             # Datei wird gefüllt mit input
file1.close()                                                   # Datei wird geschlossen und gespeichert

toFile = str(df)                             # def inhalt das hinzugefügt wird
file1 = open(completeName, "a")                                 # Datei wird geöffnet
print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
file1.write(toFile)                                             # Datei wird gefüllt mit input
file1.close()                                                   # Datei wird geschlossen und gespeichert

print("\n")

####################################################################################################
#Erstellt graph
print ("\nUm das Programm fortzufahren schließen sie den Graph und speichern ihn vorher bei bedarf ab.\n ")
plt.close("all")
df.plot()
plt.show()

#name_of_file_g = ("SpeedTest-Graph-"+(datei_Date))                      # Generiert Datei name für graph
#save_path = full_path
#completeName_g = os.path.join(save_path, name_of_file_g +".png") 
#plt.savefig(completeName_g)                                             # Speichert graph ab


####################################################################################################
#Temp Ordner mit inhalt lösch abfrage

print("""Temporäre Dateien und Ordner werden nicht mehr benötigt.
    ->  """+str(temp_full_path)+"\n")

delt_temp = (input("Dürfen die Temporäre Dateien und Ordner nun gelöscht werden? (y/n): ")).lower()

if delt_temp == "y" or delt_temp == "yes" or delt_temp == "ja" :
    print("Temporära Ordner wird gelöscht ")
    print("     -> " + temp_full_path)
    shutil.rmtree(temp_full_path)
else :
    print("Der Ordner wurde nicht gelöscht")
    print("     ->"+str(temp_full_path))

####################################################################################################
print("\n")
End=(input("Beliebige Eingabe um das Programm zu schließen."))
####################################################################################################


####################################################################################################

#       T O   D O   L I S T
#   - Daten auswertung def
#   - help/info Text schreiben
#   - Server daten in Text Datei hinzufügen
#   - outro mit 5 sec max
#   - graf save bug