# A. Gravity Flip 
**Difficulty**: 900 
**Link**: https://codeforces.com/problemset/problem/405/A

# A. Gravity Flip
Little Chris is bored during his physics lessons (too easy), so he has built a
toy box to keep himself occupied. The box is special, since it has the ability
to change gravity.

There are _n_ columns of toy cubes in the box arranged in a line. The _i_ -th
column contains _a_ _i_ cubes. At first, the gravity in the box is pulling the
cubes downwards. When Chris switches the gravity, it begins to pull all the
cubes to the right side of the box. The figure shows the initial and final
configurations of the cubes in the box: the cubes that have changed their
position are highlighted with orange.

![](https://espresso.codeforces.com/383cc55fefceeac300e8d90362dca986d56b436a.png)

Given the initial configuration of the toy cubes in the box, find the amounts
of cubes in each of the _n_ columns after the gravity switch!

Input

The first line of input contains an integer _n_ (1 ≤  _n_ ≤ 100), the number
of the columns in the box. The next line contains _n_ space-separated integer
numbers. The _i_ -th number _a_ _i_ (1 ≤  _a_ _i_ ≤ 100) denotes the number of
cubes in the _i_ -th column.

Output

Output _n_ integer numbers separated by spaces, where the _i_ -th number is
the amount of cubes in the _i_ -th column after the gravity switch.

Examples

Input

    
    
    4  
    3 2 1 2  
    

Output

    
    
    1 2 2 3   
    

Input

    
    
    3  
    2 3 8  
    

Output

    
    
    2 3 8   
    

Note

The first example case is shown on the figure. The top cube of the first
column falls to the top of the last column; the top cube of the second column
falls to the top of the third column; the middle cube of the first column
falls to the top of the second column.

In the second example case the gravity switch does not change the heights of
the columns.

