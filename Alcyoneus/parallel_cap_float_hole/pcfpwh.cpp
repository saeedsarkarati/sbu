#include <bits/stdc++.h>
#include "../include/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2, fd = d/2;;

for (int iss = 3; iss < 20; ++iss)
{

	TCap cap;
	TFCap f;
	TRect R0, Ru, Rd, fRu, fRd, hR0, hRu, hRd;
	TSegment hu, hd;
	R0.set(0,0,0,1,1);
	hR0.set(0,0,0,1.0/2,1.0/2);
	Ru = R0;
	Rd = R0;
	Ru.z = d /2;
	Rd.z = -d /2;
	fRu = R0;
	fRd = R0;
	fRu.z = fd /2;
	fRd.z = -fd /2;
	hRu = hR0;
	hRd = hR0;
	hRu.z = fRu.z;
	hRd.z = fRd.z;
	hu.R = hRu;
	hd.R = hRd;
	
	
	int n = iss;
	cap.Pu.init(Ru, n, n);
	cap.Pd.init(Rd, n, n);
	f.Pu.init(fRu, n, n);
	f.Pd.init(fRd, n, n);
	int num = f.Pu.Tiles.size()+ f.Pd.Tiles.size();
	
	removeTilesInHoles(f.Pu.Tiles, hu);
	removeTilesInHoles(f.Pd.Tiles, hd);
	int num2 = f.Pu.Tiles.size()+ f.Pd.Tiles.size();
	cout << num2 <<"   "<< num << endl;
	cap.make_v();
	f.make_v();
	TTiles T;
	cap.Pu.is = T.push_tiles(cap.Pu);
	cap.Pd.is = T.push_tiles(cap.Pd);
	f.Pu.is = T.push_tiles(f.Pu);
	f.Pd.is = T.push_tiles(f.Pd);
	T.make_mat();
	T.change_mat_ccc(cap.Pu.is.index, cap.Pu.is.size+cap.Pd.is.size);
	T.change_mat_ccc(f.Pu.is.index, f.Pu.is.size+f.Pd.is.size);
	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	//cout <<x<<endl;
	cout <<n<< "  Solution: " << x.head(cap.Pu.Tiles.size()).sum() << endl;
}
cout <<e0 /d<<endl;

return 0;
};
