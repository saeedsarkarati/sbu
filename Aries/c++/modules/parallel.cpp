#include "parallel.h"

int main() {
    double d = 0, Lx = 1, Ly = 1, z = 1;

    double Isc = saeed_sc(Lx, Ly);
    cout << "saeed self coupling: " << scientific << Isc << endl;

    double Icp = saeed_coplanar(Lx, Ly, d, 0);
    cout << "saeed coplanar: " << scientific << Icp << endl;

    double Is = saeed(Lx, Ly, d, 0, z);
    cout << "saeed: " << scientific << Is << endl;

    Icp = parallel_coplanar(Lx / 2, Ly / 2, Lx, Ly, d, 0);
    cout << "parallel coplanar: " << scientific << Icp << endl;

    Is = parallel(Lx / 2, Ly / 2, Lx, Ly, d, 0, z);
    cout << "parallel: " << scientific << Is << endl;

    Icp = parallel_coplanar(Lx, Ly, Lx, Ly, 0, 0);
    cout << "parallel coplanar normal: " << scientific << Icp << endl;

    Icp = parallel_coplanar(Lx / 10, Ly / 10, Lx / 10, Ly / 10, 0, 0);
    cout << "parallel coplanar shortened: " << scientific << Icp << endl;

    return 0;
}
