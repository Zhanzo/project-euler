#include <iostream>
using namespace std;

int findPythagoreanTriplet(int number)
{
  for (int a = 1; a < number; a++)
  {
    for (int b = a+1; b < number; b++)
    {
      for (int c = b+1; c < number; c++)
        if (a + b + c == number && a*a + b*b == c*c) return a*b*c;
    }
  }
  return -1;
}

int main()
{
  int prod = findPythagoreanTriplet(1000);
  cout << prod << endl;
} 
