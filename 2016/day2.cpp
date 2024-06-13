#include <array>
#include <fstream>
#include <iostream>
#include <string>

int KEYPAD[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

char KEYPAD2[5][5] = {
    {0, 0, 49, 0, 0},   {0, 50, 51, 52, 0}, {53, 54, 55, 56, 57},
    {0, 65, 66, 67, 0}, {0, 0, 68, 0, 0},
};

int x, y;
int x2, y2;

void try_move_y2(int new_y) {
    new_y = std::min(std::max(0, new_y), 4);
    if (KEYPAD2[new_y][x2]) y2 = new_y;
}

void try_move_x2(int new_x) {
    new_x = std::min(std::max(0, new_x), 4);
    if (KEYPAD2[y2][new_x]) x2 = new_x;
}

void move(char c) {
    switch (c) {
        case 'U':
            y--;
            try_move_y2(y2 - 1);
            break;
        case 'L':
            x--;
            try_move_x2(x2 - 1);
            break;
        case 'D':
            try_move_y2(y2 + 1);
            y++;
            break;
        case 'R':
            try_move_x2(x2 + 1);
            x++;
            break;
    }
    x = std::min(std::max(0, x), 2);
    y = std::min(std::max(0, y), 2);
}

int main() {
    std::ifstream file("data/2");
    std::string line;

    x = 1, y = 1;
    x2 = 0, y2 = 2;

    while (std::getline(file, line)) {
        for (char c : line) move(c);

        //        std::cout << x << "," << y << ": " << KEYPAD[y][x] << '\n';
        std::cout << x2 << "," << y2 << ": " << KEYPAD2[y2][x2] << '\n';
    }
}
