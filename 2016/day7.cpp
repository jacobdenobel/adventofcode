#include <fstream>
#include <iostream>
#include <string>
#include <vector>

bool has_abba(const std::string& s) {
    for (int i = 0; i < (int)s.size() - 3; i++)
        if (s[i] == s[i + 3] && s[i + 1] == s[i + 2] && s[i] != s[i + 1])
            return true;
    return false;
}

std::vector<std::string> has_aba(const std::string& s) {
    std::vector<std::string> res;
    for (int i = 0; i < (int)s.size() - 2; i++)
        if (s[i] == s[i + 2] && s[i] != s[i + 1]) res.push_back(s.substr(i, 2));
    return res;
}

bool has_bab(const std::string& s, const char a, const char b) {
    for (int i = 0; i < (int)s.size() - 2; i++)
        if (s[i] == b && s[i + 1] == a && s[i + 2] == b) return true;
    return false;
}

struct IP {
    std::vector<std::string> inside;
    std::vector<std::string> outside;

    IP(const std::string& addr) : inside{}, outside{} {
        std::string current = "";
        for (auto c : addr) {
            if (c == '[') {
                outside.push_back(current);
                current.clear();
                continue;
            }
            if (c == ']') {
                inside.push_back(current);
                current.clear();
                continue;
            }
            current += c;
        }
        outside.push_back(current);
    }

    bool supports_tls() const {
        bool outside_abba = false;
        for (const auto& s : outside) outside_abba |= has_abba(s);
        bool inside_abba = false;
        for (const auto& s : inside) inside_abba |= has_abba(s);
        return outside_abba && !inside_abba;
    }

    bool supports_ssl() const {
        std::vector<std::string> abas{};
        for (const auto& s : outside) {
            const auto aba = has_aba(s);
            for (const auto& ab : aba) abas.push_back(ab);
        }
        for (const auto& s : inside) {
            for (const auto& aba : abas)
                if (has_bab(s, aba[0], aba[1])) return true;
        }
        return false;
    }
};

int main() {
    std::ifstream file("data/7");
    std::string line;

    int n_tls = 0;
    int n_ssl = 0;
    while (std::getline(file, line)) {
        IP ip(line);
        n_tls += (int)ip.supports_tls();
        n_ssl += (int)ip.supports_ssl();
    }
    std::cout << "Q1: " << n_tls << std::endl;
    std::cout << "Q2: " << n_ssl << std::endl;
}
