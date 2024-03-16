# B. Fence 
**Difficulty**: 1100 
**Link**: https://codeforces.com/problemset/problem/363/B

# B. Fence
There is a fence in front of Polycarpus's home. The fence consists of _n_
planks of the same width which go one after another from left to right. The
height of the _i_ -th plank is _h_ _i_ meters, distinct planks can have
distinct heights.

![](https://espresso.codeforces.com/f6aed87382b8964ec019d349490eab55c60e6602.png)
Fence for _n_ = 7 and _h_ = [1, 2, 6, 1, 1, 7, 1]

Polycarpus has bought a posh piano and is thinking about how to get it into
the house. In order to carry out his plan, he needs to take exactly _k_
consecutive planks from the fence. Higher planks are harder to tear off the
fence, so Polycarpus wants to find such _k_ consecutive planks that the sum of
their heights is minimal possible.

Write the program that finds the indexes of _k_ consecutive planks with
minimal total height. Pay attention, the fence is not around Polycarpus's
home, it is in front of home (in other words, the fence isn't cyclic).

Input

The first line of the input contains integers _n_ and _k_ (1 ≤  _n_ ≤ 1.5·105,
1 ≤  _k_ ≤  _n_) — the number of planks in the fence and the width of the hole
for the piano. The second line contains the sequence of integers _h_ 1,  _h_
2, ...,  _h_ _n_ (1 ≤  _h_ _i_ ≤ 100), where _h_ _i_ is the height of the _i_
-th plank of the fence.

Output

Print such integer _j_ that the sum of the heights of planks _j_ , _j_ \+ 1,
..., _j_ \+  _k_ \- 1 is the minimum possible. If there are multiple such _j_
's, print any of them.

Examples

Input

    
    
    7 3  
    1 2 6 1 1 7 1  
    

Output

    
    
    3  
    

Note

In the sample, your task is to find three consecutive planks with the minimum
sum of heights. In the given case three planks with indexes 3, 4 and 5 have
the required attribute, their total height is 8.

