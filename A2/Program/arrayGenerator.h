#pragma once
#include <vector>
#include <random>

class ArrayGenerator {
    std::mt19937 randGen;
    const int maxSize = 10000;
    const int maxValue = 6000;

public:
    ArrayGenerator();
    std::vector<int> getRandom(int size);

    static std::vector<int> getReverseSorted(int size);
    std::vector<int> getNearlySorted(int size);
};