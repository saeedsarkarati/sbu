#include <bits/stdc++.h>
#include "parallel.h"
using namespace std;
//این برنامه صرفا برای کاش‌های صفحه x و y نوشته شده است.

class TSegment {
public:
    double x, y, z, lx, ly, q;
    double V;
    bool empty;
	vector<TSegment> holes;
    
    TSegment(bool empty = false) : empty(empty) {}
    void print()
    {
		cout <<" x: "<< x<<" y: "<< y<<" lx: "<< lx<<" ly: "<< ly<<endl;;
	};
    double area() const
    {
		double a = lx * ly;
		return a;
	};
    double area_without_holes () const
    {
		double a = lx * ly;
		    for ( auto hole: holes) {
				a -= hole.area();
			}
		return a;
	}; 
};
double coupling(const TSegment& , const TSegment& );
double coupling_with_holes(const TSegment& t1, const TSegment& t2);

class TPlate
{
	public:
	double x, y, z, lx, ly;
	int nx, ny;
	bool Active = true;
	vector <TSegment> Tiles;
	void init (double x, double y, double z, double lx, double ly, int nx, int ny);
};
class TTiles
{
	public:
	vector <TSegment> Tiles;
	MatrixXd Pij;
	VectorXd rhs;
	void make_mat()
	{
		size_t n = Tiles.size();
		Pij.resize(n, n);
		rhs.resize(n);
		#pragma omp parallel for collapse(2)
		for (size_t i = 0; i < n; ++i)
			for (size_t j = 0; j < n; ++j)
			{
				Pij(i,j) = coupling(Tiles[i], Tiles[j]);
			}
		#pragma omp parallel for
		for (size_t i = 0; i < n; ++i)
			rhs(i) = Tiles[i].V;
	};	
	void make_mat2()
	{
		size_t n = Tiles.size();
		Pij.resize(n, n);
		rhs.resize(n);
		//~ #pragma omp parallel for collapse(2)
		for (size_t i = 0; i < n; ++i)
			for (size_t j = 0; j < n; ++j)
			{
				Pij(i,j) = coupling_with_holes(Tiles[i], Tiles[j]);
			}
		//~ #pragma omp parallel for
		for (size_t i = 0; i < n; ++i)
			rhs(i) = Tiles[i].V;
	};
	int push_tiles(TPlate T)
	{
		int index = Tiles.size();
		for (size_t i = 0; i < T.Tiles.size(); ++i)
			Tiles.push_back(T.Tiles[i]);
		return index;
	};
	//constant charge condition
	void change_mat_ccc(int start, int n )
	{
		 // اندیس سطر آخر در محدوده مورد نظر

        int last_row_idx = start + n - 1;

        // ذخیره سطر آخر (قبل از تغییر)
        RowVectorXd last_row_Pij = Pij.row(last_row_idx);
        double last_row_rhs = rhs(last_row_idx);
        // برای n-1 سطر اول در محدوده: سطر آخر را از آنها کم کن
        for (int i = start; i < last_row_idx; ++i)
        {
            Pij.row(i) -= last_row_Pij;  // کم کردن سطر آخر از سطرهای بالایی در ماتریس
            rhs(i) -= last_row_rhs;      // کم کردن مقدار سطر آخر از سطرهای بالایی در بردار
        }

        // تنظیم سطر آخر ماتریس Pij به تمام 1
        //Pij.row(last_row_idx).setOnes();
		Pij.row(last_row_idx).setZero();

		// ستون‌های start تا start+n-1 را در این سطر برابر 1 قرار می‌دهیم
		for (int j = start; j < start + n; ++j) {
			Pij(last_row_idx, j) = 1.0;
		}

        // تنظیم مقدار rhs سطر آخر به 0
        rhs(last_row_idx) = 0;
	};
};
//Float Voltage Plate
class TFVP
{
	public:
	TPlate P;
	int index = 0;
	void make_v()
	{
		for (size_t i = 0; i < P.Tiles.size(); ++i)
			P.Tiles[i].V = 0;
	};
};
//Constant Voltage Plate
class TCVP
{
	public:
	TPlate P;
	double V = 0;
	int index = 0;
	void make_v()
	{
		for (size_t i = 0; i < P.Tiles.size(); ++i)
			P.Tiles[i].V = V;
	};

};
class TCap
{
	// up و down در اینجا به معنا بالا و پایین بودن نیستند. ممکن است که دو صفحه خازنی چب و راست باشند.
	public:
	TPlate Pu, Pd;
	double dV = 1;
	int uindex = 0;
	int dindex = 0;
	void make_v()
	{
		for (size_t i = 0; i < Pu.Tiles.size(); ++i)
			Pu.Tiles[i].V = dV;
		for (size_t i = 0; i < Pd.Tiles.size(); ++i)
			Pd.Tiles[i].V = 0;
	};
	
};
class THole
{
	public:
	TPlate P;
	TPlate* OP;
	int index = 0;
	void make_v()
	{
		for (size_t i = 0; i < P.Tiles.size(); ++i)
			P.Tiles[i].V = 0;
	};

