def unpack(string):
    start_marker = string.find("(")
    if start_marker != -1:
        end_marker = start_marker + string[start_marker:].find(")")
        marker = string[start_marker + 1 : end_marker]
        size, times = map(int, marker.split("x"))
        end_marker_cntrl = end_marker + 1 + size
        remainder = string[end_marker + 1 : end_marker_cntrl]
        lenght = (
            start_marker + times * unpack(remainder) + unpack(string[end_marker_cntrl:])
        )
        return lenght
    else:
        return len(string)

if __name__ == "__main__":
    tests = [
        "(3x3)XYZ",
        "X(8x2)(3x3)ABCY",
        "(27x12)(20x12)(13x14)(7x10)(1x12)A",
        "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN",
    ]

    for t in tests:
        print(t, unpack(t))

    with open("data/9") as f:
        print("Q2", unpack(f.read()))
