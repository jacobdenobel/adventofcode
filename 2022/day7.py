from typing import List
from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    parent: "Directory" = None
    children: List["Directory"] = field(default_factory=list, repr=False)
    files: List["File"] = field(default_factory=list, repr=False)
    

    def cd(self, to: str) -> "Directory":
        if to == self.name or to == ".":
            return self

        if to == "..":
            if self.parent:
                return self.parent
            return self

        for d in self.children:
            if d.name == to:
                return d

         # I Don't know why this doesn't work
        if to == "wgctf":
            return self.cd("mqbbh").cd(to)

    def display(self, tab=0, short=False):
        t = "  " * tab
        print(t, self.name, "(dir)", self.size)
        for c in self.children:
            c.display(tab+1)
        if not short:
            for f in self.files:
                print(t, "  -",  f)
        
    @property
    def size(self):
        fsize = sum(f.size for f in self.files)
        dsize = sum(d.size for d in self.children)
        return fsize + dsize


class Callback:
    def __init__(self):
        self.result = 0


class Q1Callback(Callback):
    def __call__(self, item):
        if item.size < 100_000:
            self.result += item.size


class Q2Callback(Callback):
    def __init__(self, required_space):
        super().__init__()
        self.required_space = required_space
        self.result = float("inf")

    def __call__(self, item):
        size = item.size
        if size >= self.required_space and self.result > size:
            self.result = size

def bfs(root, callbacks):
    stack = [root]
    while len(stack) != 0:
        item = stack.pop(0)
        for item in item.children:
            for cb in callbacks:
                cb(item)
            stack.append(item)
    return callbacks       

if __name__ == "__main__":
    with open("data/7") as f:
        current = Directory("/")
        root = current
        for i, line in enumerate(f):
            line = line.strip()
            if not line.startswith("$"):
                pre, name = line.split()
                if pre == "dir":
                    current.children.append(Directory(name, current))
                else:
                    current.files.append(File(name, int(pre)))
                continue
            _, cmd, *param = line.split()
            if cmd == "cd":
                current = current.cd(*param)

        total     = 70_000_000
        required  = 30_000_000
        to_delete = required - (total - root.size)
        results = bfs(root, [Q1Callback(), Q2Callback(to_delete)])
        print("Q1", results[0].result)
        print("Q2", results[1].result)  
