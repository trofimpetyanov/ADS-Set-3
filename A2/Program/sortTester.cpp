#include "sortTester.h"
#include <fstream>
#include "sortAlgorithms.h"

long long SortTester::testArray(const std::vector<int>& arr, const bool isHybrid, const int threshold) const {
    long long totalTime = 0;

    for (int test = 0; test < testsCount; test++) {
        std::vector<int> testArr = arr;
        auto start = std::chrono::high_resolution_clock::now();

        if (isHybrid) {
            hybridMergeSort(testArr, 0, testArr.size() - 1, threshold);
        } else {
            mergeSort(testArr, 0, testArr.size() - 1);
        }

        auto end = std::chrono::high_resolution_clock::now();
        totalTime += std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    }

    return totalTime / testsCount;
}

void SortTester::runTests() {
    std::vector thresholds = {5, 10, 15, 20, 30, 50};
    std::vector<int> sizes;
    for (int size = 500; size <= 10000; size += 100) {
        sizes.push_back(size);
    }

    std::ofstream randomFile("randomResults.csv");
    std::ofstream reverseFile("reverseResults.csv");
    std::ofstream nearlySortedFile("nearlySortedResults.csv");

    auto writeHeader = [&](std::ofstream& file) {
        file << "Size,MergeSort";
        for (const int t : thresholds) {
            file << ",Hybrid" << t;
        }
        file << '\n';
    };

    writeHeader(randomFile);
    writeHeader(reverseFile);
    writeHeader(nearlySortedFile);

    for (int size : sizes) {
        auto randomArr = arrayGen.getRandom(size);
        auto reverseArr = ArrayGenerator::getReverseSorted(size);
        auto nearlySortedArr = arrayGen.getNearlySorted(size);

        randomFile << size << ',' << testArray(randomArr, false, 0);
        for (int t : thresholds) {
            randomFile << ',' << testArray(randomArr, true, t);
        }
        randomFile << '\n';

        reverseFile << size << ',' << testArray(reverseArr, false, 0);
        for (int t : thresholds) {
            reverseFile << ',' << testArray(reverseArr, true, t);
        }
        reverseFile << '\n';

        nearlySortedFile << size << ',' << testArray(nearlySortedArr, false, 0);
        for (int t : thresholds) {
            nearlySortedFile << ',' << testArray(nearlySortedArr, true, t);
        }
        nearlySortedFile << '\n';
    }
}