#pragma once
#include <vector>
#include "arrayGenerator.h"

class SortTester {
    ArrayGenerator arrayGen;
    const int testsCount = 10;

    [[nodiscard]] long long testArray(const std::vector<int>& arr, bool isHybrid, int threshold) const;

public:
    void runTests();
};