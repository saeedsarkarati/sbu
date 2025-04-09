#ifndef TILES_H
#define TILES_H

#include <vector>
#include <Eigen/Dense>
#include "parallel.h"

class TSegment {
public:
    double x, y, z, lx, ly, q;
    double V;
};

class TPlate {
public:
    double x, y, z, lx, ly;
    int nx, ny;
    bool Active = true;
    std::vector<TSegment> Tiles;
    
    void init(double x, double y, double z, double lx, double ly, int nx, int ny);
};

class TTiles {
public:
    std::vector<TSegment> Tiles;
    Eigen::MatrixXd Pij;
    Eigen::VectorXd rhs;
    
    void make_mat();
    int push_tiles(TPlate T);
    void cap_dv_change_mat(int start, int n);
    void FVP_change_mat(int start, int n);
};

class TFVP {
public:
    TPlate P;
    int index = 0;
    void make_v();
};

class TCVP {
public:
    TPlate P;
    double V = 0;
    int index = 0;
    void make_v();
};

class TCap {
public:
    TPlate Pu, Pd;
    double dV = 1;
    int uindex = 0;
    int dindex = 0;
    void make_v();
};

class THole {
public:
    TPlate P;
    TPlate* OP;
    int index = 0;
    void make_v();
};

double coupling(TSegment t1, TSegment t2);

#endif // TILES_H
