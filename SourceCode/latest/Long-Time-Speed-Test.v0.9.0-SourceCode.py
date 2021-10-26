####################################################################################################
# #   Intro
v = "v0.9.0"

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
                                    - """ + v + """
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
import os.path
import shutil   # um temp Ornder mit inhalt zu löschen
import re
import matplotlib.pyplot as plt
import winsound
import sys
import os
from os import listdir
from os.path import isfile, join
import shutil   # um temp Ornder mit inhalt zu löschen

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

                    frequency = 3000  # Set Frequency To 2500 Hertz
                    duration = 500  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)
                    frequency = 37  # Set Frequency To 2500 Hertz
                    duration = 500  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)

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

                    frequency = 3000  # Set Frequency To 2500 Hertz
                    duration = 500  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)
                    frequency = 37  # Set Frequency To 2500 Hertz
                    duration = 500  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)

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

zahl =re.findall('\d+[,.]\d+|\d+', text) # Filtert aus Eingabe eine Zahl herraus
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
            while True:                                                  # Zeit schleife startet
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
data_size = len(download_result_list)
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
f00 = "--------------------------------------------------------------------------------------------------------------------------\n"
f000 ="---------------------------------\n"
print(f00)
####################################################################################################
# Auswertung

df_mean = df.mean(axis=None, skipna=None, level=None, numeric_only=None,)
df_median = df.median(axis=None, skipna=None, level=None, numeric_only=None,)
df_max = df.max(axis=None, skipna=None, level=None, numeric_only=None,)
df_min = df.min(axis=None, skipna=None, level=None, numeric_only=None,)


f1 = "Spezifische Werte aus der Messung: \n"
print(f1+f00)

f2 = ("Die Durchschnittswerte der Messung: ")
print(f2)
print(f000)
print((df_mean.to_string()))    # Mittelwert
print(f000)

print("\n")

f3 = ("Die Niederstwert der Messung liegen bei: ")
print(f3)
print(f000)
print((df_min.to_string()))     # min wert
print(f000)

print("\n")

f4 = ("Die Höchstwerte der Messung liegen bei: ")
print(f4)
print(f000)
print((df_max.to_string()))     # max wert
print(f000)

f5 = """Alle gemessenen Werte:
------------------------------------------------------------------------"""
print("\n")

####################################################################################################




#################
#Test Datei header

f01 = ("Es wurde ein Langzeit-Speed-Test am "+ str(aktuellesDatum.strftime("%d.%m.%Y"))+ " durchgefüht. Die Messung began am\n" + str(Zeit_Stempel)+ " und leif bis zum: "+ str(Zeit_Stempel_end) +". Sie dauerte "+str(int((elapsed_time)/60)) +" min und es wurden "+ str(data_size) + " Messungen durchgeführt.\n")

### Data in Text Datei gespeichert

toFile = f0 +f00*2 +f01 +f00*2 +"\n" +f1 + "\n" + f2 + "\n" +f000 + (df_mean.to_string()) +"\n" + f000+ "\n" +f3 +"\n" + f000 + (df_min.to_string()) +"\n" + f000 +"\n"+ f4 +"\n" + f000 + (df_max.to_string()) + "\n" + f000 + "\n" + f5 + "\n"              # def inhalt das hinzugefügt wird
file1 = open(completeName, "a")                                 # Datei wird geöffnet
print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
file1.write(toFile)                                             # Datei wird gefüllt mit input
file1.close()                                                   # Datei wird geschlossen und gespeichert

pd.set_option('display.max_rows', None)
toFile = (df.to_string())                            # def inhalt das hinzugefügt wird
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
os.system(completeName)
kill = (input("Sollen alle vorhanden Daten nun zussamen gefasst werden? (y/n): ")).lower()

if kill == "n" or kill == "no" or kill == "nein" :
    print("Program wird geschlossen ")
    sys.exit()

####################################################################################################

####################################################################################################
# #   Intro
v2 = "Dataframe summaries on base of "+ v

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
                      - """ + v2 + """
    			          - python 3.7
                - https://github.com/NapoII/Long-Time-Speedtest

