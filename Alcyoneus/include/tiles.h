#include <bits/stdc++.h>
#include "parallel.h"
using namespace std;
//این برنامه صرفا برای کاش‌های صفحه x و y نوشته شده است.

class TPS {
	public:
	int index, size;
};
class TRect {
public:
    double x, y, z, lx, ly;

    // سازنده پیش‌فرض
    TRect() : x(0), y(0), z(0), lx(0), ly(0) {}

    // تابع برای مقداردهی بعد از ساخت شیء
    void set(double x_, double y_, double z_, double lx_, double ly_) {
        x = x_;
        y = y_;
        z = z_;
        lx = lx_;
        ly = ly_;
    }
};

class TSegment {
public:
    TRect R;
    double q;
    double V;
    bool empty;
    
    TSegment(bool empty = false) : empty(empty) {}
    void print()
    {
		cout <<" x: "<< R.x<<" y: "<< R.y<<" lx: "<< R.lx<<" ly: "<< R.ly<<endl;;
	};
    double area() const
    {
		double a = R.lx * R.ly;
		return a;
	};
};
double coupling(const TSegment& , const TSegment& );

class TPlate
{
	public:
	TPS is;
	TRect R;
	int nx, ny;
	vector <TSegment> Tiles;
	void init (TRect R, int nx, int ny);
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
	
