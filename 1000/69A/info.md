# A. Young Physicist 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/69/A

# A. Young Physicist
A guy named Vasya attends the final grade of a high school. One day Vasya
decided to watch a match of his favorite hockey team. And, as the boy loves
hockey very much, even more than physics, he forgot to do the homework.
Specifically, he forgot to complete his physics tasks. Next day the teacher
got very angry at Vasya and decided to teach him a lesson. He gave the lazy
student a seemingly easy task: You are given an idle body in space and the
forces that affect it. The body can be considered as a material point with
coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium.
"Piece of cake" — thought Vasya, we need only to check if the sum of all
vectors is equal to 0. So, Vasya began to solve the problem. But later it
turned out that there can be lots and lots of these forces, and Vasya can not
cope without your help. Help him. Write a program that determines whether a
body is idle or is moving by the given vectors of forces.

Input

The first line contains a positive integer _n_ (1 ≤  _n_ ≤ 100), then follow
_n_ lines containing three integers each: the _x_ _i_ coordinate, the _y_ _i_
coordinate and the _z_ _i_ coordinate of the force vector, applied to the body
( \- 100 ≤  _x_ _i_ ,  _y_ _i_ ,  _z_ _i_ ≤ 100).

Output

Print the word "YES" if the body is in equilibrium, or the word "NO" if it is
not.

Examples

Input

    
    
    3  
    4 1 7  
    -2 4 -1  
    1 -5 -3  
    

Output

    
    
    NO

Input

    
    
    3  
    3 -1 7  
    -5 2 -4  
    2 -1 -3  
    

Output

    
    
    YES

