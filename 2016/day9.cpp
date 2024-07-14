#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

struct Op {
    int n_times;
    int size;

    Op(const std::string& op_s) {
        std::string data;
        std::stringstream ss(op_s);
        std::getline(ss, data, 'x');
        size = std::stoi(data);
        std::getline(ss, data, 'x');
        n_times = std::stoi(data);
    }
};

std::string decompress(const std::string& line) {
    std::string op;
    std::string decompressed;
    bool in_op = false;

    for (size_t i = 0; i < line.size(); i++) {
        auto c = line[i];
        if (c == '(') {
            op.clear();
            in_op = true;
            continue;
        }
        if (c == ')') {
            if (i == line.size() - 1) break;
            in_op = false;
            Op rep(op);
            for (int j = 0; j < rep.n_times; j++)
                decompressed += line.substr(i + 1, rep.size);
            i += rep.size;
            continue;
        }
        if (in_op)
            op += c;
        else
            decompressed += c;
    }
    return decompressed;
}


long int unpack(const std::string& string) 
{
    const auto start_marker = string.find('(');
    if (start_marker != string.npos) 
    {
        const auto end_marker = string.find(')');
        const Op op = string.substr(start_marker + 1, end_marker - 1);
        const size_t end_marker_cntrl = end_marker + op.size + 1;
        const auto remainder = string.substr(end_marker + 1, op.size);
        const auto next_part = string.substr(end_marker_cntrl);
        return start_marker + op.n_times * unpack(remainder) + unpack(next_part);
    }
    return string.size();
}

void print_length(const std::string& line)
{
    std::cout << "Q1: " << decompress(line).size() << std::endl;
    std::cout << "Q2: " << unpack(line) << std::endl;
}

int main() {
    std::array<std::string, 4> tests {
        "(3x3)XYZ",
        "X(8x2)(3x3)ABCY",
        "(27x12)(20x12)(13x14)(7x10)(1x12)A",
        "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN",
    };

    // for (const auto& c: tests)
    //     print_length(c);


    std::ifstream file("data/9");
    std::string line;

    while (std::getline(file, line)) {
        print_length(line);
    }
}
