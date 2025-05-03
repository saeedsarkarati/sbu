#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
cout <<"$$$$ 6033  " <<e0/d <<endl;
double f;
double Alx = 0.2, Aly = 0.2;
double A1lx = 0.1, A1ly = 0.1;
double A2lx = 0.1, A2ly = 0.1;
double A3lx = 0.1, A3ly = 0.1;
double A4lx = 0.1, A4ly = 0.1;
double Blx = 0.1, Bly = 0.1;
double dABx = 0.25, dABy = 0.05;
double dA1Bx = 0.3, dA1By = 0.0;
double dA2Bx = 0.2, dA2By = 0.0;
double dA3Bx = 0.3, dA3By = 0.1;
double dA4Bx = 0.2, dA4By = 0.1;
double SA = Alx * Aly;
double SB = Blx * Bly;
double SA1 = A1lx * A1ly;
double SA2 = A2lx * A2ly;
double SA3 = A3lx * A3ly;
double SA4 = A4lx * A4ly;
double fAB = parallel_coplanar(Alx, Aly, Blx, Bly, dABx, dABy);
double fA1B = parallel_coplanar(A1lx, A1ly, Blx, Bly, dA1Bx, dA1By);
double fA2B = parallel_coplanar(A2lx, A2ly, Blx, Bly, dA2Bx, dA2By);
double fA3B = parallel_coplanar(A3lx, A3ly, Blx, Bly, dA3Bx, dA3By);
double fA4B = parallel_coplanar(A4lx, A4ly, Blx, Bly, dA4Bx, dA4By);
double ans1, ans2;
ans1 = (fA1B * (SA1 * SB) + fA2B * (SA2 * SB) + fA3B * (SA3 * SB) ) 
		/ ( (SA1 + SA2 + SA3) * SB);
ans2 = (fAB * (SA * SB) - fA4B * (SA4 * SB) ) 
		/ ( (SA - SA4) * SB);
cout <<ans1 <<endl;
cout <<"!"<<ans2 <<endl;
double z = 0.1;
fAB = parallel(Alx, Aly, Blx, Bly, dABx, dABy,z);
fA1B = parallel(A1lx, A1ly, Blx, Bly, dA1Bx, dA1By,z);
fA2B = parallel(A2lx, A2ly, Blx, Bly, dA2Bx, dA2By,z);
fA3B = parallel(A3lx, A3ly, Blx, Bly, dA3Bx, dA3By,z);
fA4B = parallel(A4lx, A4ly, Blx, Bly, dA4Bx, dA4By,z);

ans1 = (fA1B * (SA1 * SB) + fA2B * (SA2 * SB) + fA3B * (SA3 * SB) ) 
		/ ( (SA1 + SA2 + SA3) * SB);
ans2 = (fAB * (SA * SB) - fA4B * (SA4 * SB) ) 
		/ ( (SA - SA4) * SB);
cout <<ans1 <<endl;
cout <<"!"<<ans2 <<endl;

	return 0;
};
