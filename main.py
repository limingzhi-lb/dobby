import machine
import time
import socket
from motor import MotorController
from wifi import connect_wifi


def module_init():
    # 初始化电机控制器
    global motor_controller
    motor_controller = MotorController()
    connect_wifi()

# 舵机引脚定义
servo = machine.PWM(machine.Pin(14), freq=50)

# 超声波引脚定义
trigger = machine.Pin(15, machine.Pin.OUT)
echo = machine.Pin(16, machine.Pin.IN)



# 定义超声波测距函数
def get_distance():
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.0343 / 2
    return distance

# 定义舵机控制函数
def set_servo_angle(angle):
    duty = int((angle / 180) * 102 + 26)
    servo.duty(duty)

# 定义网页
html = """<!DOCTYPE html>
<html>
<head> <title>ESP32 Web Server</title> </head>
<body>
    <h1>ESP32 Web Server</h1>
    <button onclick="forward()">Forward</button>
    <button onclick="backward()">Backward</button>
    <button onclick="left()">Left</button>
    <button onclick="right()">Right</button>
    <button onclick="turnLeft()">Turn Left</button>
    <button onclick="turnRight()">Turn Right</button>
    <button onclick="stop()">Stop</button>
    <script>
        function forward() {
            fetch('/forward');
        }
        function backward() {
            fetch('/backward');
        }
        function left() {
            fetch('/left');
        }
        function right() {
            fetch('/right');
        }
        function turnLeft() {
            fetch('/turnleft');
        }
        function turnRight() {
            fetch('/turnright');
        }
        function stop() {
            fetch('/stop');
        }
    </script>
</body>
</html>
"""

# 创建socket服务器
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# 自动避障和远程控制主循环
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    # 处理远程控制请求
    if '/forward' in request:
        move_forward(50)
    elif '/backward' in request:
        move_backward(50)
    elif '/left' in request:
        move_left(50)
    elif '/right' in request:
        move_right(50)
    elif '/turnleft' in request:
        turn_left(50)
    elif '/turnright' in request:
        turn_right(50)
    elif '/stop' in request:
        stop()

    # 自动避障
    set_servo_angle(90)
    time.sleep(0.5)
    distance = get_distance()
    if distance < 20:
        stop()
        turn_right(50)
        time.sleep(1)

    # 发送网页响应
    response = html
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
