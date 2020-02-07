IoTDeeperDiveOOP2020

Hier finden Teilnehmer des IoT Deeper Dive Tutoriums und andere interessierte Nutzer eines Raspberry Pi alle Resourcen wie zum Beispiel Quelldateien, Handouts, Datenblätter.
Das Tutorium nutzt den Raspberry Pi Zero WH als Zielplattform für die Implementierung eines IoT-Geräts.
Es sind auch andere Raspberry-Pi-Boards nutzbar, sofern sie über WiFi-Funktionalität verfügen.

  Voraussetzung für das Tutorium bzw. das Nachvollziehen des Tutoriums zuhause sind (Bill of Material):

    Eigenes Notebook (Windows, Linux, Mac) mit WLAN-Fähigkeit (WAP, WAP2); 
    falls möglich mit microSD-Leser/Schreiber (für Class 10 microSDs)
    
  Verwendete Programmiersprache
  
    Python 3.x (x >= 7)
  
  Vorgehensweise
  
    Die Übungen setzen einen Raspberry Pi Zero W{H} oder ein anderes Raspberry Pi Board voraus.
  
    Die Arbeit an den Übungen erfolgt über eine sogenannte "headless" Installation: 
    d.h., Zugriff auf Raspi über ssh/sftp. Also Host = PC, Target = Raspberry Pi.
    Alternativ können IoT-Interessierte auch Bildschirm, Maus, Tastatur an den Raspberry Pi anschließen. 
    In diesem Fall ist der Raspberry Pi zugleich Host und Target.
    
    Verwendet wird Raspbian Buster oder höher als Betriebssystem
    
    Notwendig dazu ist auf dem Host-PC (Windows, Mac, Linux, Raspberry Pi) eine WiFi-Funktion.
    
    Die Übungen arbeiten mit LEDs, einem PIR-Sensor (Bewegungsmelder), 
    einem BME280-Modul (Temperatur, Feuchtigkeit, Druck), 
    einem PFC8591 A/D-Wandler Breakout, einer Raspberry Pi Camera.
    
    Benötigt werden des Weiteren ein Breadboard und Jumper-Wires.
    
    In den Übungen erfolgt Zugriff auf ThingSpeak und IFTTT, wofür Teilnehmer 
    ein eigenes Konto anlegen müssen.
    
    Auf dem Raspberry Pi Zero WH mit Raspbian Buster (oder höher) wird im Verlauf des Tutoriums 
    auch Node-RED benutzt (optional)
    
  Agenda
  
    Teil 1) Grundlagen
    Teil 2) Übungen
    Teil 3) Mini Hackathon
  
  
  Die folgende Hardware wird benötigt / vom Veranstalter bzw. Referenten zur Verfügung gestellt 
    (geschätzter Einkaufspreis: 50-60 Euro)
  
    Raspberry Pi Zero WH
    
    Netzteil
    
    microSD-Karte (32 GB, Class 10) mit Buster Lite als OS
    
    PFC8591 Modul
    
    PIR Sensor
    
    BME280 Breakout Board
    
    Raspberry Pi Camera 
    
    Breadboard
    
    LEDs
    
    Widerstände (220 Ohm und 470 Ohm)
    
    Push-Buttons
    
    "Jumper-Cables" (Female/Female, Female/Male und Male/Male)
    
    Ein gemeinsamer WLAN-Zugang (für Notebook und Raspberry Pi)
    
    Lötstation (für notwendige Elektronikarbeiten)
    
    
Optional: Eigene Hardware (z.B. Analogsensoren), Messgeräte
  

Notwendige Software-Installationen (alle Software-Pakete sind frei von Kosten)

    Visual Studio Code (Mac, Linux oder Windows) plus PlugIns für Python 3 und Remote SSH
    Alternativ: Andere IDE oder anderer Editor (z.B., nano, vim, vi)
  
    openSSH-kompatibler Client für den ssh- und sftp-Zugriff auf Raspberry Pi
  
    BalenaEtcher-Software zum Schreiben von microSDs oder alternativ PiBakery
    
    Optional: Fritzing für Schaltungsentwurf
  
Für die Übungen erstellen Teilnehmer eigene Konten auf

    ThingSpeak
  
    IFTTT
    
Die GitHub-Verzeichnisse auf https://github.com/ms1963/IoTDeeperDiveOOP2020 enthalten:

    /src .......... Quellen für die im Tutorium verwendeten Beispiele 
    /datasheets ... Datenblätter, Informationsbroschüren, Python-Tutorial
    /handouts ..... PDF mit Handouts des Tutoriums
    /resources .... PiBakery 2.0 - Rezept zum Erzeugen der microSD (Raspbian Buster)
  
Kopieren des Master-Branches über 

    git clone https://github.com/ms1963/IoTDeeperDiveOOP2020.git 
    
oder als 
    ZIP-Download.
