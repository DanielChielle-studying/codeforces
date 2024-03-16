# A. Expression 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/479/A

# A. Expression
Petya studies in a school and he adores Maths. His class has been studying
arithmetic expressions. On the last class the teacher wrote three positive
integers _a_ , _b_ , _c_ on the blackboard. The task was to insert signs of
operations '+' and '*', and probably brackets between the numbers so that the
value of the resulting expression is as large as possible. Let's consider an
example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard.
Here are some ways of placing signs and brackets:

  * 1+2*3=7 
  * 1*(2+3)=5 
  * 1*2*3=6 
  * (1+2)*3=9 

Note that you can insert operation signs only between _a_ and _b_ , and
between _b_ and _c_ , that is, you cannot swap integers. For instance, in the
given sample you cannot get expression (1+3)*2.

It's easy to see that the maximum value that you can obtain is 9.

Your task is: given _a_ , _b_ and _c_ print the maximum value that you can
get.

Input

The input contains three integers _a_ , _b_ and _c_ , each on a single line (1
≤  _a_ ,  _b_ ,  _c_ ≤ 10).

Output

Print the maximum value of the expression that you can obtain.

Examples

Input

    
    
    1  
    2  
    3  
    

Output

    
    
    9  
    

Input

    
    
    2  
    10  
    3  
    

Output

    
    
    60  
    

