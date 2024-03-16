# B. T-primes 
**Difficulty**: 1300 
**Link**: https://codeforces.com/problemset/problem/230/B

# B. T-primes
We know that prime numbers are positive integers that have exactly two
distinct positive divisors. Similarly, we'll call a positive integer _t_
Т-prime, if _t_ has exactly three distinct positive divisors.

You are given an array of _n_ positive integers. For each of them determine
whether it is Т-prime or not.

Input

The first line contains a single positive integer, _n_ (1 ≤  _n_ ≤ 105),
showing how many numbers are in the array. The next line contains _n_ space-
separated integers _x_ _i_ (1 ≤  _x_ _i_ ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in С++.
It is advised to use the cin, cout streams or the %I64d specifier.

Output

Print _n_ lines: the _i_ -th line should contain "YES" (without the quotes),
if number _x_ _i_ is Т-prime, and "NO" (without the quotes), if it isn't.

Examples

Input

    
    
    3  
    4 5 6  
    

Output

    
    
    YES  
    NO  
    NO  
    

Note

The given test has three numbers. The first number 4 has exactly three
divisors — 1, 2 and 4, thus the answer for this number is "YES". The second
number 5 has two divisors (1 and 5), and the third number 6 has four divisors
(1, 2, 3, 6), hence the answer for them is "NO".

