cmake_minimum_required(VERSION 3.26)
project(TSP_Project)

set(CMAKE_CXX_STANDARD 17)

include_directories(
        include
)

set(SOURCE_FILES
        src/tsp_setup.cpp
        src/TSP.cpp
)

add_executable(TSP_Project ${SOURCE_FILES} main.cpp)
