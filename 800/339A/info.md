# A. Helpful Maths 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/339/A

# A. Helpful Maths
Xenia the beginner mathematician is a third year student at elementary school.
She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should
calculate the sum. To make the calculation easier, the sum only contains
numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning
to count, so she can calculate a sum only if the summands follow in non-
decreasing order. For example, she can't calculate sum 1+3+2+1 but she can
calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and
print the sum in such a way that Xenia can calculate the sum.

Input

The first line contains a non-empty string _s_ — the sum Xenia needs to count.
String _s_ contains no spaces. It only contains digits and characters "+".
Besides, string _s_ is a correct sum of numbers 1, 2 and 3. String _s_ is at
most 100 characters long.

Output

Print the new sum that Xenia can count.

Examples

Input

    
    
    3+2+1  
    

Output

    
    
    1+2+3  
    

Input

    
    
    1+1+3+1+3  
    

Output

    
    
    1+1+1+3+3  
    

Input

    
    
    2  
    

Output

    
    
    2  
    

