# A. Vanya and Fence 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/677/A

# A. Vanya and Fence
Vanya and his friends are walking along the fence of height _h_ and they do
not want the guard to notice them. In order to achieve this the height of each
of the friends should not exceed _h_. If the height of some person is greater
than _h_ he can bend down and then he surely won't be noticed by the guard.
The height of the _i_ -th person is equal to _a_ _i_.

Consider the width of the person walking as usual to be equal to 1, while the
width of the bent person is equal to 2. Friends want to talk to each other
while walking, so they would like to walk in a single row. What is the minimum
width of the road, such that friends can walk in a row and remain unattended
by the guard?

Input

The first line of the input contains two integers _n_ and _h_ (1 ≤  _n_ ≤
1000, 1 ≤  _h_ ≤ 1000) — the number of friends and the height of the fence,
respectively.

The second line contains _n_ integers _a_ _i_ (1 ≤  _a_ _i_ ≤ 2 _h_), the _i_
-th of them is equal to the height of the _i_ -th person.

Output

Print a single integer — the minimum possible valid width of the road.

Examples

Input

    
    
    3 7  
    4 5 14  
    

Output

    
    
    4  
    

Input

    
    
    6 1  
    1 1 1 1 1 1  
    

Output

    
    
    6  
    

Input

    
    
    6 5  
    7 6 8 9 10 5  
    

Output

    
    
    11  
    

Note

In the first sample, only person number 3 must bend down, so the required
width is equal to 1 + 1 + 2 = 4.

In the second sample, all friends are short enough and no one has to bend, so
the width 1 + 1 + 1 + 1 + 1 + 1 = 6 is enough.

In the third sample, all the persons have to bend, except the last one. The
required minimum width of the road is equal to 2 + 2 + 2 + 2 + 2 + 1 = 11.

