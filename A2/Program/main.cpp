#include <iostream>
#include "sortTester.h"

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    SortTester tester;
    tester.runTests();

    return 0;
}