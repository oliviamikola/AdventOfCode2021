from typing import Tuple


class LiteralPacket:
    def __init__(self, version: int, type_id: int, value: int):
        self.version: int = version
        self.type_id: int = type_id
        self.value = value


def read_literal_packet(packet: str, start_index: int) -> Tuple[int, LiteralPacket]:
    packet_version = int(packet[start_index: start_index + 3], 2)
    packet_type_id = int(packet[start_index + 3: start_index + 6], 2)

    binary_value = ""
    last_bits = False
    current_index = start_index + 6
    while not last_bits:
        bit_header = int(packet[current_index])
        binary_value += packet[current_index + 1: current_index + 5]

        current_index += 5
        last_bits = (bit_header == 0)

    packet_value = int(binary_value, 2)

    return current_index, LiteralPacket(packet_version, packet_type_id, packet_value)


def read_operator_packet(packet: str, start_index: int):
    pass
