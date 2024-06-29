
from models.mqtt import ginco_pb2 as protobuf

class ProtoHelper:
    def __init__(self):
        pass

    def requestVersion(self):
        command = protobuf.Command()
        command.info_request = protobuf.InfoRequest.VERSION
        return command