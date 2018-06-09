#include <iostream>
using namespace std;

bool isEven(int number)
{
  return number % 2 == 0;
}

long collatzSequence(long number, int sequences)
{
  sequences++;
  if (number == 1) return sequences;
  if (isEven(number)) return collatzSequence(number/2, sequences);
  else return collatzSequence(3*number + 1, sequences);
}

int main()
{
  int number = 0;
  int max_sequences = 0;
  for (int i = 1; i < 1000000; i++)
  {
    int sequences = collatzSequence(i, 0);
    if (sequences > max_sequences) 
    { 
      max_sequences = sequences;
      number = i;
    }
  }

  cout << number << endl;
}
