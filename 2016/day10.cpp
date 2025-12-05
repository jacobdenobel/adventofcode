#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int iMIN = INT32_MIN;
int iMAX = INT32_MAX;

struct Bot
{
    int *low = &iMIN;
    int *high = &iMAX;

    void set_value(int *value)
    {
        if (value == &iMIN || value == &iMAX)
            return;

        // std::cout << *value << " " << *low << " " << *high << std::endl;

        if (low == &iMIN && high == &iMAX)
        {
            low = value;
        }
        else if (low == &iMIN)
        {
            if (*value > *high)
            {
                low = high;
                high = value;
            }
            else
            {
                low = value;
            }
        }
        else if (high == &iMAX)
        {

            if (*value < *low)
            {
                high = low;
                low = value;
            }
            else
            {
                high = value;
            }
        }
        else
        {
            if (*value < *high)
                low = value;
            else
                high = value;
        }
        // std::cout << *value << " " << *low << " " << *high << std::endl;
    }
};

std::vector<std::string> get_words(const std::string &line)
{

    std::stringstream ss(line);
    std::string buf;
    std::vector<std::string> words;
    while (ss >> buf)
        words.push_back(buf);
    return words;
}

template <typename T>
T &get_idx(const int idx, std::vector<T> &vec)
{

    if (vec.size() < idx)
        vec.resize(idx + 1);
    return vec[idx];
}

void display(const std::vector<Bot> &bots, const std::vector<int *> &outputs)
{
    std::cout << "bots:\n";
    int i = 0;
    for (const auto &bot : bots)
        std::cout << i++ << " " << *bot.low << " " << *bot.high << std::endl;
    std::cout << "outputs:\n";
    for (const auto x : outputs)
        if(x != nullptr)
            std::cout << *x << ' ';
    std::cout << '\n';
}

void print(const std::vector<int> &values)
{
    for (const auto &x : values)
        std::cout << &x << "= " << x << std::endl;
    std::cout << '\n';
}

int main()
{

    std::ifstream file("data/10");
    std::string line;
    std::vector<Bot> bots;
    std::vector<int> values;
    std::vector<int *> outputs;
    values.reserve(10000);

    while (std::getline(file, line))
    {
        const auto words = get_words(line);

        std::cout << line << std::endl;
        if (words[0] == "value")
        {
            values.push_back(std::stoi(words[1]));
            const int bot_id = std::stoi(words.back());
            int *v_ptr = values.data() + values.size() - 1;
            get_idx(bot_id, bots).set_value(v_ptr);
        }
        else if (words[0] == "bot")
        {
            const int bot_id = std::stoi(words[1]);
            const bool low_to_bot = words[5] == "bot";
            const int low_to_idx = std::stoi(words[6]);
            const bool high_to_bot = words[10] == "bot";
            const int high_to_idx = std::stoi(words[11]);

            if (low_to_bot)
            {
                get_idx(low_to_idx, bots).set_value(get_idx(bot_id, bots).low);
            }
            else
            {
                get_idx(low_to_idx, outputs) = get_idx(bot_id, bots).low;
                // std::cout << *outputs[1];
            }

            if (high_to_bot)
            {
                get_idx(high_to_idx, bots).set_value(get_idx(bot_id, bots).high);
            }
            else
            {
                get_idx(high_to_idx, outputs) = get_idx(bot_id, bots).high;
            }
        }
        display(bots, outputs);
    }

    std::cout << '\n';
}
