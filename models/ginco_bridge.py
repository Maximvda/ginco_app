import logging
from models.mqtt.client import MqttClient

logger = logging.getLogger(__name__)


class GincoBridge:
    def __init__(self, mac: str, mqtt: MqttClient):
        self.mac = mac
        self.mqtt = mqtt

    def upgrade(self, path: str):
        """Upgrade the device"""
        logger.info("Upgrading %s with %s", self.mac, path)
        self.mqtt.upgrade(0, path, self.topic)

    def upgrade_dev(self, id: int, path: str):
        """Upgrade the device"""
        logger.info("Upgrading %s with %s", self.mac, path)
        self.mqtt.upgrade(id, path, self.topic)

    @property
    def topic(self):
        return f"ginco_bridge/command/{self.mac}"
