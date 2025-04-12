#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
for (int iss = 1; iss < 20; ++iss)
{
	TCVP s;
	s.V = 1;
	s.P.init(0, 0, 0, 1, 1, iss, iss);
	s.make_v();
	   // تعریف ماتریس کوپلینگ به صورت مستقل
    
	//vector<vector<double>> Pij(s.P.Tiles.size(), vector<double>(s.P.Tiles.size(), 0.0));
    TTiles T;
    s.index = T.push_tiles(s.P);
    T.make_mat();
    cout << s.P.Tiles.size()<< T.Tiles.size()<<endl;
    VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);

	cout <<iss<< " Solution: " << x.sum() << endl;

}
	return 0;
};
