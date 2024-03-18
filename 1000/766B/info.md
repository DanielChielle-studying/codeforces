# B. Mahmoud and a Triangle 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/766/B

Mahmoud has _n_ line segments, the _i_ -th of them has length _a_ _i_. Ehab
challenged him to use exactly 3 line segments to form a non-degenerate
triangle. Mahmoud doesn't accept challenges unless he is sure he can win, so
he asked you to tell him if he should accept the challenge. Given the lengths
of the line segments, check if he can choose exactly 3 of them to form a non-
degenerate triangle.

Mahmoud should use exactly 3 line segments, he can't concatenate two line
segments or change any length. A non-degenerate triangle is a triangle with
positive area.

Input

The first line contains single integer _n_ (3 ≤  _n_ ≤ 105) — the number of
line segments Mahmoud has.

The second line contains _n_ integers _a_ 1,  _a_ 2, ...,  _a_ _n_ (1 ≤  _a_
_i_ ≤ 109) — the lengths of line segments Mahmoud has.

Output

In the only line print "YES" if he can choose exactly three line segments and
form a non-degenerate triangle with them, and "NO" otherwise.

Examples

Input

    
    
    5  
    1 5 3 2 4  
    

Output

    
    
    YES  
    

Input

    
    
    3  
    4 1 2  
    

Output

    
    
    NO  
    

Note

For the first example, he can use line segments with lengths 2, 4 and 5 to
form a non-degenerate triangle.

