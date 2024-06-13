#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

struct Room {
    std::string name;
    std::string sector;
    std::string hash;
    std::string true_hash;

    int sector_id() const { return std::stoi(sector); }

    std::string true_name() const {
        int shift = sector_id();
        std::string true_name;

        for (char c : name) {
            char k = c;
            for (int i = 0; i < shift; i++) {
                if (++k > 'z') k = 'a';
            }
            true_name += k;
        }
        true_name += (char)0;
        return true_name;
    }

    void compute_true_hash() {
        std::map<char, int> counter;

        for (char c : name) {
            if (counter.find(c) != counter.end())
                counter[c]++;
            else
                counter[c] = 1;
        }

        std::map<int, std::string> order;
        std::vector<int> counts;

        for (auto [key, value] : counter) {
            if (order.find(value) != order.end()) {
                order[value] += key;
                std::sort(order[value].begin(), order[value].end());
                continue;
            }
            order[value] = key;
            counts.push_back(value);
        }

        std::sort(counts.begin(), counts.end(), std::greater<>());

        for (int i = 0; i < 5; i++) true_hash += order[counts[i]];
        true_hash.resize(5);
    }
    bool is_real() const { return true_hash == hash; };
};

int main() {
    std::ifstream file("data/4");
    std::string line;

    int sector_sum = 0, north_pole_sector;
    while (std::getline(file, line)) {
        Room room;

        int part = 0;
        for (int i = 0; i < line.size() - 1; i++) {
            if (line[i] == '-') continue;
            if (line[i] == ']') break;
            if (line[i] == '[') {
                part++;
                continue;
            }
            if (std::isdigit(line[i])) {
                room.sector += line[i];
                continue;
            }
            if (!part) {
                room.name += line[i];
                continue;
            }
            room.hash += line[i];
        }
        room.compute_true_hash();
        if (room.is_real()) sector_sum += room.sector_id();
        if (room.true_name()[0] == 'n') {
            north_pole_sector = room.sector_id();
            //    std::cout << room.true_name();
        };
    }
    std::cout << "Q1:" << sector_sum << std::endl;
    std::cout << "Q2:" << north_pole_sector << std::endl;
}
