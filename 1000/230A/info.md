# A. Dragons 
**Difficulty**: 1000 
**Link**: https://codeforces.com/problemset/problem/230/A

# A. Dragons
Kirito is stuck on a level of the MMORPG he is playing now. To move on in the
game, he's got to defeat all _n_ dragons that live on this level. Kirito and
the dragons have strength, which is represented by an integer. In the duel
between two opponents the duel's outcome is determined by their strength.
Initially, Kirito's strength equals _s_.

If Kirito starts duelling with the _i_ -th (1 ≤  _i_ ≤  _n_) dragon and
Kirito's strength is not greater than the dragon's strength _x_ _i_ , then
Kirito loses the duel and dies. But if Kirito's strength is greater than the
dragon's strength, then he defeats the dragon and gets a bonus strength
increase by _y_ _i_.

Kirito can fight the dragons in any order. Determine whether he can move on to
the next level of the game, that is, defeat all dragons without a single loss.

Input

The first line contains two space-separated integers _s_ and _n_ (1 ≤  _s_ ≤
104, 1 ≤  _n_ ≤ 103). Then _n_ lines follow: the _i_ -th line contains space-
separated integers _x_ _i_ and _y_ _i_ (1 ≤  _x_ _i_ ≤ 104, 0 ≤  _y_ _i_ ≤
104) — the _i_ -th dragon's strength and the bonus for defeating it.

Output

On a single line print "YES" (without the quotes), if Kirito can move on to
the next level and print "NO" (without the quotes), if he can't.

Examples

Input

    
    
    2 2  
    1 99  
    100 0  
    

Output

    
    
    YES  
    

Input

    
    
    10 1  
    100 100  
    

Output

    
    
    NO  
    

Note

In the first sample Kirito's strength initially equals 2. As the first
dragon's strength is less than 2, Kirito can fight it and defeat it. After
that he gets the bonus and his strength increases to 2 + 99 = 101. Now he can
defeat the second dragon and move on to the next level.

In the second sample Kirito's strength is too small to defeat the only dragon
and win.

