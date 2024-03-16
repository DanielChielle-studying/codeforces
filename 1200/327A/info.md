# A. Flipping Game 
**Difficulty**: 1200 
**Link**: https://codeforces.com/problemset/problem/327/A

# A. Flipping Game
Iahub got bored, so he invented a game to be played on paper.

He writes _n_ integers _a_ 1,  _a_ 2, ...,  _a_ _n_. Each of those integers
can be either 0 or 1. He's allowed to do exactly one move: he chooses two
indices _i_ and _j_ (1 ≤  _i_ ≤  _j_ ≤  _n_) and flips all values _a_ _k_ for
which their positions are in range [_i_ ,  _j_] (that is _i_ ≤  _k_ ≤  _j_).
Flip the value of _x_ means to apply operation _x_ = 1 \- _x_.

The goal of the game is that after exactly one move to obtain the maximum
number of ones. Write a program to solve the little game of Iahub.

Input

The first line of the input contains an integer _n_ (1 ≤  _n_ ≤ 100). In the
second line of the input there are _n_ integers: _a_ 1,  _a_ 2, ...,  _a_ _n_.
It is guaranteed that each of those _n_ values is either 0 or 1.

Output

Print an integer — the maximal number of 1s that can be obtained after exactly
one move.

Examples

Input

    
    
    5  
    1 0 0 1 0  
    

Output

    
    
    4  
    

Input

    
    
    4  
    1 0 0 1  
    

Output

    
    
    4  
    

Note

In the first case, flip the segment from 2 to 5 (_i_ = 2,  _j_ = 5). That flip
changes the sequence, it becomes: [1 1 1 0 1]. So, it contains four ones.
There is no way to make the whole sequence equal to [1 1 1 1 1].

In the second case, flipping only the second and the third element (_i_ = 2,
_j_ = 3) will turn all numbers into 1.

