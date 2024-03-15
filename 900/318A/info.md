# A. Even Odds 
**Difficulty**: 900 
**Link**: https://codeforces.com/problemset/problem/318/A

# A. Even Odds
Being a nonconformist, Volodya is displeased with the current state of things,
particularly with the order of natural numbers (natural number is positive
integer number). He is determined to rearrange them. But there are too many
natural numbers, so Volodya decided to start with the first _n_. He writes
down the following sequence of numbers: firstly all odd integers from 1 to _n_
(in ascending order), then all even integers from 1 to _n_ (also in ascending
order). Help our hero to find out which number will stand at the position
number _k_.

Input

The only line of input contains integers _n_ and _k_ (1 ≤  _k_ ≤  _n_ ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in C++.
It is preferred to use the cin, cout streams or the %I64d specifier.

Output

Print the number that will stand at the position number _k_ after Volodya's
manipulations.

Examples

Input

    
    
    10 3  
    

Output

    
    
    5

Input

    
    
    7 7  
    

Output

    
    
    6

Note

In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2,
4, 6, 8, 10}. The third place in the sequence is therefore occupied by the
number 5.

