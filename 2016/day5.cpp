#include <openssl/evp.h>
#include <openssl/md5.h>

#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

unsigned char result[MD5_DIGEST_LENGTH];

std::string hash_to_string(const std::string& target) {
    EVP_Q_digest(NULL, "MD5", NULL, target.c_str(), target.size(), result,
                 NULL);

    std::ostringstream oss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        oss << std::setw(2) << std::setfill('0') << std::hex
            << static_cast<int>(result[i]);
    }
    return oss.str();
}

int main() {
    std::string tgt = "00000";
    std::string room_id = "abbhdwsy";
    std::string pwd1;
    std::string pwd2 = "xxxxxxxx";
    std::vector<int> pos = {0, 1, 2, 3, 4, 5, 6, 7};

    int i = 0;
    while (!pos.empty()) {
        std::string target = room_id + std::to_string(i++);
        std::string s = hash_to_string(target);
        auto first = s.substr(0, 5);
        if (first == tgt) {
            std::cout << first << " ~ " << (first == tgt) << " : " << s
                      << " > ";
            pwd1 += s[5];

            int index = (int)(s[5]) - '0';
            std::cout << "index: " << index << '\n';
            if (std::find(pos.begin(), pos.end(), index) != pos.end()) {
                pwd2[index] = s[6];
                pos.erase(std::remove(pos.begin(), pos.end(), index),
                          pos.end());
            }
        }
    }
    pwd1.resize(8);
    std::cout << "Q1: " << pwd1 << std::endl;
    std::cout << "Q2: " << pwd2 << std::endl;
}
