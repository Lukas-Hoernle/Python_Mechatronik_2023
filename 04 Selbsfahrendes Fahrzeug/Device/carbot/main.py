#! /usr/bin/env python3

# https://docs.circuitpython.org/en/latest/shared-bindings/board/index.html
# https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
# https://docs.circuitpython.org/projects/pca9685/en/latest/index.html
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685

from carbot.vehicle import Vehicle
from carbot.sensors.obstacle import ObstacleSensor
from carbot.sensors.direction import DirectionServo
from carbot.drive import direction_change
from carbot.drive.strategy import BackAndForthDrive, RandomDrive

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

    # PCA9685-Baustein für die PWM-Steuerung der Motoren
    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c)
    pca.frequency = 60

    # Fahrzeug starten
    vehicle = Vehicle(pca)

    vehicle.add_sensor("obstacle", ObstacleSensor(trigger=20, echo=21, min_cm=10, max_cm=50))
    vehicle.add_sensor("direction", DirectionServo(pca, pwmChannel=15))
    vehicle.add_sensor("drive", BackAndForthDrive(direction_change.onObstacle(vehicle, 0.9)))

    #vehicle.target_speed = 0
    #vehicle.direction = 0.2

    try:
        vehicle.loop_forever()
    except KeyboardInterrupt:
        vehicle.stop()
