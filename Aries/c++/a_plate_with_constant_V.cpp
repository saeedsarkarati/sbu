#include <bits/stdc++.h>
#include "modules/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
for (int iss = 1; iss < 100; ++iss)
{
	TCVP s;
	s.V = 1;
	s.P.init(0, 0, 0, 1, 1, iss, iss);
	   // تعریف ماتریس کوپلینگ به صورت مستقل
    
	//vector<vector<double>> Pij(s.P.Tiles.size(), vector<double>(s.P.Tiles.size(), 0.0));
    size_t n = s.P.Tiles.size();
	MatrixXd Pij(n, n);

    // پر کردن ماتریس کوپلینگ
    #pragma omp parallel for collapse(2)
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
        {
            Pij(i,j) = coupling(s.P.Tiles[i], s.P.Tiles[j]);
		}
    //VectorXd Ones = VectorXd::Ones(s.V);
    VectorXd rhs = VectorXd::Constant(n, s.V); // V مقدار ثابت شما

    VectorXd x = Pij.colPivHouseholderQr().solve(rhs);

	cout <<iss<< " Solution: " << x.sum() << endl;

}
	return 0;
};
