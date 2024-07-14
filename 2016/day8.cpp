#include <array>
#include <fstream>
#include <iostream>
#include <sstream>

constexpr int H = 6;
constexpr int W = 50;
char grid[H][W] = {};

void print_grid() {
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) std::cout << grid[i][j];
        std::cout << '\n';
    }
}

void fill_grid() {
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) grid[i][j] = 46;
}

void add_rect(const int h, const int w) {
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++) grid[i][j] = 35;
}

void rotate_row(const int x, const int b) {
    for (int i = 0; i < b; i++) {
        auto tmp = grid[x][W - 1];
        for (int j = W - 1; j >= 0; j--) grid[x][j + 1] = grid[x][j];
        grid[x][0] = tmp;
    }
}

void rotate_column(const int x, const int b) {
    for (int i = 0; i < b; i++) {
        auto tmp = grid[H - 1][x];
        for (int j = H - 1; j >= 0; j--) grid[j + 1][x] = grid[j][x];
        grid[0][x] = tmp;
    }
}

std::array<int, 3> parse(const std::string& line) {
    std::array<int, 3> res{};

    if (line.substr(0, 4) == "rect") {
        res[0] = 0;
        std::stringstream ss(line.substr(5));
        std::string c;

        for (int i = 0; i < 2; i++) {
            std::getline(ss, c, 'x');
            res[i + 1] = std::stoi(c);
        }
    } else {
        res[0] = 2 - (int)(line.substr(0, 10) == "rotate row");
        std::stringstream ss(line.substr(line.find('=') + 1));
        std::string c;
        ss >> res[1] >> c >> res[2];
    }
    return res;
}

int main() {
    fill_grid();

    std::ifstream stream("data/8");
    std::string line;

    while (std::getline(stream, line)) {
        auto [p1, p2, p3] = parse(line);
        switch (p1) {
            case 0:
                add_rect(p2, p3);
                break;
            case 1:
                rotate_row(p2, p3);
                break;
            case 2:
                rotate_column(p2, p3);
        }
    }

    int n_pixels = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) n_pixels += (int)(grid[i][j] == 35);

    std::cout << "Q1: " << n_pixels << std::endl;
    print_grid();
}
