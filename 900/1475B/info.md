# B. New Year's Number 
**Difficulty**: 900 
**Link**: https://codeforces.com/problemset/problem/1475/B

# B. New Year's Number
Polycarp remembered the $2020$-th year, and he is happy with the arrival
of the new $2021$-th year. To remember such a wonderful moment, Polycarp
wants to represent the number $n$ as the sum of a certain number of
$2020$ and a certain number of $2021$.

For example, if:

  * $n=4041$, then the number $n$ can be represented as the sum $2020 + 2021$; 
  * $n=4042$, then the number $n$ can be represented as the sum $2021 + 2021$; 
  * $n=8081$, then the number $n$ can be represented as the sum $2020 + 2020 + 2020 + 2021$; 
  * $n=8079$, then the number $n$ cannot be represented as the sum of the numbers $2020$ and $2021$. 

Help Polycarp to find out whether the number $n$ can be represented as the
sum of a certain number of numbers $2020$ and a certain number of numbers
$2021$.

Input

The first line contains one integer $t$ ($1 \leq t \leq 10^4$) — the
number of test cases. Then $t$ test cases follow.

Each test case contains one integer $n$ ($1 \leq n \leq 10^6$) — the
number that Polycarp wants to represent as the sum of the numbers $2020$
and $2021$.

Output

For each test case, output on a separate line:

  * "YES" if the number $n$ is representable as the sum of a certain number of $2020$ and a certain number of $2021$; 
  * "NO" otherwise. 

You can output "YES" and "NO" in any case (for example, the strings yEs, yes,
Yes and YES will be recognized as positive).

Example

Input

    
    
    5
    1
    4041
    4042
    8081
    8079
    

Output

    
    
    NO
    YES
    YES
    YES
    NO
    
