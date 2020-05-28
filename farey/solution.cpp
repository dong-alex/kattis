
/*
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (farey length) - https://en.wikipedia.org/wiki/Farey_sequence#Sequence_length_and_index_of_a_fraction
  (Euler Phi) - https://github.com/UAPSPC/Code-Archive/blob/master/num_theory/eulerphi.c
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  N/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

#define MAXN 10001
using namespace std;

vector<int> eulerPhi(MAXN, 0);

vector<int> query(MAXN, 0);
// calculate euler phi for all values from
void phi(int n)
{
  // base

  // iterate for all possible values

  int i, count, res = 1, temp = n;

  for (i = 2; i * i <= n; i++)
  {
    count = 0;
    while (n % i == 0)
    {
      n /= i;
      count++;
    }
    if (count > 0)
      res *= (pow(i, count) - pow(i, count - 1));
  }
  if (n > 1)
    res *= (n - 1);
  eulerPhi[temp] = res;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  // calculate euler phi
  // solve for Fn = 1 + sum(eulerphi(m))
  // Fn = Fn-1 + phi
  eulerPhi[0] = 1;
  eulerPhi[1] = 1;
  for (int k = 1; k < MAXN; k++)
  {
    phi(k);
  }
  // calculate the length given above - looks like range sum query
  // F(1) = F(0) + phi(1)
  query[0] = 1;
  for (int i = 1; i < MAXN; i++)
  {
    query[i] = query[i - 1] + eulerPhi[i];
  }

  int n;
  scanf("%d\n", &n);
  while (n--)
  {
    int test, num;
    scanf("%d %d\n", &test, &num);
    printf("%d %d\n", test, query[num]);
  }
}