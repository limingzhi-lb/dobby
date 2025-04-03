from collections import namedtuple


MOTOR1 = namedtuple('MOTOR1', ['pin1', 'pin2', 'enable_pin']
                    )(3, 4, 2)
MOTOR2 = namedtuple('MOTOR2', ['pin1', 'pin2', 'enable_pin']
                    )(5, 6, 5)
MOTOR3 = namedtuple('MOTOR3', ['pin1', 'pin2', 'enable_pin']
                    )(8, 9, 10)
MOTOR4 = namedtuple('MOTOR4', ['pin1', 'pin2', 'enable_pin']
                    )(11, 12, 13)
MOTOR_FREQUENCY = 1000

WIFI_SSID = 'your_wifi_ssid'
WIFI_PASSWORD = 'your_wifi_password'

try:
    from config_local import *
except ImportError:
    pass
