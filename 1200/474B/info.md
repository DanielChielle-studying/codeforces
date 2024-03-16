# B. Worms 
**Difficulty**: 1200 
**Link**: https://codeforces.com/problemset/problem/474/B

# B. Worms
It is lunch time for Mole. His friend, Marmot, prepared him a nice game for
lunch.

Marmot brought Mole _n_ ordered piles of worms such that _i_ -th pile contains
_a_ _i_ worms. He labeled all these worms with consecutive integers: worms in
first pile are labeled with numbers 1 to _a_ 1, worms in second pile are
labeled with numbers _a_ 1 \+ 1 to _a_ 1 \+  _a_ 2 and so on. See the example
for a better understanding.

Mole can't eat all the worms (Marmot brought a lot) and, as we all know, Mole
is blind, so Marmot tells him the labels of the best juicy worms. Marmot will
only give Mole a worm if Mole says correctly in which pile this worm is
contained.

Poor Mole asks for your help. For all juicy worms said by Marmot, tell Mole
the correct answers.

Input

The first line contains a single integer _n_ (1 ≤  _n_ ≤ 105), the number of
piles.

The second line contains _n_ integers _a_ 1,  _a_ 2, ...,  _a_ _n_ (1 ≤  _a_
_i_ ≤ 103, _a_ 1 \+  _a_ 2 \+ ... +  _a_ _n_ ≤ 106), where _a_ _i_ is the
number of worms in the _i_ -th pile.

The third line contains single integer _m_ (1 ≤  _m_ ≤ 105), the number of
juicy worms said by Marmot.

The fourth line contains _m_ integers _q_ 1,  _q_ 2, ...,  _q_ _m_ (1 ≤  _q_
_i_ ≤  _a_ 1 \+  _a_ 2 \+ ... +  _a_ _n_), the labels of the juicy worms.

Output

Print _m_ lines to the standard output. The _i_ -th line should contain an
integer, representing the number of the pile where the worm labeled with the
number _q_ _i_ is.

Examples

Input

    
    
    5  
    2 7 3 4 9  
    3  
    1 25 11  
    

Output

    
    
    1  
    5  
    3  
    

Note

For the sample input:

  * The worms with labels from [1, 2] are in the first pile. 
  * The worms with labels from [3, 9] are in the second pile. 
  * The worms with labels from [10, 12] are in the third pile. 
  * The worms with labels from [13, 16] are in the fourth pile. 
  * The worms with labels from [17, 25] are in the fifth pile. 

