#pragma once

#include <ostream>
#include <set>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>


namespace parser
{
    enum instruction_type
    {
        nop,
        acc,
        jmp
    };

    inline instruction_type get_instruction_type(const std::string& t)
    {
        if (t == "nop") return nop;
        if (t == "jmp") return jmp;
        if (t == "acc") return acc;
        throw;
    }

    inline std::ostream& operator<<(std::ostream& os, const instruction_type& t)
    {
        const char* types[3] = {"nop", "acc", "jmp"};
        return os << types[t];
    }

    struct InstructionState
    {
        int current_index;
        int accumulator;

        InstructionState() : current_index(0), accumulator(0) { }

        friend std::ostream& operator<<(std::ostream& os, const InstructionState& obj)
        {
            return os
                << "current_index: " << obj.current_index
                << " accumulator: " << obj.accumulator;
        }
    };


    struct Instruction
    {
        instruction_type type;
        int value;

        Instruction(const std::string& str)
        {
            std::istringstream stream(str);
            std::string t;
            stream >> t;
            stream >> value;
            type = get_instruction_type(t);
        }

        friend std::ostream& operator<<(std::ostream& os, const Instruction& obj)
        {
            return os
                << "type: " << obj.type
                << " value: " << obj.value;
        }

        void advance(InstructionState& state) const
        {
            if (type == jmp)
            {
                state.current_index += value;
                return;
            }
            if (type == acc)
                state.accumulator += value;

            state.current_index++;
        }
    };


    class Parser
    {
        std::vector<Instruction> instructions_;
        std::set<int> seen_instructions_;
        InstructionState state_;
        bool verbose_;

    public:
        explicit Parser(std::stringstream& ss, const bool verbose = false): verbose_(verbose)
        {
            std::string line;
            while (std::getline(ss, line))
                instructions_.emplace_back(line);
        }

        explicit Parser(std::ifstream& ss, const bool verbose = false) : verbose_(verbose)
        {
            std::string line;
            while (std::getline(ss, line))
                instructions_.emplace_back(line);
            ss.close();
        }



        Parser(const Parser& other)
            : instructions_(other.instructions_),
              seen_instructions_(other.seen_instructions_),
              state_(other.state_),
              verbose_(other.verbose_)
        {
        }

        Parser(Parser&& other) noexcept
            : instructions_(std::move(other.instructions_)),
              seen_instructions_(std::move(other.seen_instructions_)),
              state_(std::move(other.state_)),
              verbose_(other.verbose_)
        {
        }

        Parser& operator=(const Parser& other)
        {
            if (this == &other)
                return *this;
            instructions_ = other.instructions_;
            seen_instructions_ = other.seen_instructions_;
            state_ = other.state_;
            verbose_ = other.verbose_;
            return *this;
        }

        Parser& operator=(Parser&& other) noexcept
        {
            if (this == &other)
                return *this;
            instructions_ = std::move(other.instructions_);
            seen_instructions_ = std::move(other.seen_instructions_);
            state_ = std::move(other.state_);
            verbose_ = other.verbose_;
            return *this;
        }

        ~Parser()
        {
            if (verbose_) std::cout << *this << std::endl;
        }

        [[nodiscard]] const Instruction& current_instruction() const
        {
            return instructions_.at(state_.current_index);
        }

        void step()
        {
            if (verbose_) std::cout << *this << std::endl;

            seen_instructions_.insert(state_.current_index);
            current_instruction().advance(state_);
        }

        void run()
        {
            try
            {
                while (!has_seen_instruction(state_.current_index))
                    step();
            }
            catch (const std::exception& e)
            {
                std::cout << state_ << std::endl;
            }
            
        }

        bool has_seen_instruction(const int index)
        {
            const auto it = seen_instructions_.find(index);
            return it != seen_instructions_.end();
        }

        std::vector<Parser> permute()
        {

            std::vector<Parser> permutations;
            for(auto i = 0; i < instructions_.size(); i++)
            {
                auto t = instructions_[i].type;
                if(t == nop || t == jmp)
                {
                    auto new_parser = *(this);
                    new_parser.instructions_[i].type = t == nop ? jmp : nop;
                    permutations.emplace_back(new_parser);
                }
            }
            return permutations;
        }

        friend std::ostream& operator<<(std::ostream& os, const Parser& obj)
        {
            return os
                << "state: " << obj.state_
                << "\n\tcurrent_instruction: " << obj.current_instruction();
        }
    };
}
