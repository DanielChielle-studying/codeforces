# A. Stones on the Table 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/266/A

# A. Stones on the Table
There are _n_ stones on the table in a row, each of them can be red, green or
blue. Count the minimum number of stones to take from the table so that any
two neighboring stones had different colors. Stones in a row are considered
neighboring if there are no other stones between them.

Input

The first line contains integer _n_ (1 ≤  _n_ ≤ 50) — the number of stones on
the table.

The next line contains string _s_ , which represents the colors of the stones.
We'll consider the stones in the row numbered from 1 to _n_ from left to
right. Then the _i_ -th character _s_ equals "R", if the _i_ -th stone is red,
"G", if it's green and "B", if it's blue.

Output

Print a single integer — the answer to the problem.

Examples

Input

    
    
    3  
    RRG  
    

Output

    
    
    1  
    

Input

    
    
    5  
    RRRRR  
    

Output

    
    
    4  
    

Input

    
    
    4  
    BRBG  
    

Output

    
    
    0  
    

