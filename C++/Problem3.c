#include <stdio.h>
#include <math.h>

bool isPrime(int number)
{
  if (number % 2 == 0)
  {
    return false;
  }
  for (int i = 3; i <= round(sqrt(number)) + 1; i += 2)
  {
    if (number % i == 0) 
    {
      return false;
    }
  }
  return true;
}

int main()
{
  long number = 600851475143;
  int max_factor = 0;

  for (int i = 3; i <= round(sqrt(number)) +  1; i += 2)
  {
    if (number % i == 0)
    {
      if (isPrime(i))
      {
        max_factor = i;
      }
    }
  }

  printf("%d \n", max_factor);
}
