def read_signal(inp, packet=None, pos=1):
    packet = packet if packet else []
    while pos < len(inp):
        if inp[pos] in (",", " "):
            pass
        elif inp[pos] == "]":
            return (packet, pos) if pos < len(inp) - 1 else packet
        elif inp[pos] == "[":
            inner, pos = read_signal(inp, [], pos + 1)
            packet.append(inner)
        else:
            for n in range(pos, len(inp)):
                if not inp[n].isdigit():
                    packet.append(int(inp[pos:n]))
                    pos = n - 1
                    break
        pos += 1


signal = [] = []
while inp := input():
    signal.append(read_signal(inp))
    signal.append(read_signal(input()))
    input()

signal.append([[2]])
signal.append([[6]])


def key(li):
    flattened = []

    def _key(li):
        for ele in li:
            if isinstance(ele, list):
                _key(ele) if ele else flattened.append(0)
            else:
                flattened.append(ele)

    _key(li)
    return flattened


signal.sort(key=key)
decoder_key = 1

for i in range(len(signal)):
    if signal[i] == [[2]] or signal[i] == [[6]]:
        decoder_key *= i + 1

print(decoder_key)
