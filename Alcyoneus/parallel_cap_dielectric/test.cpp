class S;  // پیش‌اعلان (Forward Declaration) چون کلاس T به کلاس S نیاز دارد  

class T {
public:
    int a, b;
    
    void addFromS(S x);  // تعریف متد بعد از تعریف کلاس S  
};

class S {
public:
    int a, b;
    
    void addFromT(T x) {
        a += x.b;
    }
};

// تعریف کامل متد addFromS (باید بعد از تعریف کلاس S باشد)  
void T::addFromS(S x) {
    a += x.a;
}
int main()
{
};
