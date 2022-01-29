# Camera Mask Recognition
## _A little jab at CounterFit Module and Face/Mask detection_

Camera Mask Recognition comes as a prototype to an automation-based approach to Covid-19 safety in enclosed spaces.
Through facial recognition and image processing the program recognizes wether the subject is wearing a mask or not, and - if desired - also takes into account the body temperature of said subject.
If the person comforms to the configured safety standards then a relay is activated and said person has access to the building, otherwise a warning is issued. 


## Features

- **Easy to setup**: scroll down to the Setup section for more information.
- **Accurate**: 90%+ accurate mask readings are the norm in regular conditions. False positives and False negatives are the exception, not the rule.
- **Clear and concise output**: 3 LED's of different colors convey clear messages.
- **Flexible**: Mask detection accuracy, the critical body temperature and whether to use temperature readings or not could all be set up.
- **Under Development**: This project is still under developement, so there are more features to come!

## Installing and Running the app:

- Clone *Camera-Mask-Module* repository:

```sh
git clone https://github.com/AChillFeeder/Camera-Mask-Recognition.git
```

- Move into Camera-Mask-Module directory and install requirements
```sh
cd Camera-Mask-Module
pip install -f requirements.txt
```
---
- To run the program, first start Counterfit
```sh
Counterfit
```
- This will open a new browser window with the CounterFit interface.
- Create the following components on their respective pins.
    - *LED* on pins **1, 2 and 3**
    - *RELAY* on pin **4**
    - *TEMPERATURE* SENSOR on pin **0**
    - *BUTTON* on pin **10**
    
    ![Counterfit Setup Screenshot](https://github.com/AChillFeeder/Camera-Mask-Recognition/blob/main/Assets/counterfit_setup_screenshot.png)



- On a separate CMD window, run the program
```sh
python main.py
```

## Credits:
Big thanks to:
- jimbobbennett (https://github.com/jimbobbennett) for Counterfit (https://github.com/CounterFit-IoT/CounterFit)
- chandrikadeb7 (https://github.com/chandrikadeb7) for Face Mask Detection (https://github.com/chandrikadeb7/Face-Mask-Detection)
