from dataclasses import dataclass, asdict


@dataclass
class Passport:
    byr: int = None
    iyr: int = None
    eyr: int = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None
    
    def __post_init__(self):
        if self.byr:
            self.byr = int(self.byr)
        if self.iyr:
            self.iyr = int(self.iyr)
        if self.eyr:
            self.eyr = int(self.eyr)

    @property
    def all_filled(self):
        return all(v is not None for k, v in asdict(self).items()
                   if k != 'cid')
 
    @property
    def valid(self):
        if not self.all_filled:
            return False

        if self.byr < 1920 or self.byr > 2002:
            return False

        if self.iyr < 2010 or self.iyr > 2020:
            return False

        if self.eyr < 2020 or self.eyr > 2030:
            return False
        
        height_unit = self.hgt[-2:]
        if height_unit not in ("cm", "in",):
            return False

        int_height = int(self.hgt[:-2])
        if height_unit == "cm" and (int_height < 150 or int_height > 193):
            return False

        if height_unit == "in" and (int_height < 59 or int_height > 76):
            return False    

        clr_chars = '0123456789abcdef'
        if not self.hcl.startswith("#") or len(self.hcl) != 7 or any(
                char not in clr_chars for char in self.hcl[1:]):
            return False

        if self.ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth",):
            return False

        if len(self.pid) != 9 or not all(map(str.isdigit, self.pid)):
            return False
        
        return True


if __name__ == "__main__":
    with open("data/4.txt", "r") as f:
        data = map(lambda x: x.replace("\n", " ").strip().split(),
                   f.read().split("\n\n"))
        data = map(lambda l: dict(tuple(e.split(":", 1)) for e in l), data)
        data = list(map(lambda p: Passport(**p), data))
        data_filled = filter(lambda p: p.all_filled, data)
        data_valid = filter(lambda p: p.valid, data)
        
        print("Q1", len(list(data_filled)))  
        print("Q2", len(list(data_valid)))       
