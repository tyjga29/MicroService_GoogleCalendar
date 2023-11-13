# MicroService_Spotify
Für DHBW 5. Semester ASE

Dieser Microservice erfüllt zwei Funktionen.
1. Mit den gegebenen Authentifikationen holt er alle relevanten Termine von dem Google Account und
2. Schickt sie über MQTT weiter

Um einen täglichen Ablauf zu starten (morgens um 1 Uhr werden beide Funktionen ausgeführt) script.py starten.


Needed libraries (pip install):
    --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    paho-mqtt
    pymongo
    pyyaml
