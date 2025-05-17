#include <bits/stdc++.h>
#include "../include/tiles.h"
#include <eigen3/Eigen/Dense>
#include <omp.h>

using namespace std;
using namespace Eigen;

int main ()
{
double d = 1e-2;
cout <<"$$$$ 6033  " <<e0/d <<endl;
for (int iss = 3; iss < 4; ++iss)
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
	THole hu, hd;
	double dh = d;
	double rr = 2.0;
	hu.P.init(0, 0,  dh/2 , 1.0/rr, 1.0/rr, 1, 1);
	hd.P.init(0, 0,  -dh/2, 1.0/rr, 1.0/rr, 1, 1);
	//~ hu.OP = &(fu.P);
	//~ hd.OP = &(fd.P);
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
cout << "before"<<T.Tiles.size()	<<endl;
	// حذف کاشی‌هایی که حداقل یکی از holes آنها کاملاً منطبق با خود کاشی است
//~ for (auto it = T.Tiles.begin(); it != T.Tiles.end(); ) {
    //~ bool shouldRemove = false;
    //~ for (const auto& hole : it->holes) {
        //~ if (!hole.empty && IsExactlySame(*it, hole)) {
            //~ shouldRemove = true;
            //~ break;
        //~ }
    //~ }
    //~ if (shouldRemove) {
        //~ it = T.Tiles.erase(it);  // حذف کاشی و ادامه حلقه
    //~ } else {
        //~ ++it;
    //~ }
//~ }
// به جای حذف، ابعاد hole را در 0.99 ضرب می‌کنیم
for (auto& tile : T.Tiles) {
    for (auto& hole : tile.holes) {
        if (!hole.empty && IsExactlySame(tile, hole)) {
            hole.lx *= 0;
            hole.ly *= 0;
            // در صورت نیاز می‌توانید موقعیت (x,y) را هم کمی تنظیم کنید
            // hole.x = ... 
            // hole.y = ...
        }
    }
}

cout << "after"<<T.Tiles.size()	<<endl;

}
	//~ cout << "Tiles  size()" << T.Tiles.size()<<endl;;

	T.make_mat();
	//~ cout << "Pij:0 - before ccc" <<endl<<T.Pij<< endl;
	
	T.change_mat_ccc(s.uindex, size);
	//~ cout << "Pij:0" <<endl<<T.Pij<< endl;

	VectorXd x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout << "without hole" << endl;
	cout <<iss<< " Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	//~ cout << x << endl;
	//~ 2222222222222222
	cout << "OOOOO with hole OOOO" << endl;

	T.make_mat2();
	//~ cout << "Pij:1 - before ccc" <<endl<<T.Pij<< endl;

	T.change_mat_ccc(s.uindex, size);
	//~ cout << "Pij:1" <<endl<<T.Pij<< endl;
	
	x = T.Pij.colPivHouseholderQr().solve(T.rhs);
	cout <<iss<< "  Solution: " << x.head(s.Pu.Tiles.size()).sum() << endl;
	cout << endl;	
}
	return 0;
};
