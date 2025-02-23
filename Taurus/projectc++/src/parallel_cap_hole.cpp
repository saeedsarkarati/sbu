#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
cout <<"$$$$ 6033  " <<e0/d <<endl;
for (int iss = 1; iss < 2; ++iss)
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
	double fs = 1.0;
	fu.P.init(0, 0,  df/2 , fs, fs, iss, iss);
	fd.P.init(0, 0,  -df/2, fs, fs, iss, iss);
	fu.index = T.push_tiles(fu.P);
	fd.index = T.push_tiles(fd.P);
	THole hu, hd, h;
	double dh = df;
	double rr = 1.0;
	hu.P.init(0, 0,  dh/2 , fs/rr, fs/rr, 1, 1);
	hd.P.init(0, 0,  -dh/2, fs/rr, fs/rr, 1, 1);
	hu.OP = &(fu.P);
	hd.OP = &(fd.P);
	vector <int> findex;
	vector <double> area_ratio;
	for (size_t i =0; i < T.Tiles.size(); ++i)
	{
		TSegment fh;
		fh = Intersection (T.Tiles[i], hu.P.Tiles[0]);
		if (fh.lx > 1e-10 && fh.ly > 1e-10){ 
			h.P.Tiles.push_back(fh);
			findex.push_back(i);
			area_ratio.push_back(fh.lx * fh.ly / (T.Tiles[i].lx * T.Tiles[i].lx));
		};
	};
	for (size_t i =0; i < T.Tiles.size(); ++i)
	{
		TSegment fh;
		fh = Intersection (T.Tiles[i], hd.P.Tiles[0]);
		if (fh.lx > 1e-10 && fh.ly > 1e-10){ 
			h.P.Tiles.push_back(fh);
			findex.push_back(i);
			area_ratio.push_back(fh.lx * fh.ly / (T.Tiles[i].lx * T.Tiles[i].ly));
		};
	};
	cout << "holes " << endl;
	for (size_t i = 0; i < h.P.Tiles.size(); ++i)
		cout <<i <<" : "<<findex[i] << " area_r : " << area_ratio[i]<< " --- "
				<<h.P.Tiles[i].x << " : " << h.P.Tiles[i].y
				<< " : " << h.P.Tiles[i].lx<< " : " 
						<< h.P.Tiles[i].ly << endl;
	cout << "QQ" << T.Tiles.size()<<endl;
	int hole_index = T.push_tiles(h.P);
	cout << "QQQ" << T.Tiles.size()<<endl;;

	T.make_mat();
	
	T.change_mat_ccc(s.uindex, size);
	
	for (size_t i = 0; i < h.P.Tiles.size(); ++i) {
        int row = hole_index + i;
        T.Pij.row(row).setZero();                  // صفر کردن تمام سطر
        T.Pij(row, row) = 1.0;                     // ستون قطری برابر 1
        T.Pij(row, findex[i]) = area_ratio[i];    // ستون findex برابر -area_ratio
        T.rhs(row) = 0.0;                          // صفر کردن rhs
    }

	T.change_mat_ccc(fu.index, fu.P.Tiles.size() + fd.P.Tiles.size()
					+h.P.Tiles.size());
	
	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< " Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	cout << x << endl;
	
}
	return 0;
};
