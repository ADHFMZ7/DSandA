#include <iostream>

using namespace std;

class Rectangle{

public:
  int GetSide1(){return side1;}
  int GetSide2(){return side2;}
  int GetArea(){return side1 * side2;}
  void SetSide1(int val){side1 = val;}
  void SetSide2(int val){side2 = val;}

private:
  int side1;
  int side2;
};


int main()
{
  
  Rectangle rect;

  rect.SetSide1(10);
  rect.SetSide2(15);

  cout << rect.GetArea() << endl;
}


