"""
author: Maxim Van den Abeele
06/05/2023
"""
import time
from models.ginco_socket import GincoSocket, Commands
from models.mqtt.client import MqttClient
from utils.logging import enable_console_log

def configure_socket():
    """Configure client over socket"""
    soc = GincoSocket()
    soc.connect()
    soc.start_command(Commands.CONFIGURE)
    soc.send_string("ssid")
    soc.send_string("ssid_pass")
    soc.send_string("mqtt://hostname")
    print(soc.receive_response())

def use_mqtt():
    """Send mqtt commands"""
    mqtt = MqttClient("mqtt_url", topics=[
        "ginco_bridge/status"
    ])
    mqtt.upgrade(0, '/path_to_bin_file/gincoBridge.bin')

if __name__ == "__main__":
    enable_console_log()
    use_mqtt()
    while True:
        time.sleep(1)
