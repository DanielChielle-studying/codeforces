# B. Fedor and New Game 
**Difficulty**: 1100 
**Link**: https://codeforces.com/problemset/problem/467/B

After you had helped George and Alex to move in the dorm, they went to help
their friend Fedor play a new computer game «Call of Soldiers 3».

The game has (_m_ \+ 1) players and _n_ types of soldiers in total. Players
«Call of Soldiers 3» are numbered form 1 to (_m_ \+ 1). Types of soldiers are
numbered from 0 to _n_ \- 1. Each player has an army. Army of the _i_ -th
player can be described by non-negative integer _x_ _i_. Consider binary
representation of _x_ _i_ : if the _j_ -th bit of number _x_ _i_ equal to one,
then the army of the _i_ -th player has soldiers of the _j_ -th type.

Fedor is the (_m_ \+ 1)-th player of the game. He assume that two players can
become friends if their armies differ in at most _k_ types of soldiers (in
other words, binary representations of the corresponding numbers differ in at
most _k_ bits). Help Fedor and count how many players can become his friends.

Input

The first line contains three integers _n_ , _m_ , _k_ (1 ≤  _k_ ≤  _n_ ≤ 20;
1 ≤  _m_ ≤ 1000).

The _i_ -th of the next (_m_ \+ 1) lines contains a single integer _x_ _i_ (1
≤  _x_ _i_ ≤ 2 _n_ \- 1), that describes the _i_ -th player's army. We remind
you that Fedor is the (_m_ \+ 1)-th player.

Output

Print a single integer — the number of Fedor's potential friends.

Examples

Input

    
    
    7 3 1  
    8  
    5  
    111  
    17  
    

Output

    
    
    0  
    

Input

    
    
    3 3 3  
    1  
    2  
    3  
    4  
    

Output

    
    
    3  
    

