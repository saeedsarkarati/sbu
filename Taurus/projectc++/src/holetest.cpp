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


	TCap s;
	s.dV = 1;
	s.Pu.init(0, 0,  d/2, 1, 1, 1, 1);
	s.Pd.init(0, 0, -d/2, 1, 1, 1, 1);
	s.make_v();
	TTiles T;
	s.uindex = T.push_tiles(s.Pu);
	s.dindex = T.push_tiles(s.Pd);
	int size = s.Pu.Tiles.size() + s.Pu.Tiles.size();
	TFVP fu, fd;
	double df = 0.5e-2;
	double fs = 1.0;
	fu.P.init(0, 0,  df/2 , fs, fs, 1, 1);
	fd.P.init(0, 0,  -df/2, fs, fs, 1, 1);
	fu.index = T.push_tiles(fu.P);
	fd.index = T.push_tiles(fd.P);
	THole hu, hd, h;
	double dh = df;
	double rr = 1e1;
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
			cout << "hu--Tile index:  "<< i << endl;
		cout << "intersect"<<endl;
		fh.print();

			T.Tiles[i].holes.push_back(fh);
		};
	};
	for (size_t i =0; i < T.Tiles.size(); ++i)
	{
		TSegment fh;
		fh = Intersection (T.Tiles[i], hd.P.Tiles[0]);
		if (!(fh.empty)){ 
			cout << "hd---Tile index:  "<< i << endl;
		cout << "intersect"<<endl;
		fh.print();

			T.Tiles[i].holes.push_back(fh);
		};
	};
}
	double vv = coupling(T.Tiles[3].holes[0], T.Tiles[1]);
	cout << "-------------" << vv <<endl;
	vv = coupling(T.Tiles[3], T.Tiles[4]);
	cout << "-------------" << vv <<endl;
	cout << "Tiles  size()" << T.Tiles.size()<<endl;;

	T.make_mat();
	cout << "Pij:0 - before ccc" <<endl<<T.Pij<< endl;
	
	

	
	//~ 2222222222222222
	cout << "22222222222222222" << endl;

	T.make_mat2();
	cout << "Pij:1 - before ccc" <<endl<<T.Pij<< endl;


	
	

	return 0;
};
