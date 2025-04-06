import machine
import time
from motor import MotorController
from third_source.hcsr04 import HCSR04
from socket_server.server import current_socket
from socket_server.template import base_html
from hcsr import hcsr
motor_controller = None

def module_init():
    # 初始化电机控制器
    global motor_controller
    motor_controller = MotorController()

module_init()
# 自动避障和远程控制主循环
while True:
    request, conn = current_socket.listen()
    # 处理远程控制请求
    if '/forward' in request:
        motor_controller.move_forward(50)
    elif '/backward' in request:
        motor_controller.move_backward(50)
    elif '/left' in request:
        motor_controller.move_left(50)
    elif '/right' in request:
        motor_controller.move_right(50)
    elif '/turnleft' in request:
        motor_controller.turn_left(50)
    elif '/turnright' in request:
        motor_controller.turn_right(50)
    elif '/stop' in request:
        motor_controller.stop()

    way = hcsr.find_way()
    if way == 1:  # 左边有路
        motor_controller.move_left(50)
    elif way == 2:  # 右边有路
        motor_controller.move_right(50)
    elif way == 3:  # 前方无路可走
        motor_controller.stop()
    else:  # 前方有路
        motor_controller.move_forward(50)

    # 发送网页响应
    current_socket.send_response(conn, base_html)
