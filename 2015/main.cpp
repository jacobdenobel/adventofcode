#include "utils.hpp"

void day1(){
    const auto input = read_file(1)[0];
    int floor = 0;
    for (size_t i =0; i < input.size(); i++){
        switch (input[i])
        {
        case '(': floor++; break;
        case ')': floor--; break;
        }
        if(floor == -1) std::cout << "index: " << (i + 1) << std::endl;
    }
    std::cout << "floor: " << floor << std::endl;
}


int compute_required_paper(const int l, const int w, const int h) {
    const int s1 = 2*l*w, s2 = 2*w*h, s3 = 2*h*l;
    const int paper = s1+s2+s3 + (std::min(std::min(s1, s2), s3) / 2);
    return paper;
}

int compute_required_ribbon(const int l, const int w, const int h) {
    const int bow = l * w * h;
    const int s1 = 2 * l + 2 * w, s2 = 2 * w + 2 * h, s3 = 2 * l + 2 * h;
    const int min_s = std::min(std::min(s1, s2), s3);
    return bow + min_s;
}


void day2(){
    const auto input = read_file(2);
    int total_paper = 0, total_ribbon = 0;
    for (const auto& wi: input){
        int i = 0;
        std::string c;
        std::array<int, 3> data;
        for (const auto& xi: wi){
            if (xi == 'x'){
                data[i++] = std::stoi(c);
                c.clear();
                continue;
            }
            c += xi;
        }
        data[i] = std::stoi(c);
        total_paper += compute_required_paper(data[0], data[1], data[2]);
        total_ribbon += compute_required_ribbon(data[0], data[1], data[2]);
    }
    std::cout << total_paper << std::endl;
    std::cout << total_ribbon << std::endl;
}

int main() {
    day2();
}