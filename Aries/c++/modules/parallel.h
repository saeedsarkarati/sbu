#include <iostream>
#include <cmath>
#include <vector>
#include "/usr/include/eigen3/Eigen/Dense"


using namespace std;
using namespace Eigen;

const double k0 = 8.9875517923e9;
const double e0 = 1 / (4 * M_PI * k0);

double Iss(double x1, double x2, double y1, double y2, double z) {
    double x = abs(x1 - x2);
    double y = abs(y1 - y2);
    z = abs(z);

    double I1 = 1.0 / 12 * (-x * x - y * y + 2 * z * z) * sqrt(x * x + y * y + z * z);
    double I2 = 1.0 / 4 * (y * (x * x - z * z)) * asinh(y / hypot(x, z));
    double I3 = 1.0 / 4 * (x * (y * y - z * z)) * asinh(x / hypot(y, z));
    double I4 = -1.0 / 2 * x * y * z * atan2(x * y, z * sqrt(x * x + y * y + z * z));

    double II = sqrt(M_PI) * (I1 + I2 + I3 + I4);
    return II;
}

double Iss_coplanar(double x1, double x2, double y1, double y2) {
    double x = abs(x1 - x2);
    double y = abs(y1 - y2);

    double I1 = 1.0 / 12 * (-x * x - y * y) * sqrt(x * x + y * y);
    double I2 = 0, I3 = 0;

    if (x != 0) {
        I2 = 1.0 / 4 * (y * x * x) * asinh(y / x);
    }
    if (y != 0) {
        I3 = 1.0 / 4 * (x * y * y) * asinh(x / y);
    }

    double II = sqrt(M_PI) * (I1 + I2 + I3);
    return II;
}

double ISum(const vector<vector<double>>& Limits, double z) {
    double s = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 0; l < 2; l++) {
                    double A = ((i + j + k + l) % 2 == 0) ? 1 : -1;
                    s += A * Iss(Limits[0][i], Limits[1][j], Limits[2][k], Limits[3][l], z);
                }
            }
        }
    }
    return s;
}

double ISum_coplanar(const vector<vector<double>>& Limits) {
    double s = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 0; l < 2; l++) {
                    double A = ((i + j + k + l) % 2 == 0) ? 1 : -1;
                    s += A * Iss_coplanar(Limits[0][i], Limits[1][j], Limits[2][k], Limits[3][l]);
                }
            }
        }
    }
    return s;
}

double saeed(double Lx, double Ly, double x0, double y0, double z) {
    vector<vector<double>> Limits = {
        {x0 - Lx / 2, x0 + Lx / 2},
        {-Lx / 2, Lx / 2},
        {y0 - Ly / 2, y0 + Ly / 2},
        {-Ly / 2, Ly / 2}
    };
    return ISum(Limits, z) * k0 / pow(Lx * Ly, 2) * 2 / sqrt(M_PI);
}

double parallel(double Lx1, double Ly1, double Lx2, double Ly2, double x0, double y0, double z) {
    vector<vector<double>> Limits = {
        {x0 - Lx1 / 2, x0 + Lx1 / 2},
        {-Lx2 / 2, Lx2 / 2},
        {y0 - Ly1 / 2, y0 + Ly1 / 2},
        {-Ly2 / 2, Ly2 / 2}
    };
    return ISum(Limits, z) * k0 / (Lx1 * Ly1 * Lx2 * Ly2) * 2 / sqrt(M_PI);
}

double saeed_coplanar(double Lx, double Ly, double x0, double y0) {
    vector<vector<double>> Limits = {
        {x0 - Lx / 2, x0 + Lx / 2},
        {-Lx / 2, Lx / 2},
        {y0 - Ly / 2, y0 + Ly / 2},
        {-Ly / 2, Ly / 2}
    };
    return ISum_coplanar(Limits) * k0 / pow(Lx * Ly, 2) * 2 / sqrt(M_PI);
}

double parallel_coplanar(double Lx1, double Ly1, double Lx2, double Ly2, double x0, double y0) {
    vector<vector<double>> Limits = {
        {x0 - Lx1 / 2, x0 + Lx1 / 2},
        {-Lx2 / 2, Lx2 / 2},
        {y0 - Ly1 / 2, y0 + Ly1 / 2},
        {-Ly2 / 2, Ly2 / 2}
    };
    return ISum_coplanar(Limits) * k0 / (Lx1 * Ly1 * Lx2 * Ly2) * 2 / sqrt(M_PI);
}

double saeed_sc(double x, double y) {
    double II = 1.0 / 3 * (pow(x, 3) + pow(y, 3)) + 1.0 / 3 * (-x * x - y * y) * hypot(x, y) +
                y * x * x * asinh(y / x) + x * y * y * asinh(x / y);
    return II * k0 / pow(x * y, 2) * 2;
}
