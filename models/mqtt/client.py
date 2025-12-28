"""
author: Maxim Van den Abeele
date: 19/04/2023
"""
import logging
import os

import paho.mqtt.client as mqtt
from google.protobuf.internal.decoder import _DecodeVarint32  # pylint: disable=W0611
from google.protobuf.internal.encoder import _VarintBytes

from utils.safe_executor import SafeExecutor
from models.mqtt import ginco_pb2 as protobuf

# pylint: disable=E1101


class MqttClient(mqtt.Client):
    """A client to interface with the current protobuf

    cb_MAC_ADDRESS : callable
    Callback function for decoded protobuf messages:

    - ``topic``: topic parameter (`string`).
    - ``message``: depending on topic it's a different protobuf message (`protobuf message`).

    cb_message : callable
    Callback function for decoded protobuf messages:

    - ``topic``: topic parameter (`string`).
    - ``message``: received message on the defined topic

    cb_connect : callable
    Callback function when client gets connect to mqtt server

    cb_disconnect : callable
    Callback function when client gets disconnected from mqtt server

    cb_subscribe : callable
    Callback function when client subscribes to defined topic

    - ``mid``: integer indicating your subscription number.

    cb_unsubscribe : callable
    Callback function when client unsubscribed to defined topic

    - ``mid``: integer indicating your subscription number.

    """

    # All different protobuf variables
    _command = protobuf.Command()  # pylint: disable=E1101
    _request = protobuf.Command()  # pylint: disable=E1101

    def __init__(self, url, *args, user=None, password=None, port=1883, topics=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger("Mqtt client")
        self._url = url
        # Set password and connect the loop
        try:
            self.username_pw_set(user, password=password)
            self.connect_async(url, port)
            self.loop_start()
            self._logger.info("Mqtt loop started")
        except TimeoutError:
            self._logger.error("Failed to connect to: %s", url, exc_info=1)
            raise

        self._topics = []
        if not topics is None:
            self._topics.extend(topics)

        # Setting up threadpool executer to process incomming messages
        self._executor = SafeExecutor(max_workers=16)

        # Attaching callbacks
        self.on_connect = self.__on_connect
        self.on_disconnect = self.__on_disconnect
        self.on_subscribe = self.__on_subscribe
        self.on_unsubscribe = self.__on_unsubscribe
        self.on_message = self.__on_message

        self.cb_connect = self.__cb_connect
        self.cb_disconnect = self.__cb_disconnect
        self.cb_subscribe = self.__cb_subscribe
        self.cb_unsubscribe = self.__cb_unsubscribe
        self.cb_message = self.__cb_message

    def __on_connect(self, *_args):
        """Callback function when mqtt client gets connected

        Args:
            client (Mqtt): instance of this class
            userdata (_type_): _description_
            flags (_type_): _description_
            rc (_type_): _description_
        """
        self._logger.info("Connected to: %s", self._url)
        self._executor.submit('cb connected', self.cb_connect)
        for topic in self._topics:
            _, mid = self.subscribe(f"{topic}")

    def __on_disconnect(self, *_args):
        """Called when client disconnects

        Args:
            client (_type_): _description_
            userdata (_type_): _description_
            rc (_type_): _description_
        """
        self._logger.warning("Disconnected...")
        self._executor.submit('cb disconnected', self.cb_disconnect)

    def __on_subscribe(self, _client, _userdata, mid, _qos):
        """Called when subscribe succeeded

        Args:
            _client (_type_): _description_
            _userdata (_type_): _description_
            mid (int): Used to check if your subscribe succeeded
            _qos (_type_): _description_
        """
        self._executor.submit('cb subscribed', self.cb_subscribe, mid)

    def __on_unsubscribe(self, _client, _userdata, mid):
        """Called when unsubscribed from certain topic

        Args:
            _client (_type_): _description_
            _userdata (_type_): _description_
            mid (_type_): _description_
        """
        self._executor.submit('cb unsubscribed', self.cb_unsubscribe, mid)

    def upgrade(self, device_id: int, file: str, topic: str):
        """Upgrade command for device

        Args:
            device_id (int): Identifier of module to upgrade
            file (str): String with path for bin file
        """
        self._request.upgrade.device_id = device_id
        self._request.upgrade.image_size = int(os.path.getsize(file))  # in bytes
        with open(file, 'rb') as bin_file:
            data = bin_file.read()
        self._send_upgrade(self._request, data, topic)
        self._request.ClearField('upgrade')

    def __on_message(self, _client, _userdata, message):
        """Process and queue incomming messages

        Args:
            _Client (_type_): _description_
            _userdata (_type_): _description_
            message (encoded message): _description_
        """
        self._executor.submit(
            'cb message', self.cb_message, *[message.topic, message.payload]
        )

        self._executor.submit('decode message', self._decode_message, message)

    def _decode_message(self, message, **_kwargs):
        # Extract mac and topic
        (_base, topic) = message.topic.split("/")[-2:]
        payload = message.payload
        self._logger.info("received topic %s, with payload %s", topic, payload)
        message = protobuf.InfoMessage()
        message.ParseFromString(payload)
        print(message)
        print(message.version)

    def _send_command(self, command, topic="ginco_bridge/command"):
        self.publish(topic, command.SerializeToString(), qos=0, retain=False)

    def _send_upgrade(self, command, data, topic="ginco_bridge/command"):
        encoded_command = _VarintBytes(command.ByteSize()) + command.SerializeToString()
        encoded_command += data
        self.publish(topic, encoded_command, qos=1, retain=False)

    @property
    def cb_connect(self):
        """Callback function which is called on connection of client

        Returns:
            callable: No arguments
        """
        return self._cb_connect

    @cb_connect.setter
    def cb_connect(self, callback):
        self._cb_connect = callback

    def __cb_connect(self):
        pass

    @property
    def cb_disconnect(self):
        """Callback function which is called on disconnection of client

        Returns:
            callable: No arguments
        """
        return self._cb_disconnect

    @cb_disconnect.setter
    def cb_disconnect(self, callback):
        self._cb_disconnect = callback

    def __cb_disconnect(self):
        pass

    @property
    def cb_subscribe(self):
        """Callback function which is called on subscription of a topic

        Returns:
            callable: Handle subscription. Callable with arugments, mid
        """
        return self._cb_subscribe

    @cb_subscribe.setter
    def cb_subscribe(self, callback):
        self._cb_subscribe = callback

    def __cb_subscribe(self, mid):
        pass

    @property
    def cb_unsubscribe(self):
        """Callback function which is called on unsubscription of a topic

        Returns:
            callable: Handle unsubscription. Callable with arugments, mid
        """
        return self._cb_unsubscribe

    @cb_unsubscribe.setter
    def cb_unsubscribe(self, callback):
        self._cb_unsubscribe = callback

    def __cb_unsubscribe(self, mid):
        pass

    @property
    def cb_message(self):
        """Callback function which is called each time a message is received

        Returns:
            callable: Handle mqtt messages. Callable with arugments, topic and message
        """
        return self._cb_message

    @cb_message.setter
    def cb_message(self, callback):
        self._cb_message = callback

    def __cb_message(self, topic, message):
        pass

    def disable_logs(self):
        """Disable all the loggers of this class"""
        logging.getLogger("Mqtt error").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Status").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Debug").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Out").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Out modbus").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Long").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Short").setLevel(logging.CRITICAL + 1)
        logging.getLogger("Event").setLevel(logging.CRITICAL + 1)

    def __del__(self):
        self.loop_stop()
        del self._executor
