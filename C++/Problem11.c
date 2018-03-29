#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream is("Problem11.txt");
  int numbers[20][20];
  for (int i = 0; i < 20; i++)
  {
    for (int j = 0; j < 20; j++)
    {
      is >> numbers[i][j];
    }
  }
  
  // vertical
  long max_prod = 0;
  for (int i = 0; i < 17; i++)
  {
    for (int j = 0; j < 20; j++)
    {
      long prod = numbers[i][j] * numbers[i+1][j] * numbers[i+2][j] * numbers[i+3][j];
      if (prod > max_prod) max_prod = prod;
    }
  }

  // horizontal
  for (int i = 0; i < 20; i++)
  {
    for (int j = 0; j < 17; j++)
    {
      long prod = numbers[i][j] * numbers[i][j+1] * numbers[i][j+2] * numbers[i][j+3];
      if (prod > max_prod) max_prod = prod;
    }
  }

  // diagonal - \*
  for (int i = 0; i < 17; i++)
  {
    for (int j = 0; j < 17; j++)
    {
      long prod = numbers[i][j] * numbers[i+1][j+1] * numbers[i+2][j+2] * numbers[i+3][j+3];
      if (prod > max_prod) max_prod = prod;
    }
  }

  // diagonal - /*
  for (int i = 3; i < 20; i++)
  {
    for (int j = 0; j < 17; j++)
    {
      long prod = numbers[i][j] * numbers[i-1][j+1] * numbers[i-2][j+2] * numbers[i-3][j+3];
      if (prod > max_prod) max_prod = prod;
    }
  }

  
  cout << max_prod << endl;
} 
