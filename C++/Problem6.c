#include <iostream>
using namespace std;

int sumOfSquares()
{
  int sum = 0;
  for (int i = 1; i <= 100; i++)
    sum += i*i;
  return sum;
}

int squareOfSums()
{
  int sum = 0;
  for (int i = 1; i <= 100; i++)
    sum += i;
  return sum*sum;
}

int main()
{
  int sum_of_squares = sumOfSquares();
  int square_of_sums = squareOfSums();

  int diff = square_of_sums - sum_of_squares;
  cout << diff << endl;
}
