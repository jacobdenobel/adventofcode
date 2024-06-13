#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

bool is_valid(int a, int b, int c) {
    return (a + b) > c && (a + c) > b && (b + c) > a;
}

int main() {
    std::ifstream file("data/3");
    std::string line1, line2, line3;

    int a, b, c;
    int A[3], B[3], C[3];
    int count = 0, count2 = 0;
    while (std::getline(file, line1) && std::getline(file, line2) &&
           std::getline(file, line3)) {
        int i = 0;
        for (auto& line : {line1, line2, line3}) {
            std::stringstream ss(line);
            ss >> a >> b >> c;
            count += (int)is_valid(a, b, c);
            A[i] = a;
            B[i] = b;
            C[i++] = c;
        }
        for (auto& X : {A, B, C}) {
            count2 += is_valid(X[0], X[1], X[2]);
        }
    }

    std::cout << "Q1: " << count << '\n';
    std::cout << "Q2: " << count2 << '\n';
}
