class LiteralPacket:
    def __init__(self, version: int, type_id: int, value: int):
        self.version: int = version
        self.type_id: int = type_id
        self.value = value
