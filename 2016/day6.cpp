#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>

constexpr int N = 8;

template <typename K>
struct Counter {
    std::map<K, size_t> map;

    void update(const K k) {
        if (map.find(k) == map.end()) map[k] = 0;
        map[k]++;
    }

    K most_common() const {
        size_t max_v = 0;
        K max_k;
        for (const auto& [k, v] : map) {
            if (v > max_v) {
                max_v = v;
                max_k = k;
            }
        }
        return max_k;
    }

    K least_common() const {
        size_t min_v = -1;
        K min_k;
        for (const auto& [k, v] : map) {
            if (v < min_v) {
                min_v = v;
                min_k = k;
            }
        }
        return min_k;
    }
};

int main() {
    std::ifstream file("data/6");
    std::string line;

    std::array<Counter<char>, N> counters{};

    while (std::getline(file, line)) {
        for (int i = 0; i < N; i++) counters[i].update(line[i]);
    }

    std::cout << "Q1: ";
    for (int i = 0; i < N; i++) std::cout << counters[i].most_common();
    std::cout << std::endl;
    std::cout << "Q2: ";
    for (int i = 0; i < N; i++) std::cout << counters[i].least_common();
    std::cout << std::endl;
}
