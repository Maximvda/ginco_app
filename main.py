"""
author: Maxim Van den Abeele
06/05/2023
"""
import time
from models.ginco_socket import GincoSocket, Commands
from models.mqtt.client import MqttClient
from utils.logging import enable_console_log
from models.ginco_bridge import GincoBridge


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
    bridge = GincoBridge("083AF23AE643", mqtt)
    # helper = ProtoHelper()
    time.sleep(1)
    # version = helper.requestVersion()
    # print(version)
    # mqtt.publish("ginco_bridge/command/083AF23AE64", version.SerializeToString())
    # bridge.upgrade('/Users/siemie/code/other/ginco_bridge/_build_debug/ginco_bridge.bin')
    bridge.upgrade_dev(2, '/Users/siemie/code/other/ginco_switch/_build_debug/ginco_switch.bin')


if __name__ == "__main__":
    enable_console_log()
    use_mqtt()
    # configure_socket()
    while True:
        time.sleep(1)
