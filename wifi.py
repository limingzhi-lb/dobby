import network
import config


# 连接到WiFi
def connect_wifi():
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print('Connecting to network...')
        station.active(True)
        station.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not station.isconnected():
            pass
    print('Network config:', station.ifconfig())
