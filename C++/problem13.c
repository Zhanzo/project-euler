#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
  ifstream is("Problem13.txt");
  double numbers[100];
  double sum = 0;
  for (int i = 0; i < 100; i++)
    is >> numbers[i];
  

  for (int i = 0; i < 100; i++)
    sum += numbers[i];
  
  cout << setprecision(100) << sum << endl;
}
