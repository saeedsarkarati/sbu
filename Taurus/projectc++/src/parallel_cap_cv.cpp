#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
for (int iss = 1; iss < 10; ++iss)
{
	double d = 1e-2;
	cout <<"$$$$  "<<e0 /d<<endl;
	TCVP a, b;
	a.V = .5;
	b.V = -.5;
	a.P.init(0, 0,  d/2, 1, 1, iss, iss);
	a.make_v();
	b.P.init(0, 0, -d/2, 1, 1, iss, iss);
	b.make_v();
	   // تعریف ماتریس کوپلینگ به صورت مستقل
    
    TTiles T;
    a.index = T.push_tiles(a.P);
    b.index = T.push_tiles(b.P);
    T.make_mat();
    VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);

	cout <<iss<< " Solution: " << x.head(x.size()/2).sum() << endl;
	//cout <<x <<endl;
}
	return 0;
};
