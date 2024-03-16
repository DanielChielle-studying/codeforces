# A. Jzzhu and Children 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/450/A

# A. Jzzhu and Children
There are _n_ children in Jzzhu's school. Jzzhu is going to give some candies
to them. Let's number all the children from 1 to _n_. The _i_ -th child wants
to get at least _a_ _i_ candies.

Jzzhu asks children to line up. Initially, the _i_ -th child stands at the _i_
-th place of the line. Then Jzzhu start distribution of the candies. He
follows the algorithm:

  1. Give _m_ candies to the first child of the line. 
  2. If this child still haven't got enough candies, then the child goes to the end of the line, else the child go home. 
  3. Repeat the first two steps while the line is not empty. 

Consider all the children in the order they go home. Jzzhu wants to know,
which child will be the last in this order?

Input

The first line contains two integers _n_ ,  _m_ (1 ≤  _n_ ≤ 100; 1 ≤  _m_ ≤
100). The second line contains _n_ integers _a_ 1,  _a_ 2, ...,  _a_ _n_ (1 ≤
_a_ _i_ ≤ 100).

Output

Output a single integer, representing the number of the last child.

Examples

Input

    
    
    5 2  
    1 3 1 4 2  
    

Output

    
    
    4  
    

Input

    
    
    6 4  
    1 1 2 2 3 3  
    

Output

    
    
    6  
    

Note

Let's consider the first sample.

Firstly child 1 gets 2 candies and go home. Then child 2 gets 2 candies and go
to the end of the line. Currently the line looks like [3, 4, 5, 2] (indices of
the children in order of the line). Then child 3 gets 2 candies and go home,
and then child 4 gets 2 candies and goes to the end of the line. Currently the
line looks like [5, 2, 4]. Then child 5 gets 2 candies and goes home. Then
child 2 gets two candies and goes home, and finally child 4 gets 2 candies and
goes home.

Child 4 is the last one who goes home.

