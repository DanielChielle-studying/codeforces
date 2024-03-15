# A. I Wanna Be the Guy 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/469/A

# A. I Wanna Be the Guy
There is a game called "I Wanna Be the Guy", consisting of _n_ levels. Little
X and his friend Little Y are addicted to the game. Each of them wants to pass
the whole game.

Little X can pass only _p_ levels of the game. And Little Y can pass only _q_
levels of the game. You are given the indices of levels Little X can pass and
the indices of levels Little Y can pass. Will Little X and Little Y pass the
whole game, if they cooperate each other?

Input

The first line contains a single integer _n_ (1 ≤  _n_ ≤ 100).

The next line contains an integer _p_ (0 ≤  _p_ ≤  _n_) at first, then follows
_p_ distinct integers _a_ 1,  _a_ 2, ...,  _a_ _p_ (1 ≤  _a_ _i_ ≤  _n_).
These integers denote the indices of levels Little X can pass. The next line
contains the levels Little Y can pass in the same format. It's assumed that
levels are numbered from 1 to _n_.

Output

If they can pass all the levels, print "I become the guy.". If it's
impossible, print "Oh, my keyboard!" (without the quotes).

Examples

Input

    
    
    4  
    3 1 2 3  
    2 2 4  
    

Output

    
    
    I become the guy.  
    

Input

    
    
    4  
    3 1 2 3  
    2 2 3  
    

Output

    
    
    Oh, my keyboard!  
    

Note

In the first sample, Little X can pass levels [1 2 3], and Little Y can pass
level [2 4], so they can pass all the levels both.

In the second sample, no one can pass level 4.

