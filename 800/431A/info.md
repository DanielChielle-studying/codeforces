# A. Black Square 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/431/A

# A. Black Square
Quite recently, a very smart student named Jury decided that lectures are
boring, so he downloaded a game called "Black Square" on his super cool
touchscreen phone.

In this game, the phone's screen is divided into four vertical strips. Each
second, a black square appears on some of the strips. According to the rules
of the game, Jury must use this second to touch the corresponding strip to
make the square go away. As Jury is both smart and lazy, he counted that he
wastes exactly _a_ _i_ calories on touching the _i_ -th strip.

You've got a string _s_ , describing the process of the game and numbers _a_
1,  _a_ 2,  _a_ 3,  _a_ 4. Calculate how many calories Jury needs to destroy
all the squares?

Input

The first line contains four space-separated integers _a_ 1, _a_ 2, _a_ 3, _a_
4 (0 ≤  _a_ 1,  _a_ 2,  _a_ 3,  _a_ 4 ≤ 104).

The second line contains string _s_ (1 ≤ |_s_ | ≤ 105), where the _і_ -th character of the string equals "1", if on the _i_ -th second of the game the square appears on the first strip, "2", if it appears on the second strip, "3", if it appears on the third strip, "4", if it appears on the fourth strip.

Output

Print a single integer — the total number of calories that Jury wastes.

Examples

Input

    
    
    1 2 3 4  
    123214  
    

Output

    
    
    13  
    

Input

    
    
    1 5 3 2  
    11221  
    

Output

    
    
    13  
    

