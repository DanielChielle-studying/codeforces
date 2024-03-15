# A. Business trip 
**Difficulty**: 900 
**Link**: https://codeforces.com/problemset/problem/149/A

# A. Business trip
What joy! Petya's parents went on a business trip for the whole year and the
playful kid is left all by himself. Petya got absolutely happy. He jumped on
the bed and threw pillows all day long, until...

Today Petya opened the cupboard and found a scary note there. His parents had
left him with duties: he should water their favourite flower all year, each
day, in the morning, in the afternoon and in the evening. "Wait a second!" —
thought Petya. He know for a fact that if he fulfills the parents' task in the
_i_ -th (1 ≤  _i_ ≤ 12) month of the year, then the flower will grow by _a_
_i_ centimeters, and if he doesn't water the flower in the _i_ -th month, then
the flower won't grow this month. Petya also knows that try as he might, his
parents won't believe that he has been watering the flower if it grows
strictly less than by _k_ centimeters.

Help Petya choose the minimum number of months when he will water the flower,
given that the flower should grow no less than by _k_ centimeters.

Input

The first line contains exactly one integer _k_ (0 ≤  _k_ ≤ 100). The next
line contains twelve space-separated integers: the _i_ -th (1 ≤  _i_ ≤ 12)
number in the line represents _a_ _i_ (0 ≤  _a_ _i_ ≤ 100).

Output

Print the only integer — the minimum number of months when Petya has to water
the flower so that the flower grows no less than by _k_ centimeters. If the
flower can't grow by _k_ centimeters in a year, print -1.

Examples

Input

    
    
    5  
    1 1 1 1 2 2 3 2 2 1 1 1  
    

Output

    
    
    2  
    

Input

    
    
    0  
    0 0 0 0 0 0 0 1 1 2 3 0  
    

Output

    
    
    0  
    

Input

    
    
    11  
    1 1 4 1 1 5 1 1 4 1 1 1  
    

Output

    
    
    3  
    

Note

Let's consider the first sample test. There it is enough to water the flower
during the seventh and the ninth month. Then the flower grows by exactly five
centimeters.

In the second sample Petya's parents will believe him even if the flower
doesn't grow at all (_k_ = 0). So, it is possible for Petya not to water the
flower at all.