""")
print(f0)
print(" Dataframes werden zussaemn gefügt ...\n")

####################################################################################################

folder = "Speed_Test_Ergebnisse"
dir = "~/Documents/"+str(folder)           # gibt gewünschten Datei-Pfad an
full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

#####################################################################################################
# Temp Ordner erstllen für Fulltime Data

temp_folder_full_Time = ("temp_fullTime")

temp_full_path = str(full_path)+"/"+str(temp_folder_full_Time)           # gibt gewünschten Datei-Pfad an
data_string_Len = 0
FullData = temp_full_path + "FullData.txt"

if os.path.exists(temp_full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(temp_full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(temp_full_path)
    print("Der Ordner ["+ (temp_folder_full_Time) +"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(temp_full_path))
print("\n")

####################################################################################################
# Temp Datein erstellen für Fulltime Data

#################### temp datei DL für Fulltime Data
datei_Date_full_Time = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_DW_temp_file_full_Time = ("DW_SpeedTest-temp_full_Time-"+(datei_Date_full_Time))       # Generiert Datei name

save_path = temp_full_path

complete_Name_DW_temp_full_Time = os.path.join(save_path, name_of_DW_temp_file_full_Time+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_DW_temp_file_full_Time)+"] wird erstellt...")
file1 = open(complete_Name_DW_temp_full_Time, "a")                                         # Datei erstellen
#toFile = input("Write what you want into the field")                   # Datei input def.
#file1.write(toFile)                                                    # Datei wird gefüllt mit input
file1.close()                                                           # Datei wird gespeichert und geschlossen

#################### temp datei UPL für Fulltime Data
datei_Date_full_Time = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_UPL_temp_file_full_Time = ("UPL_SpeedTest-temp-_full_Time"+(datei_Date_full_Time))       # Generiert Datei name

save_path = temp_full_path

complete_Name_UPL_temp_full_Time = os.path.join(save_path, name_of_UPL_temp_file_full_Time+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_UPL_temp_file_full_Time)+"] wird erstellt...")
file1 = open(complete_Name_UPL_temp_full_Time, "a")                                         # Datei erstellen
#toFile = input("Write what you want into the field")                   # Datei input def.
#file1.write(toFile)                                                    # Datei wird gefüllt mit input
file1.close()                                                           # Datei wird gespeichert und geschlossen

#################### temp datei PING für Fulltime Data
datei_Date_full_Time = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_PING_temp_file_full_Time = ("PING_SpeedTest-temp_full_Time-"+(datei_Date_full_Time))       # Generiert Datei name

save_path = temp_full_path

complete_Name_PING_temp_full_Time = os.path.join(save_path, name_of_PING_temp_file_full_Time+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_PING_temp_file_full_Time)+"] wird erstellt...")
file1 = open(complete_Name_PING_temp_full_Time, "a")                                         # Datei erstellen
file1.close()                                                          # Datei wird gespeichert und geschlossen

#################### temp datei TIMESTEMP
datei_Date_full_Time = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_TIMESTEMP_temp_file_full_Time = ("TIMESTEMP_SpeedTest-temp_full_Time-"+(datei_Date_full_Time))       # Generiert Datei name

save_path = temp_full_path

complete_Name_TIMESTEMP_temp_full_Time = os.path.join(save_path, name_of_TIMESTEMP_temp_file_full_Time+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_TIMESTEMP_temp_file_full_Time)+"] wird erstellt...")
file1 = open(complete_Name_TIMESTEMP_temp_full_Time, "a")                                         # Datei erstellen
file1.close()
print("\n")                                                           # Datei wird gespeichert und geschlossen

####################################################################################################
# Data aus txt auslesen pasresen und zu einer datei zusammen fügen.


Main_Folder = []
paths = []
path = full_path

for file in os.listdir(path):   # Liest die Monats über Ordner in Ergebnisse aus
  if os.path.isdir(file):
    paths.append(file) 
  else:
      Main_Folder.append(file)
Main_Folder.remove('temp_fullTime')
try:
  Main_Folder.remove('SpeedTest-Full_dataset.txt')
  Main_Folder.remove('temp_fullTimeFullData.txt')
  
except:
  print("Es ist noch kein Gesamt Dataframe vorhanden.\n")


Folder_Len = len(Main_Folder)+1   # Entimmt eine Folder nach einander.

Monate_an_data = len(Main_Folder)
print("Es wurden für "+str(Monate_an_data)+" Monate Daten gefunden.\n")
full_file_Monat =[]
while True:
  Folder_Len= Folder_Len - 1
  if Folder_Len == 0:
    break

  Folder_1 = Main_Folder.pop()

  full_path_Monat = full_path + "/" + Folder_1
  print("\nEs werden Daten aus dem Ordner --> " + str(full_path_Monat)+ " zussamen gefügt.\n" )

  Datei_list = [ f for f in listdir(full_path_Monat) if isfile(join(full_path_Monat,f)) ] # liest datein namen aus und fügt sie einer Liste hinzu.

  Datei_list_len = len(Datei_list)
  print("Es wurden "+str(Datei_list_len) + " Daten gefunden: \n")
  
  Datei_list_len = Datei_list_len +1
  while True:
      Datei_list_len = Datei_list_len - 1
      if Datei_list_len == 0 :
        break
      Main_Datei = Datei_list.pop()
      Full_datei_path = full_path_Monat + "/" + Main_Datei
      print(Full_datei_path)
      TakeFile = Full_datei_path

      with open(TakeFile) as f:
          data_string = f.readlines()[54:]
      data_string = ''.join(str(e) for e in data_string)

      datei = open(FullData,'a')
      datei.write(str(data_string)+"\n")                                         # Datei wird gefüllt mit input
      datei.close()

######################
print("\n")
FullData_string_Len = 0
datei = open(FullData,'r')
for line in datei:                                                     # zählt die länge des Data Frames
  FullData_string_Len = FullData_string_Len + 1
datei.close()
print("Es wurden insgesamt "+ str(FullData_string_Len)+ " messungen erhoben und verarbeitet.")
FullData_string_Len_text = FullData_string_Len

while True:
  FullData_string_Len = FullData_string_Len - 1
  if FullData_string_Len == 0 :
    break
  with open(FullData) as f:
    data_string_Line = f.readlines()[FullData_string_Len]
    pd_timestemp_list_full_Time = data_string_Line[0:19:1] + "\n"
    download_result_list_full_Time = data_string_Line[35:42]+ "\n"
    upload_result_list_full_Time = data_string_Line[54:59]+ "\n"
    ping_result_list_full_Time = data_string_Line[64:]
    ping_result_list_full_Time = ping_result_list_full_Time.replace(" ", "")   
                
    datei = open(complete_Name_TIMESTEMP_temp_full_Time,'a')
    datei.write(str(pd_timestemp_list_full_Time))                                         # Datei wird gefüllt mit input
    datei.close()

    datei = open(complete_Name_DW_temp_full_Time,'a')
    datei.write(str(download_result_list_full_Time))                                         # Datei wird gefüllt mit input
    datei.close()

    datei = open(complete_Name_UPL_temp_full_Time,'a')
    datei.write(str(upload_result_list_full_Time))                                         # Datei wird gefüllt mit input
    datei.close()

    datei = open(complete_Name_PING_temp_full_Time,'a')
    datei.write(str(ping_result_list_full_Time))                                      # Datei wird gefüllt mit input
    datei.close()


###################### Daten auslesen aus DW temp
print("\nGemessene Daten werden aus Temp Datei ausgelesen...")
download_result_list_full_Time = []
upload_result_list_full_Time = []
ping_result_list_full_Time = []
pd_timestemp_list_full_Time = []

with open(complete_Name_DW_temp_full_Time,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  download_result_list_full_Time.append(float(item))

###################### Daten auslesen aus UPL temp
with open(complete_Name_UPL_temp_full_Time,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  upload_result_list_full_Time.append(float(item))

###################### Daten auslesen aus PING temp
with open(complete_Name_PING_temp_full_Time,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  ping_result_list_full_Time.append(float(item))

###################### Daten auslesen aus TIMESTEMP temp
with open(complete_Name_TIMESTEMP_temp_full_Time,"r") as file:       # daten aus temp  file stripen
  list_of_strings= []
  for line in file:
    list_of_strings += [line.strip()]

for item in list_of_strings:                        # Liste mit str in flot umwandeln
  pd_timestemp_list_full_Time.append((item))

###################### Daten zussamen fassen in panda data frame
data_string_Len = 0 
data_size = data_string_Len
index = pd_timestemp_list_full_Time
df = pd.DataFrame(ping_result_list_full_Time, index = index, columns =['Ping (ms)'])
df.insert(0, "Upload (Mbit/sec)", upload_result_list_full_Time, allow_duplicates=True)
df.insert(0, "Download (Mbit/sec)", download_result_list_full_Time, allow_duplicates=True)

# erhobene Daten
#print("Folgende Daten wurden im Test gemessen:\n")

#print(df)

print("\n")

####################################################################################################
# text Datei erstellen nach Datum und Uhrzeit

datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
name_of_file = ("SpeedTest-Full_dataset")                      # Generiert Datei name

save_path = full_path

completeName = os.path.join(save_path, name_of_file+".txt")     # Path + text datei name

datei = open(completeName,'w')
datei.write("")                                         # Datei wird gefüllt mit input
datei.close()

print("Textdatei ["+str(name_of_file)+"] wird erstellt...")
file1 = open(completeName, "a")                                 # Datei erstellen
file1.close()                                                   # Datei wird gespeichert und geschlossen

####################################################################################################
f00 = "--------------------------------------------------------------------------------------------------------------------------\n"
f000 ="---------------------------------\n"
print(f00)
####################################################################################################
# Auswertung

df_mean = df.mean(axis=None, skipna=None, level=None, numeric_only=None,)
df_median = df.median(axis=None, skipna=None, level=None, numeric_only=None,)
df_max = df.max(axis=None, skipna=None, level=None, numeric_only=None,)
df_min = df.min(axis=None, skipna=None, level=None, numeric_only=None,)


f1 = "Spezifische Werte aus der Messung: \n"
print(f1+f00)

f2 = ("Die Durchschnittswerte der Messung: ")
print(f2)
print(f000)
print((df_mean.to_string()))    # Mittelwert
print(f000)

print("\n")

f3 = ("Die Niederstwert der Messung liegen bei: ")
print(f3)
print(f000)
print((df_min.to_string()))     # min wert
print(f000)

print("\n")

f4 = ("Die Höchstwerte der Messung liegen bei: ")
print(f4)
print(f000)
print((df_max.to_string()))     # max wert
print(f000)

f5 = """Alle gemessenen Werte:
------------------------------------------------------------------------"""
print("\n")

####################################################################################################

#################
#Test Datei header

f01 = ("Es wurden "+str(FullData_string_Len_text) + " Messnungen von "+str(Monate_an_data)+" Monaten erhoben und in einen Dataframe zussamen gefügt.\n")

### Data in Text Datei gespeichert

toFile = f0 +f00*2 +f01 +f00*2 +"\n" +f1 + "\n" + f2 + "\n" +f000 + (df_mean.to_string()) +"\n" + f000+ "\n" +f3 +"\n" + f000 + (df_min.to_string()) +"\n" + f000 +"\n"+ f4 +"\n" + f000 + (df_max.to_string()) + "\n" + f000 + "\n" + f5 + "\n"              # def inhalt das hinzugefügt wird
file1 = open(completeName, "a")                                 # Datei wird geöffnet
print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
file1.write(toFile)                                             # Datei wird gefüllt mit input
file1.close()                                                   # Datei wird geschlossen und gespeichert

pd.set_option('display.max_rows', None)
toFile = (df.to_string())                            # def inhalt das hinzugefügt wird
file1 = open(completeName, "a")                                 # Datei wird geöffnet
print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
file1.write(toFile)                                             # Datei wird gefüllt mit input
file1.close()                                                   # Datei wird geschlossen und gespeichert

print("\n")

####################################################################################################

####################################################################################################
print ("\nUm das Programm fortzufahren schließen sie den Graph und speichern ihn vorher bei bedarf ab.\n ")
plt.close("all")
df.plot()
plt.show()

####################################################################################################
#Temp Ordner mit inhalt lösch abfrage

print("""Temporäre Dateien und Ordner werden nicht mehr benötigt.y
    ->  """+str(temp_full_path)+"\n")

delt_temp = (input("Dürfen die Temporäre Dateien und Ordner nun gelöscht werden? (y/n): ")).lower()

if delt_temp == "y" or delt_temp == "yes" or delt_temp == "ja" :
    print("Temporäre Datei wird gelöscht ")
    print("     -> " + temp_full_path)
    try:
      os.remove(FullData)
    except OSError as e:
      print(e)
else :
    print("Der Ordner wurde nicht gelöscht")
    print("     ->"+str(temp_full_path))
    print("     ->"+str(FullData))

try:
    shutil.rmtree(temp_full_path)
except OSError as e:
    print(e)
else:
    print("Die Temporären Ornder wurden gelöscht")


####################################################################################################
os.system(completeName)
####################################################################################################

#       T O   D O   L I S T
#   - help/info Text schreiben
#   - outro mit 5 sec max
#   - graf save bug
#   - log file graf generator

########################################