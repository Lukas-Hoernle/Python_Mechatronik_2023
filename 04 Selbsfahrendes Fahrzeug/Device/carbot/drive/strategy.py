import random

from carbot.sensors.base import SensorBase

class BackAndForthDrive(SensorBase):
    """
    Fahrstrategie: Vor- und zurück ohne zu lenken.
    """
    def __init__(self, direction_change):
        """
        Konsturktor. Parameter:
            * direction_change: Funktion zum Prüfen auf Richtungswechsel
        """
        super().__init__()
        self._direction_change = direction_change

    def update(self, vehicle):
        """
        Sensor prüfen und Fahrzeugparameter anpassen.
        """
        try:
            change = self._direction_change.__next__()
        except:
            return
        
        if change:
            vehicle.direction = 0
            speed = random.randint(0, 10) / 10.0

            if vehicle.target_speed >= 0:
                vehicle.target_speed = speed * -1
            else:
                vehicle.target_speed = speed

class RandomDrive(SensorBase):
    """
    Fahrstrategie: Willkürlich rumkurven.
    """
    def __init__(self, direction_change):
        """
        Konsturktor. Parameter:
            * direction_change: Funktion zum Prüfen auf Richtungswechsel
        """
        super().__init__()
        self._direction_change = direction_change

    def update(self, vehicle):
        """
        Sensor prüfen und Fahrzeugparameter anpassen.
        """
        try:
            change = self._direction_change.__next__()
        except:
            return
        
        if change:
            vehicle.direction = (random.randint(0, 10) - 5) / 10.0
            speed = random.randint(0, 10) / 10.0

            if vehicle.target_speed >= 0:
                vehicle.target_speed = speed * -1
            else:
                vehicle.target_speed = speed