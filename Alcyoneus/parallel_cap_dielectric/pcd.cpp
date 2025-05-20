#include <bits/stdc++.h>
#include "../include/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2, dd = d/2;;


	TCap cap;
	TFCap di;
	TRect R0, Ru, Rd, dRu, dRd, dR0;
	R0.set(0,0,0,1,1);
	dR0.set(0,0,0,1.0/2,1.0/2);
	Ru = R0;
	Rd = R0;
	Ru.z = d /2;
	Rd.z = -d /2;
	dRu = R0;
	dRd = R0;
	dRu.z = dd /2;
	dRd.z = -dd /2;
for (int iss =1; iss < 10; ++iss)
{
	
	int n = iss;
	cap.Pu.init(Ru, n, n);
	cap.Pd.init(Rd, n, n);
	di.Pu.init(dRu, n, n);
	di.Pd.init(dRd, n, n);
	cap.make_v();
	di.make_v();
	TTiles T;
	cap.Pu.is = T.push_tiles(cap.Pu);
	cap.Pd.is = T.push_tiles(cap.Pd);
	di.Pu.is = T.push_tiles(di.Pu);
	di.Pd.is = T.push_tiles(di.Pd);
	T.make_mat();
	if (iss == 1)
		cout << T.Pij<<endl;

	T.change_mat_ccc(cap.Pu.is.index, cap.Pu.is.size+cap.Pd.is.size);
	T.change_mat_ccc(di.Pu.is.index, di.Pu.is.size+di.Pd.is.size);
	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	//cout <<x<<endl;
	cout <<n<< "  Solution: " << x.head(cap.Pu.Tiles.size()).sum() << endl;
}
cout <<e0 /d<<endl;

return 0;
};
