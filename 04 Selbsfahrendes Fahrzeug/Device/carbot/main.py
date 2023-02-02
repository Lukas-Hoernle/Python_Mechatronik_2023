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

    # pigpio-Bibliothek für höhere Genauigkeit verwenden, falls installiert
    try:
        from gpiozero.pins.pigpio import PiGPIOFactory
        from gpiozero import Device
        Device.pin_factory = PiGPIOFactory()
        print("Benutze pigpio für höhere Genauigkeit")
    except:
        pass

    # Fahrzeug starten
    vehicle = Vehicle()
    vehicle.target_speed = 0.5
    vehicle.direction = 0.2
    vehicle.loop_forever()
