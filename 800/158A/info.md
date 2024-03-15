# A. Next Round 
**Difficulty**: 800 
**Link**: https://codeforces.com/problemset/problem/158/A

# A. Next Round
"Contestant who earns a score equal to or greater than the _k_ -th place
finisher's score will advance to the next round, as long as the contestant
earns a positive score..." — an excerpt from contest rules.

A total of _n_ participants took part in the contest (_n_ ≥  _k_), and you
already know their scores. Calculate how many participants will advance to the
next round.

Input

The first line of the input contains two integers _n_ and _k_ (1 ≤  _k_ ≤  _n_
≤ 50) separated by a single space.

The second line contains _n_ space-separated integers _a_ 1,  _a_ 2, ...,  _a_
_n_ (0 ≤  _a_ _i_ ≤ 100), where _a_ _i_ is the score earned by the participant
who got the _i_ -th place. The given sequence is non-increasing (that is, for
all _i_ from 1 to _n_ \- 1 the following condition is fulfilled: _a_ _i_ ≥
_a_ _i_ \+ 1).

Output

Output the number of participants who advance to the next round.

Examples

Input

    
    
    8 5  
    10 9 8 7 7 7 5 5  
    

Output

    
    
    6  
    

Input

    
    
    4 2  
    0 0 0 0  
    

Output

    
    
    0  
    

Note

In the first example the participant on the 5th place earned 7 points. As the
participant on the 6th place also earned 7 points, there are 6 advancers.

In the second example nobody got a positive score.

