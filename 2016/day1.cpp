#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

constexpr int MAX_G = 1000;
constexpr int CENTER = MAX_G / 2;
std::array<std::array<int, MAX_G>, MAX_G> grid{0};

char turn(char new_dir, const char turn) {
    if (turn == 'R')
        new_dir++;
    else
        new_dir--;

    if (new_dir == 4) new_dir = 0;
    if (new_dir == -1) new_dir = 3;
    return new_dir;
}

int sign(int x) { return (x > 0) - (x < 0); }

int fill_row(const int row_id, int index, const int n) {
    for (int i = 0; i < abs(n); i++) {
        int& gv = grid[row_id + CENTER][index + CENTER];
        if (gv) return index;
        gv++;
        index += sign(n);
    }
    return 0;
}

int fill_column(const int col_id, int index, const int n) {
    for (int i = 0; i < abs(n); i++) {
        int& gv = grid[index + CENTER][col_id + CENTER];
        if (gv) return index;
        gv++;
        index += sign(n);
    }
    return 0;
}
char format(int e) {
    if (e) return '#';
    return '.';
}

void print_grid() {
    for (int i = 0; i < MAX_G; i++) {
        for (int j = 0; j < MAX_G; j++) std::cout << format(grid[i][j]);
        std::cout << '\n';
    }
    std::cout << std::endl;
}

int main() {
    std::ifstream file("data/1");
    std::string line;

    char dir;
    int n;
    char ldir = 0;  // 0 North, 1 East, 2 South, 3 West
    int x = 0, y = 0;
    int first_x = 0, first_y = 0;

    while (std::getline(file, line, ',')) {
        std::stringstream ss(line);

        ss >> dir >> n;
        ldir = turn(ldir, dir);

        int found_x = 0, found_y = 0;

        switch (ldir) {
            case 0:
                found_y = fill_column(x, y, n);
                y += n;
                break;
            case 1:
                found_x = fill_row(y, x, n);
                x += n;
                break;
            case 2:
                found_y = fill_column(x, y, -n);
                y -= n;
                break;
            case 3:
                found_x = fill_row(y, x, -n);
                x -= n;
                break;
        }

        if (first_x == 0 && first_y == 0) {
            if (found_x) {
                first_x = found_x;
                first_y = y;
            }

            if (found_y) {
                first_y = found_y;
                first_x = x;
            }
        }
    }
    std::cout << "Q1: " << abs(x) + abs(y) << "\n";
    std::cout << "Q2: " << abs(first_x) + abs(first_y) << "\n";
}
