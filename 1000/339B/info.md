# B. Xenia and Ringroad 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/339/B

# B. Xenia and Ringroad
Xenia lives in a city that has _n_ houses built along the main ringroad. The
ringroad houses are numbered 1 through _n_ in the clockwise order. The
ringroad traffic is one way and also is clockwise.

Xenia has recently moved into the ringroad house number 1. As a result, she's
got _m_ things to do. In order to complete the _i_ -th task, she needs to be
in the house number _a_ _i_ and complete all tasks with numbers less than _i_.
Initially, Xenia is in the house number 1, find the minimum time she needs to
complete all her tasks if moving from a house to a neighboring one along the
ringroad takes one unit of time.

Input

The first line contains two integers _n_ and _m_ (2 ≤  _n_ ≤ 105, 1 ≤  _m_ ≤
105). The second line contains _m_ integers _a_ 1,  _a_ 2, ...,  _a_ _m_ (1 ≤
_a_ _i_ ≤  _n_). Note that Xenia can have multiple consecutive tasks in one
house.

Output

Print a single integer — the time Xenia needs to complete all tasks.

Please, do not use the %lld specifier to read or write 64-bit integers in С++.
It is preferred to use the cin, cout streams or the %I64d specifier.

Examples

Input

    
    
    4 3  
    3 2 3  
    

Output

    
    
    6  
    

Input

    
    
    4 3  
    2 3 3  
    

Output

    
    
    2  
    

Note

In the first test example the sequence of Xenia's moves along the ringroad
looks as follows: 1 → 2 → 3 → 4 → 1 → 2 → 3. This is optimal sequence. So, she
needs 6 time units.

