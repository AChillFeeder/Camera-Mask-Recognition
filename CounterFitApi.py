
import requests

class CounterFitApi:
    def __init__(self, host, port) -> None:

        self.host = host
        self.port = port
        self.address = f"{self.host}:{self.port}"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} # In case I need it

        self.available_sensors = {
            "Temperature": {"default_unit": "Celsius", "value_type": "float"}, 
            "Button": {"default_unit": "", "value_type": "boolean"},
        }

        self.available_actuators = {
            "Relay", "LED"
        }

    def createSensor(self, type, pin, unit=None):
        type = type.capitalize()
        if type in self.available_sensors:
            unit = unit or self.available_sensors[type]["default_unit"] # use default unit if none is provided
        else:
            print("TYPE provided isn't supported, please use one in the following list\n" + self.available_sensors)
            return 0

        requests.post(
            f"{self.address}/create_sensor", json={
                "type": type,
                "pin": pin,
                "unit": unit
            }
        )

    def createActuator(self, type, port):
        type = type.capitalize()
        if not type in self.available_actuators:
            print("TYPE provided isn't supported, please use one in the following list\n" + self.available_actuators)
            return 0

        requests.post(
            f"{self.address}/create_actuator", json={
                "type": type,
                "port": port
            }
        )

    def editSensor(self, type, port, value, is_random=False, random_min=0, random_max=1):

        type = type.capitalize()
        if not type in self.available_sensors:
            print("TYPE provided isn't supported, please use one in the following list\n" + self.available_sensors)
            return 0

        requests.post(
            f"{self.address}/{self.available_sensors[type]['value_type']}_sensor_settings", json={
                "port": port,
                "value": value,
                "is_random": is_random,
                "random_min": random_min,
                "random_max": random_max
            }
        )
        
    def editActuator(self, port, color, type="LED"):

        type = type.capitalize()
        if not type in self.available_actuators:
            print("TYPE provided isn't supported, please use one in the following list\n" + self.available_actuators)
            return 0

        requests.post(
            f"{self.address}/{type}_actuator_settings", json={
                "port": port,
                "color": color,
            }
        )


