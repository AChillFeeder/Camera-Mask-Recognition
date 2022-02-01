
import requests
import json

class CounterFitApi:
    def __init__(self, host, port) -> None:

        self.host = host
        self.port = port
        self.address = f"http://{self.host}:{self.port}"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} # In case I need it

        self.available_sensors = {
            "Temperature": {"default_unit": "Celsius", "value_type": "float"}, 
            "Button": {"default_unit": "", "value_type": "boolean"},
        }

        self.available_actuators = {
            "Relay", "LED"
        }

    def createSensor(self, type, pin, unit=None):
        
        if type in self.available_sensors:
            unit = unit or self.available_sensors[type]["default_unit"] # use default unit if none is provided
        else:
            print(f"TYPE {type} isn't supported, use one from the following list\n" + str(self.available_sensors))
            return 0

        requests.post(
            f"{self.address}/create_sensor", json={
                "type": type,
                "pin": pin,
                "unit": unit
            }
        )

    def createActuator(self, type, pin):
        
        if not type in self.available_actuators:
            print(f"TYPE {type} isn't supported, use one from the following list\n" + str(self.available_actuators))
            return 0

        requests.post(
            f"{self.address}/create_actuator", json={
                "type": type,
                "port": pin
            }
        )

    def editSensor(self, type, pin, value, **randomization_settings):

        # Optional / Inexistant parameters in some elements but necessary in others
        is_random = False if not "is_random" in randomization_settings else randomization_settings["is_random"]
        random_min = 0 if not "random_min" in randomization_settings else randomization_settings["random_min"]
        random_max = 1 if not "random_max" in randomization_settings else randomization_settings["random_max"]

        
        if not type in self.available_sensors:
            print(f"TYPE {type} isn't supported, use one from the following list\n" + str(self.available_sensors))
            return 0

        requests.post(
            f"{self.address}/{self.available_sensors[type]['value_type']}_sensor_settings", json={
                "port": pin,
                "value": value,
                "is_random": is_random,
                "random_min": random_min,
                "random_max": random_max
            }
        )
        
    def editActuator(self, pin, type="LED", color=""):

        if not type in self.available_actuators:
            print(f"TYPE {type} isn't supported, use one from the following list\n" + str(self.available_actuators))
            return 0

        requests.post(
            f"{self.address}/led_actuator_settings", json={
                "port": pin,
                "color": color,
            }
        )

    def createCircuit(self, circuit="default_circuit.json"):
        with open(circuit, "r") as file:
            circuit = json.load(file)

        for sensor_pin, sensor in circuit["sensors"].items():
            if sensor["type"] in self.available_sensors:
                # CREATION
                self.createSensor(sensor["type"], sensor_pin)

                # ADDING SETTINGS
                # provide the values for random_min and random_max if they exist
                if "random_min" in sensor and "random_max" in sensor:
                    self.editSensor(
                        sensor["type"], 
                        sensor_pin, 
                        sensor["value"], 
                        is_random=sensor["is_random"],
                        random_min= sensor["random_min"],
                        random_max= sensor["random_max"]
                        )
    
                # pass the function without those arguments otherwise (case of a Button for example)
                else:
                    self.editSensor(
                        sensor["type"], 
                        sensor_pin, 
                        sensor["value"], 
                        is_random=sensor["is_random"],
                        )

            else:
                print(f"{sensor['type']} doesn't exist, choose a sensor from the following list \n{self.available_sensors}")

        for actuator_pin, actuator in circuit["actuators"].items():
            if actuator["type"] in self.available_actuators:
                # CREATION
                self.createActuator(actuator["type"], actuator_pin)

                # EDITING SETTINGS
                if "color" in actuator:
                    self.editActuator(actuator_pin, color=actuator["color"])
                else:
                    self.editActuator(actuator_pin)


# make is so capitalization isn't needed
# add unit support
# raise errors instead of return 0


# SWAP PIN AND TYPE IN JSON FILE AND FIX THE SHIT ACCORDINGLY
