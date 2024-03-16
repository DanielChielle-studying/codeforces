# A. Dreamoon and Stairs 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/476/A

# A. Dreamoon and Stairs
Dreamoon wants to climb up a stair of _n_ steps. He can climb 1 or 2 steps at
each move. Dreamoon wants the number of moves to be a multiple of an integer
_m_.

What is the minimal number of moves making him climb to the top of the stairs
that satisfies his condition?

Input

The single line contains two space separated integers _n_ , _m_ (0 <  _n_ ≤
10000, 1 <  _m_ ≤ 10).

Output

Print a single integer — the minimal number of moves being a multiple of _m_.
If there is no way he can climb satisfying condition print  \- 1 instead.

Examples

Input

    
    
    10 2  
    

Output

    
    
    6  
    

Input

    
    
    3 5  
    

Output

    
    
    -1  
    

Note

For the first sample, Dreamoon could climb in 6 moves with following sequence
of steps: {2, 2, 2, 2, 1, 1}.

For the second sample, there are only three valid sequence of steps {2, 1},
{1, 2}, {1, 1, 1} with 2, 2, and 3 steps respectively. All these numbers are
not multiples of 5.