	TPS push_tiles(TPlate T)
	{
		TPS i;
		i.index = Tiles.size();
		i.size = T.Tiles.size();
		for (size_t i = 0; i < T.Tiles.size(); ++i)
			Tiles.push_back(T.Tiles[i]);
		return i;
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
//Dielectric Plate^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class TDP
{
	public:
	TPlate P, U, D;
	double delta = 1e-10;
	double Uer = 1, Der = 1;
	MatrixXd Pu, Pd;

	void UDinit()
	{
		TRect UR;
		UR = P.R;
		UR.z += delta;
		U.init(UR, P.nx, P.ny);
		U.R.z += delta;
		TRect DR;
		DR = P.R;
		DR.z -= delta;
		D.init(DR, P.nx, P.ny);
	}
	void make_v()
	{
		for (size_t i = 0; i < P.Tiles.size(); ++i)
			P.Tiles[i].V = 0;
	};
	void make_P(TTiles t)
	{
		size_t n1 = U.Tiles.size();
		size_t n2 = t.Tiles.size();
		Pu.resize(n1, n2);
		Pd.resize(n1, n2);

		#pragma omp parallel for collapse(2)
		for (size_t i = 0; i < n1; ++i)
			for (size_t j = 0; j < n2; ++j)
			{
				Pu(i,j) = coupling(U.Tiles[i], t.Tiles[j]);
				Pd(i,j) = coupling(D.Tiles[i], t.Tiles[j]);
			}
		};
	

};
//Float Voltage Plate
class TFVP
{
	public:
	TPlate P;
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
	void make_v()
	{
		for (size_t i = 0; i < Pu.Tiles.size(); ++i)
			Pu.Tiles[i].V = dV;
		for (size_t i = 0; i < Pd.Tiles.size(); ++i)
			Pd.Tiles[i].V = 0;
	};
	
};
class TFCap
{
	// up و down در اینجا به معنا بالا و پایین بودن نیستند. ممکن است که دو صفحه خازنی چب و راست باشند.
	public:
	TPlate Pu, Pd;
	void make_v()
	{
		for (size_t i = 0; i < Pu.Tiles.size(); ++i)
			Pu.Tiles[i].V = 0;
		for (size_t i = 0; i < Pd.Tiles.size(); ++i)
			Pd.Tiles[i].V = 0;
	};
	
};
class TDCap
{
	// up و down در اینجا به معنا بالا و پایین بودن نیستند. ممکن است که دو صفحه خازنی چب و راست باشند.
	public:
	TPlate Pu, Pd;
	void make_v()
	{
		for (size_t i = 0; i < Pu.Tiles.size(); ++i)
			Pu.Tiles[i].V = 0;
		for (size_t i = 0; i < Pd.Tiles.size(); ++i)
			Pd.Tiles[i].V = 0;
	};
	
};

// در parallel_cap_hole.cpp (پس از includeها و قبل از main)
double coupling(const TSegment& t1, const TSegment& t2) {
    const double dx = fabs(t1.R.x - t2.R.x);
    const double dy = fabs(t1.R.y - t2.R.y);
    const double dz = fabs(t1.R.z - t2.R.z);
    
    return (fabs(t1.R.z - t2.R.z) > 1e-10)
        ? parallel(t1.R.lx, t1.R.ly, t2.R.lx, t2.R.ly, dx, dy, dz)
        : parallel_coplanar(t1.R.lx, t1.R.ly, t2.R.lx, t2.R.ly, dx, dy);
};
void TPlate::init (TRect R, int nx, int ny)
{
	int n = nx * ny;
	this->R.x = R.x;
	this->R.y = R.y;
	this->R.z = R.z;
	
	this->nx = nx;
	this->ny = ny;
	this->R.lx = R.lx;
	this->R.ly = R.ly;
	double Tlx = R.lx / nx;
	double Tly = R.ly / ny;
	Tiles.resize(n);
	for (int i = 0; i < n; ++i)
	{
		int ix = i % nx;
		int iy = i / ny;
		Tiles[i].R.x = ix * Tlx + R.x - R.lx /2 + Tlx /2;
		Tiles[i].R.y = iy * Tly + R.y - R.ly /2 + Tly /2;
		Tiles[i].R.z = R.z;
		Tiles[i].R.lx = Tlx;
		Tiles[i].R.ly = Tly;
	};
};

TSegment Intersection(const TSegment& rect1, const TSegment& rect2) {
    TSegment result;
    
    // بررسی صفحه z
    if (fabs(rect1.R.z - rect2.R.z) > 1e-10 * std::max(fabs(rect1.R.z), fabs(rect2.R.z))) {
        result.empty = true;
        return result;
    }

    // محاسبه مرزهای مستطیل‌ها
    double rect1_left = rect1.R.x - rect1.R.lx / 2;
    double rect1_right = rect1.R.x + rect1.R.lx / 2;
    double rect1_bottom = rect1.R.y - rect1.R.ly / 2;
    double rect1_top = rect1.R.y + rect1.R.ly / 2;
    
    double rect2_left = rect2.R.x - rect2.R.lx / 2;
    double rect2_right = rect2.R.x + rect2.R.lx / 2;
    double rect2_bottom = rect2.R.y - rect2.R.ly / 2;
    double rect2_top = rect2.R.y + rect2.R.ly / 2;
    
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
    result.R.x = (intersect_left + intersect_right) / 2;
    result.R.y = (intersect_bottom + intersect_top) / 2;
    result.R.lx = intersect_right - intersect_left;
    result.R.ly = intersect_top - intersect_bottom;
    result.empty = false;
    
    return result;
};
bool IsExactlySame(const TSegment& a, const TSegment& b, double tol = 1e-10) {
    return 
        fabs(a.R.x - b.R.x) < tol &&
        fabs(a.R.y - b.R.y) < tol &&
        fabs(a.R.lx - b.R.lx) < tol &&
        fabs(a.R.ly - b.R.ly) < tol &&
        fabs(a.R.z - b.R.z) < tol;
}

bool IsInside(const TSegment& tile, const TSegment& hole) {
    // محاسبه مرزهای کاشی
    double tile_left = tile.R.x - tile.R.lx / 2;
    double tile_right = tile.R.x + tile.R.lx / 2;
    double tile_bottom = tile.R.y - tile.R.ly / 2;
    double tile_top = tile.R.y + tile.R.ly / 2;

    // محاسبه مرزهای حفره
    double hole_left = hole.R.x - hole.R.lx / 2;
    double hole_right = hole.R.x + hole.R.lx / 2;
    double hole_bottom = hole.R.y - hole.R.ly / 2;
    double hole_top = hole.R.y + hole.R.ly / 2;

    // بررسی قرارگیری کامل کاشی داخل حفره
    return (tile_left >= hole_left) && (tile_right <= hole_right) &&
           (tile_bottom >= hole_bottom) && (tile_top <= hole_top);
}
	void removeTilesInHoles2(vector<TSegment>& tiles, const TSegment& hole) {
    tiles.erase(
        remove_if(tiles.begin(), tiles.end(),
            [&hole](const TSegment& tile) {
                TSegment intersection = Intersection(tile, hole);
                return !intersection.empty && 
                       (intersection.R.lx == tile.R.lx) && 
                       (intersection.R.ly == tile.R.ly);
            }),
        tiles.end());
}
  void removeTilesInHoles(vector<TSegment>& tiles, const TSegment& hole) {
    tiles.erase(
        remove_if(tiles.begin(), tiles.end(),
            [&hole](const TSegment& tile) {
                return IsInside(tile, hole);
            }),
        tiles.end());
}
void splitTilesAroundHoles(vector<TSegment>& tiles, const TSegment& hole) {
    vector<TSegment> newTiles;
    for (const auto& tile : tiles) {
        TSegment intersection = Intersection(tile, hole);
        if (intersection.empty) {
            // اگر هیچ اشتراکی با حفره ندارد، همان کاشی را نگه دار
            newTiles.push_back(tile);
        } else {
            // محاسبه مرزهای کاشی و حفره
            double tile_left = tile.R.x - tile.R.lx / 2;
            double tile_right = tile.R.x + tile.R.lx / 2;
            double tile_bottom = tile.R.y - tile.R.ly / 2;
            double tile_top = tile.R.y + tile.R.ly / 2;

            double hole_left = hole.R.x - hole.R.lx / 2;
            double hole_right = hole.R.x + hole.R.lx / 2;
            double hole_bottom = hole.R.y - hole.R.ly / 2;
            double hole_top = hole.R.y + hole.R.ly / 2;

            // تقسیم کاشی به بخش‌های خارج از حفره
            // بخش چپ
            if (tile_left < hole_left) {
                TSegment leftTile = tile;
                leftTile.R.x = (tile_left + hole_left) / 2;
                leftTile.R.lx = hole_left - tile_left;
                newTiles.push_back(leftTile);
            }
            // بخش راست
            if (tile_right > hole_right) {
                TSegment rightTile = tile;
                rightTile.R.x = (hole_right + tile_right) / 2;
                rightTile.R.lx = tile_right - hole_right;
                newTiles.push_back(rightTile);
            }
            // بخش پایین
            if (tile_bottom < hole_bottom) {
                TSegment bottomTile = tile;
                bottomTile.R.y = (tile_bottom + hole_bottom) / 2;
                bottomTile.R.ly = hole_bottom - tile_bottom;
                newTiles.push_back(bottomTile);
            }
            // بخش بالا
            if (tile_top > hole_top) {
                TSegment topTile = tile;
                topTile.R.y = (hole_top + tile_top) / 2;
                topTile.R.ly = tile_top - hole_top;
                newTiles.push_back(topTile);
            }
        }
    }
    tiles = newTiles;
}
