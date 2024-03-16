# B. Taxi 
**Difficulty**: 1100 
**Link**: https://codeforces.com/problemset/problem/158/B

# B. Taxi
After the lessons _n_ groups of schoolchildren went outside and decided to
visit Polycarpus to celebrate his birthday. We know that the _i_ -th group
consists of _s_ _i_ friends (1 ≤  _s_ _i_ ≤ 4), and they want to go to
Polycarpus together. They decided to get there by taxi. Each car can carry at
most four passengers. What minimum number of cars will the children need if
all members of each group should ride in the same taxi (but one taxi can take
more than one group)?

Input

The first line contains integer _n_ (1 ≤  _n_ ≤ 105) — the number of groups of
schoolchildren. The second line contains a sequence of integers _s_ 1,  _s_ 2,
...,  _s_ _n_ (1 ≤  _s_ _i_ ≤ 4). The integers are separated by a space, _s_
_i_ is the number of children in the _i_ -th group.

Output

Print the single number — the minimum number of taxis necessary to drive all
children to Polycarpus.

Examples

Input

    
    
    5  
    1 2 4 3 3  
    

Output

    
    
    4  
    

Input

    
    
    8  
    2 3 4 4 2 1 3 1  
    

Output

    
    
    5  
    

Note

In the first test we can sort the children into four cars like this:

  * the third group (consisting of four children), 
  * the fourth group (consisting of three children), 
  * the fifth group (consisting of three children), 
  * the first and the second group (consisting of one and two children, correspondingly). 

There are other ways to sort the groups into four cars.

