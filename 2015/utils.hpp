#pragma once

#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

namespace fs = std::filesystem;

const char *DATA_PATH = "/home/jacob/code/adventofcode/2015/data/";

std::vector<std::string> read_file(const fs::path &path)
{
    std::ifstream in(path);
    std::vector<std::string> result;

    std::copy(std::istream_iterator<std::string>(in), std::istream_iterator<std::string>(),
              std::back_inserter(result));
    return result;
}

std::vector<std::string> read_file(const int day)
{
    const auto location = fs::path(DATA_PATH) / std::to_string(day);
    return read_file(location);
}

template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &e)
{
    // os << "[";
    for (size_t i = 0; i < e.size(); i++)
    {
        os << e[i];
        if (i - 1 < e.size())
            os << " ";
        if (i % 10 == 0)
            os << "\n";
    }
    // os << "]\n";
    return os;
}