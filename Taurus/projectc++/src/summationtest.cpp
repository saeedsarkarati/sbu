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
double Alx = 0.2, Aly = 0.1;
double A1lx = 0.1, A1ly = 0.1;
double A2lx = 0.1, A2ly = 0.1;
double Blx = 0.1, Bly = 0.1;
double dAB = 0.25, dA1B = 0.3, dA2B = 0.2;
double SA = Alx * Aly;
double SB = Blx * Bly;
double SA1 = A1lx * A1ly;
double SA2 = A2lx * A2ly;
double fAB = parallel_coplanar(Alx, Aly, Blx, Bly, dAB, 0);
double fA1B = parallel_coplanar(A1lx, A1ly, Blx, Bly, dA1B, 0);
double fA2B = parallel_coplanar(A2lx, A2ly, Blx, Bly, dA2B, 0);
cout <<"fAB  " <<fAB <<endl;
cout <<"fA1B  " <<fA1B*(SA1*SB)<<endl;
cout <<"fA2B  " <<fA2B*(SA2*SB)<<endl;
cout <<(fA1B*(SA1*SB) + fA2B*(SA2*SB)) / (SA * SB) <<endl;
	return 0;
};
