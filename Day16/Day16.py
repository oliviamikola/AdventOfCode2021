from DayBase import DayBase, DayBaseSmall
from PacketHelper import read_literal_packet, read_operator_packet, LiteralPacket


class Day16(DayBaseSmall):
    def __init__(self):
        DayBaseSmall.__init__(self, 16, to_int=False)

        self.binary = bin(int(self.data[0], 16))[2:].zfill(len(8 * self.data))

    def part1(self):
        index, literal_packet = read_literal_packet(self.binary, 0)
        print(index)
        return literal_packet.value

    def part2(self):
        pass


day = Day16()
day.run()
