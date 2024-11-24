#include "arrayGenerator.h"

ArrayGenerator::ArrayGenerator() : randGen(std::random_device{}()) {
}

std::vector<int> ArrayGenerator::getRandom(const int size) {
    std::uniform_int_distribution dist(0, maxValue);
    std::vector<int> result(size);
    for (int i = 0; i < size; i++) {
        result[i] = dist(randGen);
    }
    return result;
}

std::vector<int> ArrayGenerator::getReverseSorted(const int size) {
    std::vector<int> result(size);
    for (int i = 0; i < size; i++) {
        result[i] = size - i;
    }
    return result;
}

std::vector<int> ArrayGenerator::getNearlySorted(const int size) {
    std::vector<int> result(size);
    for (int i = 0; i < size; i++) {
        result[i] = i;
    }

    const int swapsCount = size * 0.05;
    std::uniform_int_distribution dist(0, size - 1);
    for (int i = 0; i < swapsCount; i++) {
        const int idx1 = dist(randGen);
        const int idx2 = dist(randGen);
        std::swap(result[idx1], result[idx2]);
    }
    return result;
}