#include <iostream>
using namespace std;

bool isPrime(int number)
{
  for (int i = 2; i < number/2; i++)
    if (number % i == 0) return false;
  return true;
}

int main()
{
  int prime_counter = 1;
  int number = 0;
  for (number = 3; prime_counter <= 10001; number++)
    if (isPrime(number)) prime_counter++;
  cout << number-1 << endl;
}
