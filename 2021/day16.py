import enum
import operator
import math 

class MessageType(enum.IntEnum):
    OPERATOR = -1
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUALS = 7

    @classmethod
    def _missing_(cls, _):
        return MessageType.OPERATOR

    def __call__(self, *args):
        return {
            MessageType.SUM: sum,
            MessageType.PRODUCT: math.prod, 
            MessageType.MINIMUM: min,
            MessageType.MAXIMUM: max, 
            MessageType.LITERAL: lambda x:x,
            MessageType.GREATER_THAN: lambda x: int(operator.gt(*x)),
            MessageType.LESS_THAN: lambda x: int(operator.lt(*x)),
            MessageType.EQUALS: lambda x: int(operator.eq(*x)),
        }[self](*args)
        

class Message:
    def __init__(self, binary):
        self.binary = binary
        self.version = int(binary[:3], 2)
        self.typeid = MessageType(int(binary[3:6], 2))

        start = 6
        self.subs = []
        
        if self.typeid is MessageType.LITERAL:
            self.packet_binary = binary[start:]
            start += len("".join(self.get_packets()))
        else:
            self.packet_binary = ""
            ii = int(binary[6], 2)
            if ii:
                ln = int(binary[7:18], 2)
                start = 18
                for _ in range(ln):
                    m = Message(binary[start:])
                    self.subs.append(m)
                    start += m.total_ln
                assert len(self.subs) == ln
            else:
                ln = int(binary[7:22], 2)
                start = 22
                tt = start + ln
                while len(binary[start:tt]) > 0:
                    m = Message(binary[start:tt])
                    self.subs.append(m)
                    start += m.total_ln
                assert start == (22 + ln)

        self.total_ln = start
        self.binary = self.binary[: self.total_ln]

    def get_packets(self, as_binary=True):
        for s in self.subs:
            yield from s.get_packets(as_binary)

        collected = ""
        for i in range(0, len(self.packet_binary), 5):
            p = self.packet_binary[i : i + 5]
            if as_binary:
                yield p
            else:
                collected += p[1:]
            if p.startswith("0"):
                if not as_binary:
                    yield int("".join(collected), 2)
                break

    def iter_versions(self):
        yield self.version
        for s in self.subs:
            yield from s.iter_versions()

    def eval(self):
        if not any(self.subs):
            return self.typeid(*self.get_packets(False))
        return self.typeid(map(lambda x:x.eval(), self.subs))
    
    def __repr__(self):
        return f"<Message {self.version} {self.typeid} {self.x}>"


def hextobin(hexd):
    return bin(int(hexd, base=16))[2:].zfill(len(hexd) * 4)


if __name__ == "__main__":
    with open("data/day16.txt") as f:
        hexd = f.read().strip()

    
    m = Message(hextobin("9C0141080250320F1802104A08"))
    # # print(sum(m.iter_versions()))
    print(m.eval())


    # m = Message(hextobin("38006F45291200"))
    # print(sum(m.iter_versions()))
    # m = Message(hextobin("8A004A801A8002F478"))
    # print(sum(m.iter_versions()))
    # m = Message(hextobin("620080001611562C8802118E34"))
    # print(sum(m.iter_versions()))
    # m = Message(hextobin("C0015000016115A2E0802F182340"))
    # print(sum(m.iter_versions()))
    # m = Message(hextobin("A0016C880162017C3686B18A3D4780"))
    # print(sum(m.iter_versions()))
    m = Message(hextobin(hexd))
    print(m.eval())
    # print(sum(m.iter_versions()))
