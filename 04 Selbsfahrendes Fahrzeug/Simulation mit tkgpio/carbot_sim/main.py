import asyncio, json, os

# from threading import Thread
from tkgpio import TkCircuit
from gpiozero import Motor

from carbot_sim.vehicle import Vehicle

def main():
    """
    Vom Startskript aufgerufene Hauptfunktion des Programms. Abweichend zur Vollversion
    des Carbots wird hier eine tkgio-Simulation der Fahrzeughardware geladen und dann
    die Funktion `_start_vehicle` mit der eigentlichen Programmlogik aufgerufen.
    """
    file_path = os.path.dirname(__file__)
    file_path = os.path.join(file_path, "tkgpio.json")

    with open(file_path) as json_file:
        config = json.load(json_file)
    
    circuit = TkCircuit(config)
    circuit.run(_main_impl)

def _main_impl():
    """
    Die eigentliche Hauptfunktion des Programms, wenn wir nicht tkgpio zur Simulation
    der Hardware verwenden würden. Hier werden die Objekte zur Ansteuerung der Hardware
    erzeugt und mit `asyncio` nebenläufige Hintergrundtasks für die einzelnen Aufgaben
    des Programms erzeugt: Sensoren überwachen, Motoren ansteuern, ...
    """
    # hardware_thread = Thread(target=lambda: asyncio.run(_start_tasks()))
    # hardware_thread.run()
    asyncio.run(_start_tasks())
    
async def _start_tasks():
    """
    """
    print("carbot_sim sagt Hallo!")

    motor_left = Motor(forward=24, backward=23)
    motor_right = Motor(forward=22, backward=27)

    vehicle = Vehicle(motor_left, motor_right)
    # vehicle.target_speed = 1
    # vehicle.direction = 0.5
    asyncio.create_task(vehicle.drive())

    while True:
        await asyncio.sleep(0)
