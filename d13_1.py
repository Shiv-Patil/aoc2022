signal = []


def read_packets(inp, packet=None, pos=1):
    packet = packet if packet else []
    while pos < len(inp):
        if inp[pos] in (",", " "):
            pass
        elif inp[pos] == "]":
            return (packet, pos) if pos < len(inp) - 1 else packet
        elif inp[pos] == "[":
            inner, pos = read_packets(inp, [], pos + 1)
            packet.append(inner)
        else:
            for n in range(pos, len(inp)):
                if not inp[n].isdigit():
                    packet.append(int(inp[pos:n]))
                    pos = n - 1
                    break
        pos += 1


def compare_packets(left, right):
    ll, lr = len(left), len(right)
    length = True if ll < lr else False if ll > lr else None
    for i in range(min(ll, lr)):
        is_left_list = isinstance(left[i], list)
        is_right_list = isinstance(right[i], list)
        if is_left_list or is_right_list:
            newl, newr = (left[i] if is_left_list else [left[i]]), (
                right[i] if is_right_list else [right[i]]
            )
            res = compare_packets(newl, newr)
            if res is not None:
                return res
        elif left[i] < right[i]:
            return True
        elif left[i] > right[i]:
            return False
    return length


index = 1
total = 0
while inp := input():
    pair = (read_packets(inp), read_packets(input()))
    input()
    total += index if compare_packets(*pair) else 0
    index += 1

print(total)
