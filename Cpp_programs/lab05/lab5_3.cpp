#include <iostream>
#include <cmath>

class Vector2D {
private:
    double x;
    double y;

public:
    Vector2D& setX(double valX) {
        x = valX;
        return *this;
    }

    Vector2D& setY(double valY) {
        y = valY;
        return *this;
    }

    double length(){
        return std::sqrt(x * x + y * y);
    }

    Vector2D& normalize() {
        double len = length();
        if (len != 0) {
            x /= len;
            y /= len;
        }
        return *this;
    }

    void print() const {
        std::cout << "Vector(" << x << ", " << y << ")" << std::endl;
    }
};

int main() {
    Vector2D vec;

    vec.setX(3.0).setY(4.0);
    vec.print();
    vec.normalize();
    vec.print();
    std::cout << vec.length() << std::endl;

    return 0;
}