#include <bits/stdc++.h>
#include "../include/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
for (int iss = 3; iss < 10; ++iss)
{

	TCap cap;
	TRect R0, Ru, Rd;
	R0.set(0,0,0,1,1);
	Ru = R0;
	Rd = R0;
	Ru.z = d /2;
	Rd.z = -d /2;
	
	int n = iss;
	cap.Pu.init(Ru, n, n);
	cap.Pd.init(Rd, n, n);
	cap.make_v();
	TTiles T;
	cap.Pu.is = T.push_tiles(cap.Pu);
	cap.Pd.is = T.push_tiles(cap.Pd);
	T.make_mat();
	T.change_mat_ccc(cap.Pu.is.index, cap.Pu.is.size+cap.Pd.is.size);
	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	//cout <<x<<endl;
	cout <<n<< "  Solution: " << x.head(cap.Pu.Tiles.size()).sum() << endl;
}
cout <<e0 /d<<endl;

return 0;
};
