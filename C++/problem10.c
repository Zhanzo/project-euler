#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int number)
{
  for (int i = 3; i <=  round(sqrt(number))+1; i += 2)
    if (number % i == 0) return false;
  return true;
}

int main()
{
  long sum = 5;
  for (int i = 5; i < 2000000; i+=2)
    if (isPrime(i)) sum += i;
  cout << sum << endl;
}
