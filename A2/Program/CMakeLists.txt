cmake_minimum_required(VERSION 3.29)
project(Program)

set(CMAKE_CXX_STANDARD 20)

add_executable(Program main.cpp
        arrayGenerator.cpp
        arrayGenerator.h
        sortTester.cpp
        sortTester.h
        sortAlgorithms.h
        sortAlgorithms.cpp)
