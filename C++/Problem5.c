#include <iostream>
using namespace std;

bool isDivisible(int number)
{
  for (int i = 1; i <= 20; i++)
    if (number % i != 0) return false;
  return true;
}

int main()
{
  int i = 1;
  while (!isDivisible(i))
    i++;
  cout << i << endl;
}
