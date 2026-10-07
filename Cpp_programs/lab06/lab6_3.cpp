#include <iostream>
#include <string>
using namespace std;

class Box {
    private:
        double _width;
        double _height;
        double _depth;
    public:
        Box(double width, double height, double depth) {
            _width = width;
            _height = height;
            _depth = depth;
        }
        double volume() const {
            return _width * _height * _depth;
        }
        void print() const {
            cout << "Szerokosc: " << _width << "; Wysokosc: " << _height << "; Glebokosc: " << _depth << endl;
            cout << "Objetosc: " << volume();
        }
        friend const Box& compareVolume(const Box& b1, const Box& b2);
};

const Box& compareVolume(const Box& b1, const Box& b2) {
    return (b1.volume() >= b2.volume()) ? b1 : b2; //fancy zapis if-a
}

int main() {
    Box box1(2.0, 3.0, 4.0);
    Box box2(3.0, 2.5, 3.5);
    Box box3(1.5, 4.0, 5.0);
    cout << "Box 1:" << endl;
    box1.print();
    cout << endl;
    cout << "Box 2:" << endl;
    box2.print();   
    cout << endl;
    cout << "Box 3:" << endl;
    box3.print();
    cout << endl << endl;

    cout << "Wieksze z box1 i box2:" << endl;
    compareVolume(box1, box2).print();
    cout << endl;

    cout << "Wieksze z box1 i box3:" << endl;
    compareVolume(box1, box3).print();
    cout << endl;

    cout << "Wieksze z box2 i box3:" << endl;
    compareVolume(box2, box3).print();
    cout << endl;

    return 0;
}