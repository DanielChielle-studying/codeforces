# A. Party 
**Difficulty**: 900 
**Link**: https://codeforces.com/problemset/problem/115/A

A company has _n_ employees numbered from 1 to _n_. Each employee either has
no immediate manager or exactly one immediate manager, who is another employee
with a different number. An employee _A_ is said to be the superior of another
employee _B_ if at least one of the following is true:

  * Employee _A_ is the immediate manager of employee _B_
  * Employee _B_ has an immediate manager employee _C_ such that employee _A_ is the superior of employee _C_. 

The company will not have a managerial cycle. That is, there will not exist an
employee who is the superior of his/her own immediate manager.

Today the company is going to arrange a party. This involves dividing all _n_
employees into several groups: every employee must belong to exactly one
group. Furthermore, within any single group, there must not be two employees
_A_ and _B_ such that _A_ is the superior of _B_.

What is the minimum number of groups that must be formed?

Input

The first line contains integer _n_ (1 ≤  _n_ ≤ 2000) — the number of
employees.

The next _n_ lines contain the integers _p_ _i_ (1 ≤  _p_ _i_ ≤  _n_ or _p_
_i_ = -1). Every _p_ _i_ denotes the immediate manager for the _i_ -th
employee. If _p_ _i_ is -1, that means that the _i_ -th employee does not have
an immediate manager.

It is guaranteed, that no employee will be the immediate manager of
him/herself (_p_ _i_ ≠  _i_). Also, there will be no managerial cycles.

Output

Print a single integer denoting the minimum number of groups that will be
formed in the party.

Examples

Input

    
    
    5  
    -1  
    1  
    2  
    1  
    -1  
    

Output

    
    
    3  
    

Note

For the first example, three groups are sufficient, for example:

  * Employee 1 
  * Employees 2 and 4 
  * Employees 3 and 5 

