# A. Presents 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/136/A

# A. Presents
Little Petya very much likes gifts. Recently he has received a new laptop as a
New Year gift from his mother. He immediately decided to give it to somebody
else as what can be more pleasant than giving somebody gifts. And on this
occasion he organized a New Year party at his place and invited _n_ his
friends there.

If there's one thing Petya likes more that receiving gifts, that's watching
others giving gifts to somebody else. Thus, he safely hid the laptop until the
next New Year and made up his mind to watch his friends exchanging gifts while
he does not participate in the process. He numbered all his friends with
integers from 1 to _n_. Petya remembered that a friend number _i_ gave a gift
to a friend number _p_ _i_. He also remembered that each of his friends
received exactly one gift.

Now Petya wants to know for each friend _i_ the number of a friend who has
given him a gift.

Input

The first line contains one integer _n_ (1 ≤  _n_ ≤ 100) — the quantity of
friends Petya invited to the party. The second line contains _n_ space-
separated integers: the _i_ -th number is _p_ _i_ — the number of a friend who
gave a gift to friend number _i_. It is guaranteed that each friend received
exactly one gift. It is possible that some friends do not share Petya's ideas
of giving gifts to somebody else. Those friends gave the gifts to themselves.

Output

Print _n_ space-separated integers: the _i_ -th number should equal the number
of the friend who gave a gift to friend number _i_.

Examples

Input

    
    
    4  
    2 3 4 1  
    

Output

    
    
    4 1 2 3  
    

Input

    
    
    3  
    1 3 2  
    

Output

    
    
    1 3 2  
    

Input

    
    
    2  
    1 2  
    

Output

    
    
    1 2  
    

