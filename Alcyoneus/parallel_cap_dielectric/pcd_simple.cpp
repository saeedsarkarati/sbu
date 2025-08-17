#include <bits/stdc++.h>
#include "../include/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
	double d_cap = 1e-2, d_dielectric = d_cap/2;;
	TCap cap;
	TDP d_u, d_d; //dielectric up .... dielectric down
	TRect R0, Ru, Rd, Rd_u, Rd_d;
	R0.set(0,0,0,1,1);
	Ru = R0;
	Rd = R0;
	Rd_u = R0;
	Rd_d = R0;
	Ru.z = d_cap / 2;
	Rd.z = -d_cap / 2;
	Rd_u.z = d_dielectric / 2;
	Rd_d.z = -d_dielectric / 2;

	cap.Pu.init(Ru, 1, 1);
	cap.Pd.init(Rd, 1, 1);
	d_u.P.init(Rd_u, 1, 1);
	d_u.UDinit();
	d_d.P.init(Rd_d, 1, 1);
	d_d.UDinit();
	cap.make_v();
	d_u.make_v();
	d_d.make_v();
	TTiles T;
	cap.Pu.is = T.push_tiles(cap.Pu);
	cap.Pd.is = T.push_tiles(cap.Pd);
	d_u.P.is = T.push_tiles(d_u.P);
	d_d.P.is = T.push_tiles(d_d.P);
	T.make_mat();
	d_u.make_P(T);
	d_d.make_P(T);
	cout<<d_u.Pu<<endl;
	cout<<endl;
	cout<<T.Pij <<endl;

return 0;
};
