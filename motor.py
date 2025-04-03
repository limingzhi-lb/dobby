import machine
import config

class Motor(object):
    def __init__(self, enable_pin, in1_pin, in2_pin, frequency):
        self.enable = machine.PWM(machine.Pin(enable_pin))
        self.in1 = machine.Pin(in1_pin, machine.Pin.OUT)
        self.in2 = machine.Pin(in2_pin, machine.Pin.OUT)
        self.enable.freq(frequency)

    def set_speed(self, speed):
        if speed > 0:
            self.in1.value(1)
            self.in2.value(0)
            self.enable.duty(int(speed * 1023 / 100))
        elif speed < 0:
            self.in1.value(0)
            self.in2.value(1)
            self.enable.duty(int(-speed * 1023 / 100))
        else:
            self.in1.value(0)
            self.in2.value(0)
            self.enable.duty(0)


class MotorController(object):
    def __init__(self):
        # 电机引脚定义
        self.motor1 = Motor(enable_pin=config.MOTOR1.enable_pin,
                            in1_pin=config.MOTOR1.pin1, in2_pin=config.MOTOR1.pin2,
                            frequency=config.MOTOR_FREQUENCY)
        self.motor2 = Motor(enable_pin=config.MOTOR2.enable_pin,
                            in1_pin=config.MOTOR2.pin1, in2_pin=config.MOTOR2.pin2,
                            frequency=config.MOTOR_FREQUENCY)
        self.motor3 = Motor(enable_pin=config.MOTOR3.enable_pin,
                            in1_pin=config.MOTOR3.pin1, in2_pin=config.MOTOR3.pin2,
                            frequency=config.MOTOR_FREQUENCY)
        self.motor4 = Motor(enable_pin=config.MOTOR4.enable_pin,
                            in1_pin=config.MOTOR4.pin1, in2_pin=config.MOTOR4.pin2,
                            frequency=config.MOTOR_FREQUENCY)

    def move_forward(self, speed):
        self.motor1.set_speed(speed)
        self.motor2.set_speed(speed)
        self.motor3.set_speed(speed)
        self.motor4.set_speed(speed)

    def move_backward(self, speed):
        self.motor1.set_speed(-speed)
        self.motor2.set_speed(-speed)
        self.motor3.set_speed(-speed)
        self.motor4.set_speed(-speed)

    def move_left(self, speed):
        self.motor1.set_speed(-speed)
        self.motor2.set_speed(speed)
        self.motor3.set_speed(speed)
        self.motor4.set_speed(-speed)

    def move_right(self, speed):
        self.motor1.set_speed(speed)
        self.motor2.set_speed(-speed)
        self.motor3.set_speed(-speed)
        self.motor4.set_speed(speed)

    def turn_left(self, speed):
        self.motor1.set_speed(-speed)
        self.motor2.set_speed(speed)
        self.motor3.set_speed(-speed)
        self.motor4.set_speed(speed)

    def turn_right(self, speed):
        self.motor1.set_speed(speed)
        self.motor2.set_speed(-speed)
        self.motor3.set_speed(speed)
        self.motor4.set_speed(-speed)

    def stop(self):
        self.move_forward(0)
