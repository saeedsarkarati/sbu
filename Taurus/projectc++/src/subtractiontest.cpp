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
double Clx = 0.1, Cly = 0.1;
double A_Clx = 0.1, A_Cly = 0.1;
double Blx = 0.1, Bly = 0.1;
double dAB = 0.25, dCB = 0.2, dA_CB = 0.3;
double SA = Alx * Aly;
double SB = Blx * Bly;
double SC = Clx * Cly;
double SA_C = A_Clx * A_Cly;
double fAB = parallel_coplanar(Alx, Aly, Blx, Bly, dAB, 0);
double fCB = parallel_coplanar(Clx, Cly, Blx, Bly, dCB, 0);
double fA_CB = parallel_coplanar(A_Clx, A_Cly, Blx, Bly, dA_CB, 0);
cout <<"fCB  " <<fCB <<endl;
double ans;
ans = (fAB * (SA * SB) - fA_CB *(SA_C*SB) ) / (S_C * SB)
cout <<(fA1B*(SA1*SB) + fA2B*(SA2*SB)) / (SA * SB) <<endl;
	return 0;
};
