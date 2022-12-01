def main():
    with open("data/1") as f:
        max_elfs = [0, 0, 0]
        elf = 0
        for line in f:
            line = line.strip()
            if not line:
                for i, max_elf in enumerate(max_elfs):
                    if elf > max_elf:
                        max_elfs[i] = elf
                        break            
                elf = 0
                continue
            elf += int(line)

    print("Q1", max_elfs[0])
    print("Q2", sum(max_elfs))


if __name__ == "__main__":
    main()