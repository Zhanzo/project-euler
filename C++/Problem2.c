#include <stdio.h>

int main()
{
  int i = 1;
  int j = 2;
  int sum = 2;

  while (j < 4000000)
  {
    int k = i + j;
    i = j;
    j = k;
    if (j % 2 == 0)
    {
      sum += j;
    }
  }
  
  printf("%d \n", sum);
}
