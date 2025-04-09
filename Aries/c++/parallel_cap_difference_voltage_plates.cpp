#include <bits/stdc++.h>
#include "modules/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1;
cout <<"$$$$  "<<e0 /d<<endl;
for (int iss = 1; iss < 5; ++iss)
{
	TCap s;
	s.dV = 1;
	s.Pu.init(0, 0,  d/2, 1, 1, iss, iss);
	s.Pd.init(0, 0, -d/2, 1, 1, iss, iss);
	   // تعریف ماتریس کوپلینگ به صورت مستقل
    
	//vector<vector<double>> Pij(s.P.Tiles.size(), vector<double>(s.P.Tiles.size(), 0.0));
    size_t n1 = s.Pu.Tiles.size(), n = 2 * n1;
	MatrixXd Pij(n, n);
	TPlate *p1, *p2;
    // پر کردن ماتریس کوپلینگ
    #pragma omp parallel for collapse(2)
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
        {
			if (i < n1)
				p1 = &(s.Pu);
			else
				p1 = &(s.Pd);
			if (j < n1)
				p2 = &(s.Pu);
			else
				p2 = &(s.Pd);
            Pij(i,j) = coupling(p1->Tiles[i%n1], p2->Tiles[j%n1]);
		}
    //VectorXd Ones = VectorXd::Ones(s.V);
    //VectorXd rhs = VectorXd::Constant(n, s.V); // V مقدار ثابت شما
	VectorXd rhs(n);
	rhs.head(n1).setConstant(1);    // نیمه اول = 1
	rhs.tail(n - n1).setConstant(0); // نیمه دوم = -1
	RowVectorXd last_row = Pij.bottomRows(1); 
	Pij.topRows(n-1).rowwise() -= last_row;
	Pij.bottomRows(1).setOnes();
	
	double last = rhs(rhs.size()-1);
    rhs.array() -= last;
    rhs(rhs.size()-1) = 0;

    VectorXd x = Pij.colPivHouseholderQr().solve(rhs);
	//cout << Pij<<endl;
	cout << "diff_volt"<<endl;
	cout <<iss<< " qtotal: " << x.head(n1).sum() << endl;
	//cout <<iss<< " Q: " <<endl<< x << endl;
	//cout <<endl;
}
	return 0;
};
