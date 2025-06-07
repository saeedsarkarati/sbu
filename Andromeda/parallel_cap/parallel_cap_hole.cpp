#include <bits/stdc++.h>
#include "tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;fa

int main ()
{
double d = 1e-2;
cout <<"$$$$ 6033  " <<e0/d <<endl;
for (int iss = 1; iss < 11; ++iss)
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
	double df = d/100;
	double fs = 1.0;
	fu.P.init(0, 0,  df/2 , fs, fs, iss, iss);
	fd.P.init(0, 0,  -df/2, fs, fs, iss, iss);
	fu.index = T.push_tiles(fu.P);
	fd.index = T.push_tiles(fd.P);
	THole hu, hd, h;
	double dh = df;
	double rr = 1e100;
	hu.P.init(0, 0,  dh/2 , fs/rr, fs/rr, 1, 1);
	hd.P.init(0, 0,  -dh/2, fs/rr, fs/rr, 1, 1);
	hu.OP = &(fu.P);
	hd.OP = &(fd.P);
	if (true){
	for (size_t i = 0; i < T.Tiles.size(); ++i)
	{
		TSegment fh;
		fh = Intersection (T.Tiles[i], hu.P.Tiles[0]);
		if (!(fh.empty)){ 
			//~ cout << "hu--Tile index:  "<< i << endl;

			T.Tiles[i].holes.push_back(fh);
		};
	};
	for (size_t i =0; i < T.Tiles.size(); ++i)
	{
		TSegment fh;
		fh = Intersection (T.Tiles[i], hd.P.Tiles[0]);
		if (!(fh.empty)){ 
			//~ cout << "hd---Tile index:  "<< i << endl;

			T.Tiles[i].holes.push_back(fh);
		};
	};
}
	//~ cout << "Tiles  size()" << T.Tiles.size()<<endl;;

	T.make_mat();
	//~ cout << "Pij:0 - before ccc" <<endl<<T.Pij<< endl;
	
	T.change_mat_ccc(s.uindex, size);
	


	T.change_mat_ccc(fu.index, fu.P.Tiles.size() + fd.P.Tiles.size());
	//~ cout << "Pij:0" <<endl<<T.Pij<< endl;

	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< " Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	//~ cout << x << endl;
	//~ 2222222222222222
	cout << "22222222222222222" << endl;

	T.make_mat2();
	//~ cout << "Pij:1 - before ccc" <<endl<<T.Pij<< endl;

	T.change_mat_ccc(s.uindex, size);
	


	T.change_mat_ccc(fu.index, fu.P.Tiles.size() + fd.P.Tiles.size());
	//~ cout << "Pij:1" <<endl<<T.Pij<< endl;
	
	 x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< "  Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	//~ cout << x << endl;	
}
	return 0;
};
