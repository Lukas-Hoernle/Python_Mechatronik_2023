#! /usr/bin/env python3

from carbot.vehicle import Vehicle

def main():
    """
    Vom Startskript aufgerufene Hauptfunktion des Programms. Hier werden die
    Objekte zur Steuerung des Fahrzeug konfiguriert und miteinander verknüpft.
    Anschließend wird die in der Klasse `Vehicle` implementierte Hauptschleife
    gestartet.
    """
    print("carbot sagt Hallo!")

    vehicle = Vehicle()
    vehicle.target_speed = 0.5
    vehicle.loop_forever()
