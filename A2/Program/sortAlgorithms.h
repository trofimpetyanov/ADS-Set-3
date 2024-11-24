#pragma once
#include <vector>

void insertionSort(std::vector<int>& arr, int left, int right);
void merge(std::vector<int>& arr, int left, int mid, int right);
void mergeSort(std::vector<int>& arr, int left, int right);
void hybridMergeSort(std::vector<int>& arr, int left, int right, int threshold);