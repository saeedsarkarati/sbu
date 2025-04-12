#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
cout <<"$$$$  " <<e0/d <<endl;
for (int iss = 1; iss < 20; ++iss)
{
	TCap s;
	s.dV = 1;
	s.Pu.init(0, 0,  d/2, 1, 1, iss, iss);
	s.Pd.init(0, 0, -d/2, 1, 1, iss, iss);
	s.make_v();
	TTiles T;
	s.uindex = T.push_tiles(s.Pu);
	s.dindex = T.push_tiles(s.Pd);
	int size = s.Pu.Tiles.size() + s.Pu.Tiles.size();
	TFVP fu, fd;
	double df = 0.5e-2;
	fu.P.init(0, 0,  df/2 , 0.1, 0.1, iss, iss);
	fd.P.init(0, 0,  -df/2, 0.1, 0.1, iss, iss);
	fu.index = T.push_tiles(fu.P);
	fd.index = T.push_tiles(fd.P);
	
	T.make_mat();
	T.change_mat_ccc(s.uindex, size);
	T.change_mat_ccc(fu.index, fu.P.Tiles.size() + fd.P.Tiles.size());

	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< " Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	//cout << x << endl;
	
}
	return 0;
};
