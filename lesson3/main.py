import time
import random
import logging

logging.basicConfig(filename='lesson3/sensor_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def temp_sensor():
    while True:
        yield random.uniform(20.0, 40.0)
        time.sleep(1)

def pressure_sensor():
    while True:
        yield random.uniform(900, 1100)
        time.sleep(1)

def sensor_handler(func): # приймає фнк яку потрібно декорувати
    def wrapper(self, sensor_func, *args, **kwargs): # викликається ця фнк. Приймає (об'єкт, фнк типу temp_sensor(), та інші)
        for data in sensor_func():
            func(self, data) # отримує дані які генеруються
    return wrapper # повертає

class SensorSystem:
    @sensor_handler
    def handle_temp(self, data):
        logging.info(f"Temp: {data:.2f}")
        if data > 35:
            logging.info(f"High temp: {data:.2f}") # .toFixed(2)

    @sensor_handler
    def handle_pressure(self, data):
        logging.info(f"Pressure: {data:.2f}")
        if data < 950:
            logging.info(f"Low pressure: {data:.2f}")

system = SensorSystem()

try:
    system.handle_temp(temp_sensor)
    system.handle_pressure(pressure_sensor)
except KeyboardInterrupt:
    print("Stop")