
def binary_part(code: str, lower: int, upper: int, upper_code: str) -> int:
    for c in code:
        delta = ((upper + 1) - lower) // 2
        if c == upper_code:
            lower += delta
        else:
            upper -= delta
    index = upper if c == upper_code else lower
    return index

def get_seat_id(code: str) -> int:
    row = binary_part(code[:7], 0, 127, "B")
    col = binary_part(code[7:], 0, 7, "R")
    seat_id = row * 8 + col
    return seat_id


if __name__ == "__main__":
    with open("data/5.txt", "r") as f:
        all_ids = [get_seat_id(l.strip()) for l in f]
        max_id = max(all_ids)
        min_id = min(all_ids)
        id_map = set(range(min_id, max_id))
        print("Q1", max_id)
        print("Q2", (id_map - set(all_ids)).pop())
    

