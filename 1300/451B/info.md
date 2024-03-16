# B. Sort the Array 
**Difficulty**: 1300 
**Link**: https://codeforces.com/problemset/problem/451/B

# B. Sort the Array
Being a programmer, you like arrays a lot. For your birthday, your friends
have given you an array _a_ consisting of _n_ distinct integers.

Unfortunately, the size of _a_ is too small. You want a bigger array! Your
friends agree to give you a bigger array, but only if you are able to answer
the following question correctly: is it possible to sort the array _a_ (in
increasing order) by reversing exactly one segment of _a_? See definitions of
segment and reversing in the notes.

Input

The first line of the input contains an integer _n_ (1 ≤  _n_ ≤ 105) — the
size of array _a_.

The second line contains _n_ distinct space-separated integers: _a_[1],
_a_[2], ...,  _a_[_n_] (1 ≤  _a_[_i_] ≤ 109).

Output

Print "yes" or "no" (without quotes), depending on the answer.

If your answer is "yes", then also print two space-separated integers denoting
start and end (start must not be greater than end) indices of the segment to
be reversed. If there are multiple ways of selecting these indices, print any
of them.

Examples

Input

    
    
    3  
    3 2 1  
    

Output

    
    
    yes  
    1 3  
    

Input

    
    
    4  
    2 1 3 4  
    

Output

    
    
    yes  
    1 2  
    

Input

    
    
    4  
    3 1 2 4  
    

Output

    
    
    no  
    

Input

    
    
    2  
    1 2  
    

Output

    
    
    yes  
    1 1  
    

Note

Sample 1. You can reverse the entire array to get [1, 2, 3], which is sorted.

Sample 3. No segment can be reversed such that the array will be sorted.

Definitions

A segment [_l_ ,  _r_] of array _a_ is the sequence _a_[_l_],  _a_[_l_ \+ 1],
...,  _a_[_r_].

If you have an array _a_ of size _n_ and you reverse its segment [_l_ ,  _r_],
the array will become:

_a_[1],  _a_[2], ...,  _a_[_l_ \- 2],  _a_[_l_ \- 1],  _a_[_r_],  _a_[_r_ \-
1], ...,  _a_[_l_ \+ 1],  _a_[_l_],  _a_[_r_ \+ 1],  _a_[_r_ \+ 2], ...,
_a_[_n_ \- 1],  _a_[_n_].