	//void push_tiles(TTiles T)
	//{
		//index = T.tiles.size();
		//T.Tiles.push_back(P.Tiles);
	//};
};

// در parallel_cap_hole.cpp (پس از includeها و قبل از main)
double coupling(const TSegment& t1, const TSegment& t2) {
    const double dx = fabs(t1.x - t2.x);
    const double dy = fabs(t1.y - t2.y);
    const double dz = fabs(t1.z - t2.z);
    
    return (fabs(t1.z - t2.z) > 1e-10)
        ? parallel(t1.lx, t1.ly, t2.lx, t2.ly, dx, dy, dz)
        : parallel_coplanar(t1.lx, t1.ly, t2.lx, t2.ly, dx, dy);
};
double coupling_with_holes(const TSegment& t1, const TSegment& t2) {
    double cv = coupling(t1, t2) * (t1.area() * t2.area()) ;
    static int i = 0 , j =0 ;
    //cout << "j: -----------------" << j<<endl;
    j++;
    for ( auto hole : t2.holes) {
        cv -= coupling(t1, hole) * (t1.area() * hole.area());
    }
    //cout <<i<<" : cv: "<< cv <<endl;
    ++i;
    
    for ( auto hole : t1.holes) {
        cv -= coupling(t2, hole) * (t2.area() * hole.area());
    }
    //cout <<i<<" : cv: "<< cv <<endl;
    ++i;
    
    for ( auto hole1 : t1.holes) {
        for ( auto hole2 : t2.holes) {
            cv += coupling(hole1, hole2) * (hole1.area() * hole2.area());
        }
    }
    //cout <<i<<" : cv: "<< cv <<endl;
    ++i;
    
    return cv/(t1.area_without_holes() * t2.area_without_holes());
};
void TPlate::init (double x, double y, double z, double lx, double ly, int nx, int ny)
{
	int n = nx * ny;
	this->x = x;
	this->y = y;
	this->z = z;
	
	this->nx = nx;
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

TSegment Intersection(const TSegment& rect1, const TSegment& rect2) {
    TSegment result;
    
    // بررسی صفحه z
    if (fabs(rect1.z - rect2.z) > 1e-10 * std::max(fabs(rect1.z), fabs(rect2.z))) {
        result.empty = true;
        return result;
    }

    // محاسبه مرزهای مستطیل‌ها
    double rect1_left = rect1.x - rect1.lx / 2;
    double rect1_right = rect1.x + rect1.lx / 2;
    double rect1_bottom = rect1.y - rect1.ly / 2;
    double rect1_top = rect1.y + rect1.ly / 2;
    
    double rect2_left = rect2.x - rect2.lx / 2;
    double rect2_right = rect2.x + rect2.lx / 2;
    double rect2_bottom = rect2.y - rect2.ly / 2;
    double rect2_top = rect2.y + rect2.ly / 2;
    
    // محاسبه اشتراک
    double intersect_left = std::max(rect1_left, rect2_left);
    double intersect_right = std::min(rect1_right, rect2_right);
    double intersect_bottom = std::max(rect1_bottom, rect2_bottom);
    double intersect_top = std::min(rect1_top, rect2_top);
    
    // بررسی وجود اشتراک
    if (intersect_left >= intersect_right || intersect_bottom >= intersect_top) {
        result.empty = true;
        return result;
    }
    
    // محاسبه مستطیل اشتراک
    result.x = (intersect_left + intersect_right) / 2;
    result.y = (intersect_bottom + intersect_top) / 2;
    result.lx = intersect_right - intersect_left;
    result.ly = intersect_top - intersect_bottom;
    result.empty = false;
    
    return result;
};


