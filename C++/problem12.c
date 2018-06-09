#include <iostream>
using namespace std;

int findTriangularNumber(int number)
{
  int sum = 1;
  for (int i = 2; ; i++)
  {
    sum += i;
    int divisors = 1;
    for (int j = 1; j <= sum/2; j++) 
      if (sum % j == 0) divisors++;
    //cout << sum << " " << divisors << endl;
    if (divisors > number) return sum;
  }
  return -1;
}

int main()
{
  cout << findTriangularNumber(500) << endl;
}
