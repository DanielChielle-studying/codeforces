# B. Random Teams 
**Difficulty**: 1300 
**Link**: https://codeforces.com/problemset/problem/478/B

# B. Random Teams
 _n_ participants of the competition were split into _m_ teams in some manner
so that each team has at least one participant. After the competition each
pair of participants from the same team became friends.

Your task is to write a program that will find the minimum and the maximum
number of pairs of friends that could have formed by the end of the
competition.

Input

The only line of input contains two integers _n_ and _m_ , separated by a
single space (1 ≤  _m_ ≤  _n_ ≤ 109) — the number of participants and the
number of teams respectively.

Output

The only line of the output should contain two integers _k_ _min_ and _k_
_max_ — the minimum possible number of pairs of friends and the maximum
possible number of pairs of friends respectively.

Examples

Input

    
    
    5 1  
    

Output

    
    
    10 10  
    

Input

    
    
    3 2  
    

Output

    
    
    1 1  
    

Input

    
    
    6 3  
    

Output

    
    
    3 6  
    

Note

In the first sample all the participants get into one team, so there will be
exactly ten pairs of friends.

In the second sample at any possible arrangement one team will always have two
participants and the other team will always have one participant. Thus, the
number of pairs of friends will always be equal to one.

In the third sample minimum number of newly formed friendships can be achieved
if participants were split on teams consisting of 2 people, maximum number can
be achieved if participants were split on teams of 1, 1 and 4 people.

