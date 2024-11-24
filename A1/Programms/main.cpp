#include <iostream>
#include <random>
#include <cmath>
#include <fstream>

bool isInsideCircle(double x, double y, double cx, double cy, double r) {
    return (x - cx) * (x - cx) + (y - cy) * (y - cy) <= r * r;
}

double calculateArea(int pointsCount, bool wideArea) {
    double circleX1 = 1, circleY1 = 1, radius1 = 1;
    double circleX2 = 1.5, circleY2 = 2, radius2 = sqrt(5)/2;
    double circleX3 = 2, circleY3 = 1.5, radius3 = sqrt(5)/2;

    double minX, maxX, minY, maxY;
    if (wideArea) {
        minX = std::min({circleX1 - radius1, circleX2 - radius2, circleX3 - radius3});
        maxX = std::max({circleX1 + radius1, circleX2 + radius2, circleX3 + radius3});
        minY = std::min({circleY1 - radius1, circleY2 - radius2, circleY3 - radius3});
        maxY = std::max({circleY1 + radius1, circleY2 + radius2, circleY3 + radius3});
    } else {
        minX = 1;
        maxX = 2;
        minY = 1;
        maxY = 2;
    }

    std::random_device randDevice;
    std::mt19937 randGen(randDevice());
    std::uniform_real_distribution<> distX(minX, maxX);
    std::uniform_real_distribution<> distY(minY, maxY);

    int pointsInside = 0;
    for (int i = 0; i < pointsCount; i++) {
        double pointX = distX(randGen);
        double pointY = distY(randGen);

        if (isInsideCircle(pointX, pointY, circleX1, circleY1, radius1) &&
            isInsideCircle(pointX, pointY, circleX2, circleY2, radius2) &&
            isInsideCircle(pointX, pointY, circleX3, circleY3, radius3)) {
            pointsInside++;
        }
    }

    return (maxX - minX) * (maxY - minY) * pointsInside / pointsCount;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::ofstream resultFile("monteCarloResults.csv");
    resultFile << "Points,WideArea,NarrowArea,ExactArea\n";

    const double exactArea = M_PI/4 + 1.25 * asin(0.8) - 1;

    for (int points = 100; points <= 100000; points += 500) {
        double wideAreaResult = calculateArea(points, true);
        double narrowAreaResult = calculateArea(points, false);

        resultFile << points << ','
                  << wideAreaResult << ','
                  << narrowAreaResult << ','
                  << exactArea << '\n';
    }

    return 0;
}