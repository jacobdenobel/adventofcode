#include <iostream>
#include <filesystem>

#include "parser.hpp"

namespace fs = std::filesystem; 


fs::path get_data_directory()
{
    auto data = fs::path("2020") / fs::path("data");
    fs::path root;
    for (const auto& e : fs::current_path())
    {
	root /= e;
	if (fs::exists(root / data))
	{
	    data = root / data;
	    break;
	}
    }
    return data;
}



int main()
{
    std::ifstream input_file(get_data_directory() / "8.txt");
    auto parser = parser::Parser(input_file);
    auto permutations = parser.permute();
    for (auto parser: permutations)
    {
	parser.run();
	// std::cout << parser << std::endl;
    }


    // parser.run();
    // std::cout << parser;
}
