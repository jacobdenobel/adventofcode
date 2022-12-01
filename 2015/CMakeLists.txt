cmake_minimum_required(VERSION 3.11)

project(
  AdventOfCode2015
  VERSION 1.0
  LANGUAGES CXX
)

add_executable(main main.cpp utils.hpp)
set_property(TARGET main PROPERTY CXX_STANDARD 20)
