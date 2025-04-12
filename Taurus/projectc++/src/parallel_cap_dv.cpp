#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
cout <<"$$$$ " <<e0/d <<endl;
for (int iss = 1; iss < 10; ++iss)
{
	TCap s;
	s.dV = 1;
	s.Pu.init(0, 0,  d/2, 1, 1, iss, iss);
	s.Pd.init(0, 0, -d/2, 1, 1, iss, iss);
	s.make_v();
	TTiles T;
	s.uindex = T.push_tiles(s.Pu);
    s.dindex = T.push_tiles(s.Pd);
    int size = s.Pu.Tiles.size() + s.Pd.Tiles.size();
    T.make_mat();
    
    
    T.change_mat_ccc(s.uindex, size);

    VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< " Solution: " << x.head(x.size()/2).sum() << endl;
	
	
}
	return 0;
};
