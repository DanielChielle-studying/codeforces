# A. New Year Transportation 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/500/A

# A. New Year Transportation
New Year is coming in Line World! In this world, there are _n_ cells numbered
by integers from 1 to _n_ , as a 1 ×  _n_ board. People live in cells.
However, it was hard to move between distinct cells, because of the difficulty
of escaping the cell. People wanted to meet people who live in other cells.

So, user tncks0121 has made a transportation system to move between these
cells, to celebrate the New Year. First, he thought of _n_ \- 1 positive
integers _a_ 1,  _a_ 2, ...,  _a_ _n_ \- 1. For every integer _i_ where 1 ≤
_i_ ≤  _n_ \- 1 the condition 1 ≤  _a_ _i_ ≤  _n_ \-  _i_ holds. Next, he made
_n_ \- 1 portals, numbered by integers from 1 to _n_ \- 1. The _i_ -th (1 ≤
_i_ ≤  _n_ \- 1) portal connects cell _i_ and cell (_i_ \+  _a_ _i_), and one
can travel from cell _i_ to cell (_i_ \+  _a_ _i_) using the _i_ -th portal.
Unfortunately, one cannot use the portal backwards, which means one cannot
move from cell (_i_ \+  _a_ _i_) to cell _i_ using the _i_ -th portal. It is
easy to see that because of condition 1 ≤  _a_ _i_ ≤  _n_ \-  _i_ one can't
leave the Line World using portals.

Currently, I am standing at cell 1, and I want to go to cell _t_. However, I
don't know whether it is possible to go there. Please determine whether I can
go to cell _t_ by only using the construted transportation system.

Input

The first line contains two space-separated integers _n_ (3 ≤  _n_ ≤ 3 × 104)
and _t_ (2 ≤  _t_ ≤  _n_) — the number of cells, and the index of the cell
which I want to go to.

The second line contains _n_ \- 1 space-separated integers _a_ 1,  _a_ 2, ...,
_a_ _n_ \- 1 (1 ≤  _a_ _i_ ≤  _n_ \-  _i_). It is guaranteed, that using the
given transportation system, one cannot leave the Line World.

Output

If I can go to cell _t_ using the transportation system, print "YES".
Otherwise, print "NO".

Examples

Input

    
    
    8 4  
    1 2 1 2 1 2 1  
    

Output

    
    
    YES  
    

Input

    
    
    8 5  
    1 2 1 2 1 1 1  
    

Output

    
    
    NO  
    

Note

In the first sample, the visited cells are: 1, 2, 4; so we can successfully
visit the cell 4.

In the second sample, the possible cells to visit are: 1, 2, 4, 6, 7, 8; so we
can't visit the cell 5, which we want to visit.

