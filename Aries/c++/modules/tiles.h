#include <bits/stdc++.h>
#include "parallel.h"
using namespace std;
//این برنامه صرفا برای کاش‌های صفحه x و y نوشته شده است.


class TSegment 
{
	public:
	double x, y, z, lx, ly, q;
	
};

class TPlate
{
	public:
	double x, y, z, lx, ly;
	int nx, ny;
	bool Active = true;
	vector <TSegment> Tiles;
	void init (double x, double y, double z, double lx, double ly, int nx, int ny);
};
//Float Voltage Plate
class TFVP
{
	public:
	TPlate P;
};
//Constant Voltage Plate
class TCVP
{
	public:
	TPlate P;
	double V = 0;
};
class TCap
{
	// up و down در اینجا به معنا بالا و پایین بودن نیستند. ممکن است که دو صفحه خازنی چب و راست باشند.
	public:
	TPlate Pu, Pd;
	double dV = 1;
};
class THole
{
	TPlate P;
	TPlate* OP;
};


double coupling (TSegment t1, TSegment t2)
{
	double dx = fabs(t1.x - t2.x), dy = fabs(t1.y - t2.y), dz = fabs(t1.z - t2.z);
	if (fabs(t1.z - t2.z) > 1e-10 )
		return parallel(t1.lx, t1.ly, t2.lx, t2.ly, dx, dy, dz);
	return parallel_coplanar(t1.lx, t1.ly, t2.lx, t2.ly, dx, dy);

};
void TPlate::init (double x, double y, double z, double lx, double ly, int nx, int ny)
{
	int n = nx * ny;
	this->x = x;
	this->y = y;
	this->z = z;
	
	this->nx = ny;
	this->ny = ny;
	this->lx = lx;
	this->ly = ly;
	double Tlx = lx / nx;
	double Tly = ly / ny;
	Tiles.resize(n);
	for (int i = 0; i < n; ++i)
	{
		int ix = i % nx;
		int iy = i / ny;
		Tiles[i].x = ix * Tlx + x - lx /2 + Tlx /2;
		Tiles[i].y = iy * Tly + y - ly /2 + Tly /2;
		Tiles[i].z = z;
		Tiles[i].lx = Tlx;
		Tiles[i].ly = Tly;
	};
};
