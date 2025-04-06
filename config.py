from collections import namedtuple


MOTOR1 = namedtuple('MOTOR1', ['pin1', 'pin2', 'enable_pin']
                    )(12, 13, 25)
MOTOR2 = namedtuple('MOTOR2', ['pin1', 'pin2', 'enable_pin']
                    )(26, 14, 27)
MOTOR3 = namedtuple('MOTOR3', ['pin1', 'pin2', 'enable_pin']
                    )(17, 16, 21)
MOTOR4 = namedtuple('MOTOR4', ['pin1', 'pin2', 'enable_pin']
                    )(18, 19, 5)
MOTOR_FREQUENCY = 1000

WIFI_SSID = 'your_wifi_ssid'
WIFI_PASSWORD = 'your_wifi_password'

try:
    from local_config import *
except ImportError:
    pass
