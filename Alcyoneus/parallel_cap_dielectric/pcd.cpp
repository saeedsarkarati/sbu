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
	TDP di_up, di_down;
	TRect R0, Ru, Rd,Rdiu, Rdid;
	R0.set(0,0,0,1,1);
	Ru = R0;
	Rd = R0;
	Rdiu = R0;
	Rdid = R0;
	Ru.z = d /2;
	Rd.z = -d /2;
	Rdiu.z = dd /2;
	Rdid.z = -dd /2;

for (int iss =1; iss < 2; ++iss)
{
	
	int n = iss;
	cap.Pu.init(Ru, n, n);
	cap.Pd.init(Rd, n, n);
	di_up.P.init(Rdiu, n, n);
	di_up.UDinit();
	di_down.P.init(Rdid, n, n);
	di_down.UDinit();
	cap.make_v();
	di_up.make_v();
	di_down.make_v();
	TTiles T;
	cap.Pu.is = T.push_tiles(cap.Pu);
	cap.Pd.is = T.push_tiles(cap.Pd);
	di_up.P.is = T.push_tiles(di_up.P);
	di_down.P.is = T.push_tiles(di_down.P);
	T.make_mat();
	di_up.make_P(T);
	di_down.make_P(T);
	if (iss == 1)
	{
		cout << T.Pij<<endl;
		cout <<endl;
		cout <<"1 "<< di_up.Pu<<endl;
		cout <<"2 "<< di_up.Pd<<endl;
		cout <<"3 "<< di_down.Pu<<endl;
		cout <<"4 "<< di_down.Pd<<endl;
		cout <<"5 "<< di_up.Pu - di_up.Pd<<endl;
		cout <<"6 "<< di_down.Pu - di_down.Pd<<endl;
	}
		

/*

	T.change_mat_ccc(cap.Pu.is.index, cap.Pu.is.size+cap.Pd.is.size);
	T.change_mat_ccc(di.Pu.is.index, di.Pu.is.size+di.Pd.is.size);
	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	//cout <<x<<endl;
	cout <<n<< "  Solution: " << x.head(cap.Pu.Tiles.size()).sum() << endl;
*/
}
cout <<e0 /d<<endl;

return 0;
};
