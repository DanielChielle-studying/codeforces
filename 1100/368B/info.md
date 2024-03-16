# B. Sereja and Suffixes 
**Difficulty**: 1100 
**Link**: https://codeforces.com/problemset/problem/368/B

# B. Sereja and Suffixes
Sereja has an array _a_ , consisting of _n_ integers _a_ 1, _a_ 2, ..., _a_
_n_. The boy cannot sit and do nothing, he decided to study an array. Sereja
took a piece of paper and wrote out _m_ integers _l_ 1,  _l_ 2, ...,  _l_ _m_
(1 ≤  _l_ _i_ ≤  _n_). For each number _l_ _i_ he wants to know how many
distinct numbers are staying on the positions _l_ _i_ , _l_ _i_ \+ 1, ...,
_n_. Formally, he want to find the number of distinct numbers among _a_ _l_
_i_ ,  _a_ _l_ _i_ \+ 1, ...,  _a_ _n_.?

Sereja wrote out the necessary array elements but the array was so large and
the boy was so pressed for time. Help him, find the answer for the described
question for each _l_ _i_.

Input

The first line contains two integers _n_ and _m_ (1 ≤  _n_ ,  _m_ ≤ 105). The
second line contains _n_ integers _a_ 1, _a_ 2, ..., _a_ _n_ (1 ≤  _a_ _i_ ≤
105) — the array elements.

Next _m_ lines contain integers _l_ 1,  _l_ 2, ...,  _l_ _m_. The _i_ -th line
contains integer _l_ _i_ (1 ≤  _l_ _i_ ≤  _n_).

Output

Print _m_ lines — on the _i_ -th line print the answer to the number _l_ _i_.

Examples

Input

    
    
    10 10  
    1 2 3 4 1 2 3 4 100000 99999  
    1  
    2  
    3  
    4  
    5  
    6  
    7  
    8  
    9  
    10  
    

Output

    
    
    6  
    6  
    6  
    6  
    6  
    5  
    4  
    3  
    2  
    1  
    

