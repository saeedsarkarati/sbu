
class TSegment 
{
	public:
	double x, y, z, lx, ly, q;
	double V;
	
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
double coupling (TSegment, TSegment);
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
	int push_tiles(TPlate T)
	{
		int index = Tiles.size();
		for (size_t i = 0; i < T.Tiles.size(); ++i)
			Tiles.push_back(T.Tiles[i]);
		return index;
	};
	void cap_dv_change_mat(int start, int n )
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
        Pij.row(last_row_idx).setOnes();

        // تنظیم مقدار rhs سطر آخر به 0
        rhs(last_row_idx) = 0;
	};
	void FVP_change_mat(int start, int n )
	{

        int last_row_idx = start + n - 1;

        RowVectorXd last_row_Pij = Pij.row(last_row_idx);
        double last_row_rhs = rhs(last_row_idx);
        // برای n-1 سطر اول در محدوده: سطر آخر را از آنها کم کن
        for (int i = start; i < last_row_idx; ++i)
        {
            Pij.row(i) -= last_row_Pij;  // کم کردن سطر آخر از سطرهای بالایی در ماتریس
            rhs(i) -= last_row_rhs;      // کم کردن مقدار سطر آخر از سطرهای بالایی در بردار
        }

        // تنظیم سطر آخر ماتریس Pij به تمام 1
        Pij.row(last_row_idx).setOnes();

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



