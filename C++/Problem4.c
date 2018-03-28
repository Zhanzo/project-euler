#include <iostream>
using namespace std;

int number_of_digits(int number)
{
  int len = 0;
  do
  {
    number /= 10;
    len++;
  } while (number);
  return len;
}

bool isPalindrome(int number)
{
  int length = number_of_digits(number);
  int list_number[length];
  int i = 0;
  while (i < length)
  {
    list_number[i] = (number % 10);
    number = number / 10;
    i++;
  }
  for (i = 0; i < length; i++)
  {
    if (list_number[i] != list_number[length-1-i])
    {
      return false;
    }
  }
  return true;
}

int main()
{
  int max_palindrome = 0;
  for (int i = 100; i < 1000; i++)
  {
    for (int j = 100; j < 1000; j++)
    {
      if (isPalindrome(i*j))
      {
        if (i*j > max_palindrome) max_palindrome = i*j;
      }
    }
  }
  cout << max_palindrome << "\n";
  
}


