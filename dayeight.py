from collections import Counter
from pprint import pprint

def extract_layers(digits, w, h):
    rows = [
        digits[i:i+w] for i in range(0, len(digits), w)
    ]
    layers = [
        rows[i:i+h] for i in range(0, len(rows), h)
    ]
    return layers

def count_occurences(layers):
    return [
        Counter(''.join(layer)) for layer in layers
    ]

def part_one(data):
    layers = extract_layers(data, 25, 6)
    counted_layers = count_occurences(layers)
    min_zeros = min(counted_layers, key=lambda x:x.get('0'))
    return min_zeros.get('1') * min_zeros.get('2')

   
def part_two(data):
    layers = extract_layers(data, 25, 6)
    image = []
    for rows in zip(*layers):
        row = ''
        for digits in zip(*rows):
            if '1' in digits and '0' in digits:
                if digits.index('1') < digits.index('0'):
                    row += '#'
                else:
                    row += ' '
            elif '1' in digits:
                row += '#'
            elif '0' in digits:
                row += ' '
            else:
                row += ' '
        image.append(row)
    return image

if __name__ == '__main__':
    with open("inputdayeight.txt", 'r') as f:
        data = f.read().strip()
        answer = part_one(data)
        assert answer == 2904
        image = part_two(data)
        pprint(image)


