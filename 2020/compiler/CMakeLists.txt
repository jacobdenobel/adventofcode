# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.8)

project ("parser" CXX)
set (CMAKE_CXX_STANDARD 17)

add_subdirectory(extern/pybind11)

add_executable(main 
	"parser/main.cpp"
	"parser/parser.hpp"
)

pybind11_add_module(parser 
	"parser/parser.hpp"
)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
set_target_properties(parser PROPERTIES LINKER_LANGUAGE CXX)
target_compile_definitions(parser PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})



