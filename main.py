"""
author: Maxim Van den Abeele
06/05/2023
"""
import time
from models.ginco_socket import GincoSocket, Commands
from models.mqtt.client import MqttClient
from utils.logging import enable_console_log
from models.mqtt.proto_helper import ProtoHelper

def configure_socket():
    """Configure client over socket"""
    soc = GincoSocket()
    soc.connect()
    soc.start_command(Commands.CONFIGURE)
    soc.send_string("ssid")
    soc.send_string("password")
    soc.send_string("mqtt://hostname")
    print(soc.receive_response())

def use_mqtt():
    """Send mqtt commands"""
    mqtt = MqttClient("192.168.0.10", topics=[
        "ginco_bridge/status/083AF23AE64"
    ])
    helper = ProtoHelper()
    time.sleep(1)
    version = helper.requestVersion()
    print(version)
    mqtt.publish("ginco_bridge/command/083AF23AE64", version.SerializeToString())
    # mqtt.upgrade(0, '/home/siemie/Code/gincoBridge/build/gincoBridge.bin')
    # mqtt.upgrade(1, '/home/siemie/Code/switchCo/build/switch_co.bin')

if __name__ == "__main__":
    enable_console_log()
    use_mqtt()
    # configure_socket()
    while True:
        time.sleep(1)
